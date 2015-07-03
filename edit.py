#!/usr/bin/python3

import sys, json, config, re

if __name__ == "__main__":
  db = config.connect()
  cursor = db.cursor()

  # should pass message which is a string
  def internal_error(message):
    cursor.close()  
    db.commit()
    db.close()
    print(json.dumps(message))
    sys.exit(0)

  # should pass response which is an object
  def done(**response):
    cursor.close()   
    db.commit()
    db.close()
    print(json.dumps(response))
    sys.exit(0)

  def owner(slug):
    # really should be done with %s but ok since we sanitize
    cursor.execute(
      "select author, action from ws_sheets " +
      "WHERE problem = '"+slug+"' AND action != 'preview' ORDER BY ID DESC LIMIT 1;")
    result = "false"
    for row in cursor:
      author = row[0]
      action = row[1]
      if action == 'delete': return None
      return author
    return None

  def definition(slug, username):
    for definition, sharing, author, action in config.get_rows(
      "select definition, sharing, author, action from ws_sheets " +
      "WHERE problem = '"+slug+"' AND action != 'preview' ORDER BY ID DESC LIMIT 1;"):
      if action == 'delete': continue
      if not sharing.startswith('open') and author != username: continue # closed-source
      if sharing=='open-nosol' and author != username:        
        definition = json.loads(definition)
        if 'choices' in definition:
          definition['choices'] = json.dumps([[x[0], None] for x in json.loads(definition['choices'])])
        if 'answer' in definition:
          definition['answer'] = 'REDACTED'
        if 'source_code' in definition:
          bits = definition['source_code'].split(r'\[')
          for i in range(1, len(bits)):
            if r'\show:' in bits[i]:
              p = bits[i].index(r'\show:')
            elif ']\\' in bits[i]:
              p = bits[i].index(']\\')
            bits[i] = ('\nREDACTED\n' if '\n' in bits[i][:p] else ' REDACTED ') + bits[i][p:]
          definition['source_code'] = r'\['.join(bits)
        definition = json.dumps(definition)
      return definition
    internal_error('Whoa, where did that row go?')

  def list_problems(username):
    result = []

    condition = "action != 'preview'"

    for problem, action, sharing, author in config.get_rows(
      """SELECT o1.problem, o1.action, o1.sharing, o1.author FROM ws_sheets o1
      INNER JOIN (SELECT problem, MAX(id) AS id FROM ws_sheets WHERE """+condition+""" GROUP BY problem) o2
      ON (o1.problem = o2.problem AND o1.id = o2.id);"""):
      if action == 'delete': continue
      if author != username:
        if sharing == 'draft' or sharing == 'hidden': continue
      result.append([problem, author != username, sharing])
    #saner sort, files before folders
    for x in result:
      tmp = x[0].split('/')
      x[0] = [tmp[:-1], tmp[-1]]
    result.sort()
#    print(result)
    for x in result: x[0] = '/'.join(x[0][0]+[x[0][1]])
    return result

  def valid(slug):
    return re.match(r"^([\w-]+/)*[\w-]+$", slug)

  def canedit(slug):
    return owner(slug) in [None, authinfo['username']]
        
  def canread(slug):
    myowner = owner(slug)
    if myowner is None: return False
    if myowner == authinfo['username']: return True
    # ignoring previews, get the latest version
    cursor.execute(
      "select author, action, sharing from ws_sheets " +
      "WHERE problem = '"+slug+"' AND action != 'preview' ORDER BY ID DESC LIMIT 1;")
    result = "false"
    for row in cursor:
      author = row[0]
      action = row[1]
      sharing = row[2]
      return sharing==None or sharing.startswith('open')
    internal_error('Whoa, where did that row go?')

  def get_setting(user, key):
    for (value,) in config.get_rows(
      "select value from ws_settings " +
      "WHERE user = '"+user+"' AND keyname = '"+key+"';"):
      return value

  def set_setting(user, key, value):
    cursor.execute("delete from ws_settings where user = '"+user+"' AND keyname = '"+key+"';")
    cursor.execute("insert into ws_settings (user, keyname, value)" +
                                        " VALUES (%s, %s, %s)",
                                        (user, key, value))
      
  # start of request handling
  request = json.loads("".join(sys.stdin))

  authinfo = request['authinfo']
  problem = request['problem'] if 'problem' in request else None
  action = request['action']  
  if not authinfo["logged_in"] and action != 'listmine':
    internal_error("Only logged-in users can edit")

  if action not in ['listmine', 'settings', 'showgrades'] and not valid(problem):
    if (action == 'load'):
      done(success=False, message="Requested name does not have valid format: <tt>" + problem + "</tt>")
    else:
      internal_error("Does not have valid format: " + problem)
    
  if (action in ['preview', 'save', 'delete']):
    if not canedit(problem):
      internal_error("You don't have edit permissions for " + problem)
    if action == 'delete':
      sharing = None
      definition = None
    else:
      definition = json.loads(request['definition'])
      sharing = 'open-nosol'
      if 'sharing' in definition:
        sharing = definition['sharing']
    # add a row
    cursor.execute("insert into ws_sheets (author, problem, definition, action, sharing)" +
                   " VALUES (%s, %s, %s, %s, %s)",
                   (authinfo['username'], problem, request['definition'], action, sharing))
    done(success=True, message=action + " of " + problem + " successful.")
      
  if (action in ['rename', 'copy']):
    if action == 'copy' and not canread(problem):
      internal_error("You don't have read permissions for " + problem)
    if action == 'rename' and not canedit(problem):
      internal_error("You don't have edit permissions for " + problem)
    newname = request['newname']
    if not valid(newname):
      done(success=False, message="New name does not have valid format: " + newname)
    if owner(newname) != None:
      done(success=False, message="There is already a websheet with this name: " + newname)
    

    definition = json.loads(request['definition'])
    sharing = 'open-nosol'
    if 'sharing' in definition:
      sharing = definition['sharing']

    if action == 'copy':
      if 'remarks' not in definition: definition['remarks'] = ""
      definition['remarks'] = "Copied from problem " + problem + " (author: " + owner(problem) + ")\n" + definition['remarks']

    cursor.execute("insert into ws_sheets (author, problem, definition, action, sharing)" +
                   " VALUES (%s, %s, %s, %s, %s)",
                   (authinfo['username'], newname, json.dumps(definition), 'save', sharing))

    if action == 'rename':      
      cursor.execute("insert into ws_sheets (author, problem, action)" +
                     " VALUES (%s, %s, %s)",
                     (authinfo['username'], problem, 'delete'))
      
    done(success=True, message=action + " of " + problem + " to " + newname + " successful.")

  if action == 'load':
    myowner = owner(problem)
    # if it doesn't exist, everything is good
    if myowner == None:
      done(success=True, message="Loaded " + problem, new=True, canedit=True, author=authinfo['username'])
    # it exists
    if not canread(problem):
      done(success=False, message="You do not have read permissions for: " + problem)
    done(success=True, message="Loaded " + problem, new=False, canedit=myowner == authinfo['username'],
          definition= definition(problem, authinfo['username']), author=myowner)

  if action == 'listmine':
    done(problems = list_problems(authinfo['username']))

  if action == 'settings':
    if 'instructor' in request:
      set_setting(authinfo['username'], 'instructor', request['instructor'])
    inst = get_setting(authinfo['username'], 'instructor')
    if inst is None: inst = ""
    done(success=True, settings={"instructor":inst})
    
  if action == 'showgrades':
    result = {}
    for (student,) in config.get_rows(
      "select user from ws_settings " +
      "WHERE value = '"+authinfo['username']+"' AND keyname = 'instructor';"):
      stuinfo = {}
      for (count, passed, problem) in config.get_rows(
        "select count(1), max(passed), problem from ws_history WHERE user = '"+student+"' group by problem;"):
        stuinfo[problem] = ["Passed" if passed==1 else "Not Passed", str(count)+" Attempts"]
      result[student] = stuinfo
    done(success=True, grades=result)
    
  internal_error('Unknown action ' + action)
