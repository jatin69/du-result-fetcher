import requests
from bs4 import BeautifulSoup
import re
import sys

# for 6th sem - 2018
GradeCard = "http://duresult.in/Students/OLD_Sys1_GradeCardReport_Sem_New.aspx"
"""
?ExamType=Semester&CollegeCode=015&CourseCode=570&Part=III&Sem=V&Rollno=16015570001
"""
# store marks list for all DU
college_sgpa_list = []

# list codes for all CS colleges
all_colleges = [
    "15001570001",
    "15003570001",
    "15009570001",
    "15013570001",
    "15015570001",
    "15020570001",
    "15021570001",
    "15025570001",
    "15029570001",
    "15033570001",
    "15035570001",
    "15044570001",
    "15053570001",
    "15058570001",
    "15059570001",
    "15066570001",
    "15067570001",
    "15068570001",
    "15075570001",
    "15078570001"
    ]

all_colleges = [
    "16015570001"
]

for col in all_colleges:
    dduc = [['16015570001']]
    # dduc = [
    #     ['37', '15001570041', 'SONU  KUMAR', 'MR. PREM KUMAR'],
    #     ['39', '15001570043', 'VARAD  SRIVASTAVA', 'MR. RATNESH MOHAN SRIVASTAVA']
    # ]
   
    for VAR_stud in dduc:
        VAR_rollno = VAR_stud[0]
        print(VAR_rollno)
        VAR_sname = "s"
        
        payload = {
            'ExamType':'Semester',
            'CollegeCode':'015',
            'CourseCode':'570',
            'Part':'III',
            'Sem':'V',
            'Rollno':'16015570001'
            }
        # infinite cookie life
        cookies = {'ASP.NET_SessionId': 'q52d2qrq20w2buv1dkiked45'}

        soup = None
        while(soup == None):
            r = requests.get(GradeCard, params=payload, cookies=cookies)
            print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            if(soup==None):
                continue
            print(soup.title.string)
            if(soup.title.string == "Runtime Error"):
                soup = None
                continue
        
        # for img in soup.find_all('img'):
        #     img.decompose()

        #t = soup.find('span', attrs={'id':'lblstatement'}).decompose()
        #t = soup.find('span', attrs={'id':'lbl_sub_head3'}).decompose()
        #t = soup.find('span', attrs={'id':'lbldisclaimer'}).decompose()
        
        # // todo 
        # sgpa_table = soup.find("span", {"id": "lbl_gr_cgpa"})
        print(soup)
        sgpa_table = soup.find("table", {"id": "gvrslt"})
        if(sgpa_table == None ):
            continue
        try:
            sgpa_row = [x.strip() for x in sgpa_table.text.replace(',',':').split(':')]
            FINAL_CGPA = float(sgpa_row[1])
            # print([VAR_rollno, VAR_sname, FINAL_CGPA])
        except IndexError:
            continue
        college_sgpa_list.append([VAR_rollno, VAR_sname, FINAL_CGPA])

        print(college_sgpa_list)
        
        # writing result to html file
        
        VAR_filename = "html/" + VAR_rollno + '__' + VAR_sname + '__' + '.html'
        with open(VAR_filename, "w") as file:
            file.write(str(soup))
        

college_sgpa_list.sort(key = lambda x : x[2], reverse=True)
#print(college_sgpa_list)

# print to file
with open('DU-2016-2019-Batch-Result.txt','w') as f:
    print('{3:<5} {0:15} {1:25} {2:5}'.format("Roll No.","Name","SGPA","S.No"), file=f)
    for i,marks in enumerate(college_sgpa_list):
        print('{3:<5} {0:15} {1:25} {2:<5}'.format(marks[0],marks[1],marks[2], i+1), file=f)


# print(soup.prettify())

# with open("test.html", "w") as file:
#     file.write(str(soup))
