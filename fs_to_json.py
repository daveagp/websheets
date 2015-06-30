#!/usr/bin/python3
#-*- mode: python -*-

import sys, os, os.path, json, config

db = config.connect()
cursor = db.cursor()

os.chdir('exercises')

for path, folder, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            print(os.path.join(path, file))
            import importlib.machinery
            fullname = os.path.join(path, file)[2:] # remove ./
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

            if 'example' in dicted:
                dicted['example'] = "True" if dicted['example'] else "False"

            cursor.execute("insert into ws_sheets (author, problem, definition, action, sharing)" +
                           " VALUES (%s, %s, %s, %s, %s)",
                           ('daveagp@gmail.com', fullname[:-3], json.dumps(dicted), 'save', 'open-nosol'))
db.commit()
cursor.close()
db.close()
                                                                                                                             
