#!/usr/bin/python3
#-*- mode: python -*-

import sys, os, os.path, json, config

db = config.connect()
cursor = db.cursor()

os.chdir('exercises')

for path, folder, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            #print(os.path.join(path, file))
            import importlib.machinery
            fullname = os.path.join(path, file)[2:] # remove ./
            import socket
            # at usc, put all the cpp stuff in the root
            loader = importlib.machinery.SourceFileLoader(fullname, fullname)
            module = loader.load_module(fullname)

            dicted = {attname: getattr(module, attname) for attname in dir(module) if attname[0]!='_'}

            if 'lang' not in dicted: dicted['lang'] = 'Java'
            if dicted['lang']=='C++':
                tests = dicted['tests']
                for i in range(len(tests)):
                    stdin = tests[i][0]
                    args = tests[i][1]
                    tests[i] = {}
                    if (stdin != ''): tests[i]['stdin'] = stdin
                    if (args != []): tests[i]['args'] = args

            json_fields = ['choices', 'verboten', 'imports', 'dependencies', 'cppflags_add', 'cppflags_remove']
            if dicted['lang'].startswith('C++'):
                json_fields += ['tests']

            for field in json_fields:
                if field in dicted:
                    dicted[field] = json.dumps(dicted[field])

            if 'example' in dicted and 'scratch' not in fullname:
                if dicted['example'] == True:
                    print("UPDATE `wp_16_posts` SET `post_content` = replace(post_content, '"+fullname[4:-3]+"', '", end="")
                    tmp = fullname.split('/')
                    fullname = '/'.join(tmp[:-1]+['examples']+tmp[-1:])
                    print(fullname[4:-3] + "');")
                dicted['example'] = "True" if dicted['example'] else "False"

            marks = ['printseconds', 'cs104', 'mergearrays', 'strcpy', 'strlen', 'cpp/eggs', 'countodd', 'discount',
                     'liebnizapprox', 'revdigits', 'wallisapprox', 'weekday', 'names', 'nxmboard',
                     'ordered_array', 'draw_square', 'remove_factor', 'cmdargs_smartsum', 'cmdargs_sum', 'divide',
                     'roll2', 'combo', 'binsearch', 'binary_search', 'strset', 'var-expr/math'] # continue from random

            default_author = 'daveagp@gmail.com'
            if "usc.edu" in socket.getfqdn() and fullname.startswith("cpp"):
                default_author = 'dpritcha@usc.edu'
            
            for name in marks:
                if name in fullname:
                    #print(fullname)
                    if 'remarks' not in dicted: dicted['remarks'] = ""
                    dicted['remarks'] = "Originally by Mark Redekopp (redekopp@usc.edu) and Dave Pritchard (daveagp@gmail.com)\n" + dicted['remarks']
                    default_author = 'redekopp@usc.edu'

            if 'AboveAverage' in fullname:
                if 'remarks' not in dicted: dicted['remarks'] = ""
                dicted['remarks'] = "Originally by Maia Ginsburg (maia@princeton.edu) and Dave Pritchard (daveagp@gmail.com)\n" + dicted['remarks']
                default_author = 'maia@princeton.edu'

            if 'hw-' not in fullname and 'lab1' not in fullname:
                dicted['sharing'] = 'open'
                dicted['attempts_until_ref'] = '1'

            dbsharing = 'open-nosol' # default
            if 'sharing' in dicted:
                dbsharing = dicted['sharing']
            
            cursor.execute("insert into ws_sheets (author, problem, definition, action, sharing)" +
                           " VALUES (%s, %s, %s, %s, %s)",
                           (default_author, fullname[:-3], json.dumps(dicted), 'save', dbsharing))
db.commit()
cursor.close()
db.close()
                                                                                                                             
