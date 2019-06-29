# dependencies
import requests
from bs4 import BeautifulSoup
import re
import sys
import os

savePath = "html"
if not os.path.isdir(savePath):
    os.mkdir(savePath)

# link for 6th sem 2019
GradeCard = "http://duresult.in/Students/OLD_Sys1_GradeCardReport_Sem_New.aspx"

# additional params for ref
# ?ExamType=Semester&CollegeCode=015&CourseCode=570&Part=III&Sem=V&Rollno=16015570001

# store marks list for all DU
college_sgpa_list = []

# list codes for all CS colleges
# list codes for all CS colleges
all_colleges = [
    "16001570001",
    "16003570001",
    "16009570001",
    "16013570001",
    "16015570001",
    "16020570001",
    "16021570001",
    "16025570001",  
    "16029570001",
    "16033570001",
    "16035570001",
    "16044570001",
    "16053570001",
    "16058570001",
    "16059570001",
    "16066570001",
    "16067570001",
    "16068570001",
    "16075570001",
    "16078570001"
    ]

# override for one college check
# all_colleges = [
#     "16015570001"
# ]

for col in all_colleges:
    # dduc = [['16015570001']]
    dduc = []
    constantCollegePart = col[:-2]
    for i in range(1,10):
        dduc.append([constantCollegePart + '0' + str(i)])
    for i in range(10,70):
        dduc.append([constantCollegePart + str(i)])
    
    # testing generation of rollnos
    # print(dduc)
    # break
    VAR_collegeCode = col[2:5]   
    for VAR_stud in dduc:
        VAR_rollno = VAR_stud[0]
        # print(VAR_rollno)
        payload = {
            'ExamType':'Semester',
            'CollegeCode': VAR_collegeCode,
            'CourseCode':'570',
            'Part':'III',
            'Sem':'VI',
            'Rollno':VAR_rollno
            }
        
        # infinite cookie life
        cookies = {'ASP.NET_SessionId': 'ynzvyu55xowqe445gu2izs45'}

        soup = None
        count = 0
        while(soup == None):
            r = requests.get(GradeCard, params=payload, cookies=cookies)
            # print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            if(soup==None):
                continue
            # print(soup.title.string)
            if(soup.title.string == "Runtime Error"):
                if count == 1:
                    break
                else:
                    count = 1
                soup = None
                continue
        
        if count == 1:
            continue
        # for img in soup.find_all('img'):
        #     img.decompose()

        #t = soup.find('span', attrs={'id':'lblstatement'}).decompose()
        #t = soup.find('span', attrs={'id':'lbl_sub_head3'}).decompose()
        #t = soup.find('span', attrs={'id':'lbldisclaimer'}).decompose()
        
        # // todo 
        # sgpa_table = soup.find("span", {"id": "lbl_gr_cgpa"})
        # print(soup)
        total = soup.find("span", id="lbldiv").text
        
        # sgpa_table = soup.find("table", {"id": "gvrslt"})

        if(total == None ):
            continue
        try:
            VAR_college = soup.find("span", id="lblcollege").text[6:]
            VAR_sname = soup.find("span", id="lblname").text
            obtained_marks = int(total.split(':')[2].split(' ')[1].split(';')[0])
            total_marks = 3450
            FINAL_CGPA = (obtained_marks*10)/total_marks
            # print([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])
        except IndexError:
            continue
        college_sgpa_list.append([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])

        # print(college_sgpa_list)
        # writing result to html file
        savePath = "html/"+VAR_college.replace(' ', '_')
        if not os.path.isdir(savePath):
            os.mkdir(savePath)
        VAR_filename = savePath + '/' + VAR_rollno + '__' + VAR_sname + '__' + '.html'
        with open(VAR_filename, "w") as file:
            file.write(str(soup))
        

college_sgpa_list.sort(key = lambda x : x[2], reverse=True)
# print(college_sgpa_list)

# print to file
with open('DU-2016-2019-Batch-Result.txt','w') as f:
    print('{3:<5} {0:15} {1:25} {2:10} {4:<40}'.format("Roll No.","Name","SGPA","S.No", "College"), file=f)
    for i,marks in enumerate(college_sgpa_list):
        print('{3:<5} {0:15} {1:25} {2:<10.4f} {4:<40}'.format(marks[0],marks[1],marks[2], i+1, marks[3]), file=f)


# print(soup.prettify())

# with open("test.html", "w") as file:
#     file.write(str(soup))
