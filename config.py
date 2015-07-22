import socket, os, os.path
from subprocess import Popen, PIPE
import Websheet
import json

# we already checked for this error in php land
try:
    # a little convoluted to account for possibility this module's loaded from another place
    config_jo = json.loads(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ws-config.json')).read())
    db_enabled = "db-enabled" in config_jo and config_jo["db-enabled"] == True
except:
    config_jo = []
    db_enabled = False

# if you are using safeexec, securely running java should be something like this:
def java_prefix():
    if (config_jo == []): return "error: ws-config.json doesn't exist"
    jail = config_jo["java_jail-abspath"]
    safeexec = config_jo["safeexec-executable-abspath"]    

    java = ["/java/bin/java", "-cp", ".:javax.json-1.0.jar", "-Xmx128M"] # java within jail, using default java_jail config
    safeexec_args = ["--chroot_dir", jail, "--exec_dir", "/cp", "--env_vars", "",
                     "--nproc", "100", "--mem", "10000000", "--nfile", "100", "--gid", "1000", "--clock", "5", "--exec"]
    return [safeexec] + safeexec_args + java

# at princeton, they use "sandbox" instead
if socket.gethostname().endswith("princeton.edu"):
    def java_prefix():
        cos126 = "/n/fs/htdocs/cos126/" # wapps directory
        java = ["/usr/bin/java", "-cp", "java_jail/cp:java_jail/cp/javax.json-1.0.jar", "-Xmx512M"]

        return ["sandbox", "-M", "-i", cos126+"java_jail/cp"] + java

# in either case "java_prefix" is like the 'java' binary,
# ready to accept the class name and cmd line args

def execute(command, the_stdin, input_encoding="UTF-8", output_encoding="UTF-8"):
    proc = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        
    result = proc.communicate(input = the_stdin.encode(input_encoding))
    return Websheet.record(command = command,
                           pwd = os.getcwd(),
                           stdin = the_stdin,
                           stdout = result[0].decode(output_encoding),
                           stderr = result[1].decode(output_encoding),
                           returncode = proc.returncode)
    
def run_java(command, the_stdin = ""):
    return execute(java_prefix() + command, the_stdin)

tempdirs = []
# return new location for temp dir, relative to jail
# e.g. creates and returns "scratch/1237684/"
def create_tempdir():
    import random
    loc = "scratch/" + str(random.randint(100000000000, 999999999999))
    os.mkdir(config_jo["java_jail-abspath"] + loc)
    global tempdirs
    tempdirs += [config_jo["java_jail-abspath"] + loc]
    return loc + "/"

def uncreate_tempdirs():
    import shutil
    for d in tempdirs:
        shutil.rmtree(d)

# database stuff
def connect():
    if not db_enabled: return 
    import mysql.connector
    return mysql.connector.connect(host=config_jo["db-host"],
                                   user=config_jo["db-user"],
                                   password=config_jo["db-password"],
                                   db=config_jo["db-database"])

# don't run if not configured correctly,
# but run if configured correctly & not logged in
def save_submission(student, problem, user_state, result_column, passed):
        if not db_enabled: return
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "insert into ws_history (user, problem, submission, result, passed, meta)" + 
            " VALUES (%s, %s, %s, %s, %s, %s)", 
            (student, 
             problem, 
             json.dumps(user_state),
             json.dumps(result_column),
             passed,
             json.dumps(meta)))
        db.commit()
        cursor.close()
        db.close()

# the rest don't run if not logged in

# returns a json list of code fragments, or False
def load_submission(student, problem, onlyPassed = False, maxId = None):
        if student=="anonymous": return False
        db = connect()
        cursor = db.cursor()
        passed_clause = " AND passed = 1 " if onlyPassed else "" 
        maxid_clause = " AND id <= " + str(maxId) if maxId is not None else ""
        cursor.execute(
            "select submission from ws_history " +
            "WHERE user = %s AND problem = %s "
             + passed_clause + maxid_clause +
            " ORDER BY ID DESC LIMIT 1;",
            (student, 
             problem))
        result = "false"
        for row in cursor:
            result = row[0]
        cursor.close()
        db.close()
        return json.loads(result)

# returns a boolean
def ever_passed(student, problem):
        if student=="anonymous": return False
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "select passed from ws_history WHERE user = %s AND problem = %s AND passed = 1 LIMIT 1;",
            (student, 
             problem))
        result = False
        for row in cursor: # if any results, they've passed it
            result = True
        cursor.close()
        db.close()
        return result

# returns an integer
def num_submissions(student, problem):
        if student=="anonymous": return 0
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "select count(1) from ws_history WHERE user = %s AND problem = %s;",
            (student, 
             problem))
        result = -1
        for row in cursor: # if any results, they've passed it
            result = row[0]
        cursor.close()
        db.close()
        return result

def get_row(query, multiple=False, escapeme=[]):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query, escapeme)
    
    result = [] if multiple else None
    for row in cursor:
        if multiple:
            result.append([x for x in row])
        else:
            result = [x for x in row]
            
    cursor.close()
    db.close()
    return result

def get_rows(query, escapeme=[]):
    return get_row(query, True, escapeme)

