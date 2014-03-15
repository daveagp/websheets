import socket, os
from subprocess import Popen, PIPE
from Websheet import record

def execute(command, the_stdin):
    proc = Popen(command.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result = proc.communicate(input = the_stdin.encode("UTF-8"))
    return record(stdout = result[0].decode("UTF-8"),
                  stderr = result[1].decode("UTF-8"),
                  returncode = proc.returncode)
    

if socket.gethostname().endswith("uwaterloo.ca"):
    jail = "/home/cscircles/dev_java_jail/"
    scratch_dir = jail + "cp/"
    javac = jail + "java/bin/javac -J-Xmx128M -cp . "
    java = "/java/bin/java -cp .:javax.json-1.0.jar -Xmx128M "
    safeexec = "/home/cscircles/dev/safeexec/safeexec"
    safeexec_args = " --chroot_dir "+ jail +" --exec_dir /cp --env_vars '' --nproc 50 --mem 500000 --nfile 30 --clock 2 --exec "
    
    def run_javac(command, the_stdin = ""):
        os.chdir(scratch_dir)
        return execute(javac + command, the_stdin)

    def run_java(command, the_stdin = ""):
        os.chdir(scratch_dir)
        #return execute(java + command, the_stdin)  
        return execute(safeexec + safeexec_args + java + command, the_stdin)  

    def save_submission(*args):
        pass

    def load_submission(student, problem, onlyPassed = False):
        return False

    def ever_passed(student, problem):
        return False

    def num_submissions(student, problem):
        return 0

elif socket.gethostname().endswith("princeton.edu"):
    javac = "/usr/bin/javac -Xlint:path -target 1.7 -cp .:/n/fs/htdocs/cos126/java_jail/cp -J-Xmx128M "
    java = "/usr/bin/java -cp .:/n/fs/htdocs/cos126/java_jail/cp:/n/fs/htdocs/cos126/java_jail/cp/javax.json-1.0.jar -Xmx128M "

    import getpass
    server_username = getpass.getuser()
    scratch_dir = "/n/fs/htdocs/"+server_username+"/"

    def run_javac(command, the_stdin = ""):
        os.chdir(scratch_dir)
        return execute(javac + command, the_stdin)

    def run_java(command, the_stdin = ""):
        os.chdir( "/n/fs/htdocs/"+server_username+"/")
        cmd = "sandbox -M -i /n/fs/htdocs/cos126/java_jail/cp {java}{command}".format(command=command, java=java)

        return execute(cmd, the_stdin)

    def connect():
        import mysql.connector
        return mysql.connector.connect(host='publicdb.cs.princeton.edu', user='cos126',
                                       password=open('/n/fs/htdocs/'+server_username+'/websheets/.dbpwd').read(), db='cos126')

    def save_submission(student, problem, user_state, result_column, passed):
        if student == "fakestudentthatcannotbelogged": return
        import json
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "insert into ws_history (user, problem, submission, result, passed)" + 
            " VALUES (%s, %s, %s, %s, %s)", 
            (student, 
             problem, 
             json.dumps(user_state),
             json.dumps(result_column),
             passed))
        db.commit()
        cursor.close()
        db.close()

    # returns a json list of code fragments
    def load_submission(student, problem, onlyPassed = False):
        import json
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
        import json
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
        import json
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
