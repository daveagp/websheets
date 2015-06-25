#!/usr/bin/python3
#-*- mode: python -*-

import config
import cgi
import datetime
import math

def tablerow(data):
    return "<tr><td>"+"</td><td>".join(cgi.escape(str(x)) for x in data)+"</td></tr>"

def lateseq(student, course, courseinfo):
    assts = courseinfo["assignments"]
    result = []
    for i, asst in enumerate(assts):
        deadline = datetime.datetime.strptime(" ".join(str(x) for x in asst["due_date"]) + " 23:59", "%Y %b %d %H:%M")
        deadline += datetime.timedelta(minutes=5)

        extended = [student+"@usc.edu", asst["slug"]] in courseinfo["extensions"]

        query = """
        select max(time) from codedrop
        where user = '{0}'
        and assignment = '{1}'
        and course = '{2}'
        and operation like 'upload'
        """.format(student+'@usc.edu',
                   asst['slug'],
                   course)

        db = config.connect()
        cursor = db.cursor()
        cursor.execute(query)
        time = None
        for row in cursor:
            time = row[0]
        cursor.close()

        if time == None:
            result += [0]
        elif extended:
            result += [0]
        else:
            lateness = (time - deadline)/datetime.timedelta(days=1)
            result += [max(0, math.ceil(lateness))]
        
    return result

def print_table(course, assignments, labs, extensions, halfcredit, courseinfo):
    """
    assignments is a list of string->string dicts like this:
    {
    "title": "Lab1",
    "folder": "cs103/hw1",
    "problems": ["prob1", "prob2", "prob3"],
    "due_date": [2014, "Jan", 16]
    }
    students is a list of strings 
    
    NB: deadlines are midnight, but there is a grace period until 12:04am
    """
    import sections
    studentsec = sections.get_all_students(course, True)
    
    print("<table>")
    header = ["student", "section"] + [asst["title"] for asst in assignments]
    header += [lab["slug"] for lab in labs]
    for i in range(len(courseinfo["assignments"])):
        header += ["late"+str(i+1)]
    header += ["DaysLeft"]

    print(tablerow(header))
    db = config.connect()
    for asst in assignments:
        if "folder" in asst:
            for i in range(len(asst["problems"])):
                asst["problems"][i] = asst["folder"]+"/"+asst["problems"][i]                
    for student, section in studentsec:
        result = [student, section]
        for asst in assignments:
            query = """
            select min(time), problem from ws_history 
            where user = '{0}' 
            and passed = 1
            and problem in ({1})
            group by problem
            """.format(student+'@usc.edu', 
                       ", ".join("'"+prob+"'" for prob in asst["problems"]))
            #        print(query)
            cursor = db.cursor()
            cursor.execute(query)
            total = 0.0

            deadline = datetime.datetime.strptime(" ".join(str(x) for x in asst["due_date"]) + " 23:59", "%Y %b %d %H:%M")
            deadline += datetime.timedelta(minutes=5)

            extended = [student+"@usc.edu", asst["title"]] in extensions

            for row in cursor:
                if (row[0] < deadline or extended):
                    total += 1.0
                else:
                    total += 0.5
            result.append(total)
            #print(student, asst, total)
            cursor.close()
        import json
        for lab in labs:
            query = """
            select info from codedrop
            where user = '{0}' 
            and assignment = '{1}'
            and course = '{2}'
            and operation like 'enter-grade%'
            order by time desc
            limit 1
            """.format(student+'@usc.edu',
                       lab['slug'],
                       course)
            cursor = db.cursor()
            cursor.execute(query)
            score = "-0"
            for row in cursor:
                score = json.loads(row[0])["total"]
                if [student+'@usc.edu', lab['slug']] in halfcredit:
                    score *= 0.5

            cursor.close()
            result.append(score)
        ls = lateseq(student, course, courseinfo)

        daysleft = 2
        for i in lateseq(student, course, courseinfo):
            result.append(max(0, i-daysleft))
            daysleft = max(0, daysleft-i)
        result.append(daysleft)

        print(tablerow(result))
    db.close()
    print("</table>")

if __name__=="__main__":
    import sys, json
    sys.path.append("/home/parallel05/courseware/tools/")
    import utils, checker_config
    course = sys.argv[1]
    coursedir = checker_config.courseware_home+"courses/"+course+"/"
    courseinfo = json.loads(utils.read_file_contents(coursedir+"info.json"))
    print_table(course, courseinfo["websheet_sets"], courseinfo["labs"], courseinfo["extensions"],
                courseinfo["half_credit"], courseinfo)
