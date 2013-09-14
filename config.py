import socket, os
from subprocess import Popen, PIPE
from Websheet import record

def execute(command, the_stdin):
    proc = Popen(command.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result = proc.communicate(input = the_stdin)
    return record(stdout = result[0].decode("UTF-8"),
                  stderr = result[1].decode("UTF-8"),
                  returncode = proc.returncode)
    

if socket.gethostname().endswith("uwaterloo.ca"):
    jail = "/home/cscircles/dev_java_jail/"
    scratch_dir = jail + "scratch/"
    javac = jail + "java/bin/javac -J-Xmx128M "
    java = "/java/bin/java -Xmx128M "
    safeexec = "/home/cscircles/dev/safeexec/safeexec"
    safeexec_args = " --chroot_dir "+ jail +" --exec_dir /scratch --env_vars '' --nproc 50 --mem 500000 --nfile 30 --clock 2 --exec "
    
    def run_javac(command, the_stdin = ""):
        os.chdir(scratch_dir)
        return execute(javac + command, the_stdin)

    def run_java(command, the_stdin = ""):
        return execute(safeexec + safeexec_args + java + command, the_stdin)  

    def save_submission(student, problem, submission, result):
        pass

    def load_submission(student, problem):
        return "false"

elif socket.gethostname().endswith("princeton.edu"):
    javac = "javac -J-Xmx128M "
    java = "/usr/bin/java -Xmx128M "

    import getpass
    server_username = getpass.getuser()
    scratch_dir = "/n/fs/htdocs/"+server_username+"/scratch/"

    def run_javac(command, the_stdin = ""):
        os.chdir(scratch_dir)
        return execute(javac + command, the_stdin)

    def run_java(command, the_stdin = ""):
        os.chdir( "/n/fs/htdocs/"+server_username+"/")
        if the_stdin != "":
            raise Exception('Cannot handle stdin in run_java yet')
        cmd = "sandbox -M -i safeexec/safeexec -i scratch /usr/bin/python -u -S"

        input = """
import os, resource, sys
from subprocess import Popen, PIPE
cmd = 'safeexec/safeexec --exec_dir {scratch} --nproc 50 --mem 4000000 --clock 3 --nfile 30 --exec {java}{command}'
proc = Popen(cmd.split(' '), stdin=PIPE, stdout=PIPE, stderr=PIPE)
result = proc.communicate(input = '')
sys.stdout.write(result[0])
sys.stderr.write(result[1])
sys.exit(proc.returncode)
""".format(command=command, scratch=scratch_dir, java=java).encode('ASCII')
            
        return execute(cmd, input)

    def connect():
        import mysql.connector
        return mysql.connector.connect(host='publicdb.cs.princeton.edu', user='cos126',
                                       password=open('/n/fs/htdocs/'+server_username+'/websheets/.dbpwd').read(), db='cos126')

    def save_submission(student, problem, submission, result_column, passed):
        import json
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "insert into ws_history (user, problem, submission, result, passed)" + 
            " VALUES (%s, %s, %s, %s, %s)", 
            (student, 
             problem, 
             # remove positional (line/ch) data from saved submission code
             json.dumps([blank["code"] for blank in json.loads(submission)]), 
             json.dumps(result_column),
             passed))
        db.commit()
        cursor.close()
        db.close()

    # returns a list of code fragments
    def load_submission(student, problem):
        import json
        db = connect()
        cursor = db.cursor()
        cursor.execute(
            "select submission from ws_history WHERE user = %s AND problem = %s ORDER BY ID DESC LIMIT 1;",
            (student, 
             problem))
        result = "false"
        for row in cursor:
            result = row[0]
        cursor.close()
        db.close()
        return json.loads(result)
