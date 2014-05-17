import socket, os
from subprocess import Popen, PIPE
from Websheet import record
import json

# we already checked for this error in php land
try:
    config_jo = json.loads(open('config.json').read())
except:
    config_jo = {}

# if you are using safeexec, securely running java should be something like this:
def compute_java_prefix():
    if (config_jo == {}): return "error: config.json doesn't exist"
    jail = config_jo["java_jail-abspath"]
    safeexec = config_jo["safeexec-executable-abspath"]    

    java = "/java/bin/java -cp .:javax.json-1.0.jar -Xmx128M " # java within jail, using default java_jail config
    safeexec_args = " --chroot_dir "+ jail +" --exec_dir /cp --env_vars '' --nproc 50 --mem 2000000 --nfile 30 --gid 1001 --clock 5 --exec "
    return safeexec + safeexec_args + java

# at princeton, they use "sandbox" instead
if socket.gethostname().endswith("princeton.edu"):
    def compute_java_prefix():
        java = "/usr/bin/java -cp .:/n/fs/htdocs/cos126/java_jail/cp:/n/fs/htdocs/cos126/java_jail/cp/javax.json-1.0.jar -Xmx512M "
        return "sandbox -M -i /n/fs/htdocs/cos126/java_jail/cp "+java

# in either case "java_prefix" is like the 'java' binary,
# ready to accept the class name and cmd line args
java_prefix = compute_java_prefix()

def execute(command, the_stdin):
    proc = Popen(command.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result = proc.communicate(input = the_stdin.encode("UTF-8"))
    return record(stdout = result[0].decode("UTF-8"),
                  stderr = result[1].decode("UTF-8"),
                  returncode = proc.returncode)
    
def run_java(command, the_stdin = ""):
    return execute(java_prefix + command, the_stdin)

# database stuff
def connect():
    import mysql.connector
    return mysql.connector.connect(host=config_jo["db-host"],
                                   user=config_jo["db-user"],
                                   password=config_jo["db-password"],
                                   db=config_jo["db-database"])

# don't run if not configured correctly,
# but run if configured correctly & not logged in
def save_submission(student, problem, user_state, result_column, passed):
        if config_jo == []: return 
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
def load_submission(student, problem, onlyPassed = False):
        if student=="anonymous": return False
        db = connect()
        cursor = db.cursor()
        pc = " AND passed = 1 " if onlyPassed else "" # passed clause
        cursor.execute(
            "select submission from ws_history WHERE user = %s AND problem = %s "+pc+" ORDER BY ID DESC LIMIT 1;",
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
