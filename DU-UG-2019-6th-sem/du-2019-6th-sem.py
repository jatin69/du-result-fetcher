import requests
from bs4 import BeautifulSoup
import re
import json

with open("constants.json", 'r') as f:
    constants = json.load(f)
    # print(constants)

def fetchStudentResults():
    # myformdata = {
    #     '__EVENTTARGET': constants["__EVENTTARGET"],
    #     '__EVENTARGUMENT': constants["__EVENTARGUMENT"],
    #     '__VIEWSTATE': constants["__VIEWSTATE"],
    #     '__VIEWSTATEGENERATOR': constants["__VIEWSTATEGENERATOR"],
    #     '__EVENTVALIDATION': constants["__EVENTVALIDATION"],
    #     'ddlcollege': constants["ddlcollege"],
    #     'txtrollno': constants["txtrollno"],
    #     'txtcaptcha' : constants["txtcaptcha"],
    #     'btnsearch': constants["txtcaptcha"]
    # }
    # myheaders = {
    #         "Host": "duresult.in",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #         "Accept-Language": "en-US,en;q=0.5",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Referer": "http://duresult.in/students/Combine_GradeCard.aspx",
    #         "Content-Type": "application/x-www-form-urlencoded",
    #         "Content-Length": "8593",
    #         "Connection": "keep-alive",
    #         "Cookie": "ASP.NET_SessionId=eclaama23vlklpqq5sby5l45",
    #         "Upgrade-Insecure-Requests": "1",
    #         "Pragma": "no-cache",
    #         "Cache-Control": "no-cache"
    #     }
    # mycookies = {
    #     "ASP.NET_SessionId":"eclaama23vlklpqq5sby5l45"
    # }

    r = requests.post(constants["gradeCardURL"], data=myformdata)
    # , headers=myheaders, cookies=mycookies
    
    print(r.text)


def main(*args):
    fetchStudentResults()

if __name__ == "__main__":
    import sys
    main(*sys.argv)





# # load json and start working

# # store marks list for all DU
# college_sgpa_list = []

# # list codes for all CS colleges


# # all_colleges = [
# #     "15025570001"
# # ]

# for col in all_colleges:
#     CONST_college_roll_no = col
#     VAR_college_Code = CONST_college_roll_no[2:5]

#     r= requests.get(LIST_OF_STUDENTS)
#     soup = None
#     while soup == None:
#         soup = BeautifulSoup(r.text, 'html.parser')
    
#     students_table = soup.find("table", {"rules": "all"})
#     data = []
#     all_students = students_table.find_all('tr')

#     for student in all_students:
#         cols = student.find_all('td')
#         cols = [ele.text.strip() for ele in cols]
#         data.append([ele for ele in cols if ele]) # Get rid of empty values


#     data[0] = ['sno','srollno','sname','sfathername']
#     data.pop(0)

#     roll_no_pattern = CONST_college_roll_no[:-3] + '...'

#     dduc = []
#     for student in data:
#         if re.match(roll_no_pattern,student[1]):
#             dduc.append(student)
        
#     # print(*dduc,sep="\n")

#     # dduc = [
#     #     ['37', '15001570041', 'SONU  KUMAR', 'MR. PREM KUMAR'],
#     #     ['39', '15001570043', 'VARAD  SRIVASTAVA', 'MR. RATNESH MOHAN SRIVASTAVA']
#     # ]
   
#     for VAR_stud in dduc:
#         VAR_rollno = VAR_stud[1]
#         VAR_sname = VAR_stud[2]
        
#         payload = {
#             'ddlcollege' : VAR_college_Code,
#             'ddlexamtype' : 'Semester',
#             'ddlexamflag' : 'CBCS',
#             'ddlstream' : 'SC',
#             'ddlcourse' : '570',
#             'ddlpart' : 'III',
#             'ddlsem': 'VI',
#             'txtrollno' : VAR_rollno,
#             'txtname' : VAR_sname,
#             'btnsearch': 'Print Score Cart/Transcript',
#             '__EVENTTARGET' : '',
#             '__EVENTARGUMENT' : '',
#             '__LASTFOCUS':'',
#             '__VIEWSTATE': CONST_VIEWSTATE,
#             '__EVENTVALIDATION': CONST_EVENTVALIDATION,
#             '__VIEWSTATEGENERATOR' : CONST_VIEWSTATE_GENERATOR

#             }

#         r = requests.post(GradeCard, data=payload)
#         # print(r.text)
#         soup = BeautifulSoup(r.text, 'html.parser')
            

#         soup = None
#         while(soup == None):
#             r = requests.post(GradeCard, data=payload)
#             # print(r.text)
#             soup = BeautifulSoup(r.text, 'html.parser')
#             if(soup==None):
#                 continue
#             # print(soup.title.string)
#             if(soup.title.string == "Runtime Error"):
#                 soup = None
#                 continue
        
#         for img in soup.find_all('img'):
#             img.decompose()

#         #t = soup.find('span', attrs={'id':'lblstatement'}).decompose()
#         #t = soup.find('span', attrs={'id':'lbl_sub_head3'}).decompose()
#         #t = soup.find('span', attrs={'id':'lbldisclaimer'}).decompose()
        
#         sgpa_table = soup.find("span", {"id": "lbl_gr_cgpa"})
#         if(sgpa_table == None ):
#             continue
#         try:
#             sgpa_row = [x.strip() for x in sgpa_table.text.replace(',',':').split(':')]
#             FINAL_CGPA = float(sgpa_row[1])
#             # print([VAR_rollno, VAR_sname, FINAL_CGPA])
#         except IndexError:
#             continue
#         college_sgpa_list.append([VAR_rollno, VAR_sname, FINAL_CGPA])
        
#         '''
#         # writing result to html file
        
#         VAR_filename = "dduc_marks/" + VAR_rollno + '__' + VAR_sname + '__' + '.html'
#         with open(VAR_filename, "w") as file:
#             file.write(str(soup))
#         '''

# college_sgpa_list.sort(key = lambda x : x[2], reverse=True)
# #print(college_sgpa_list)

# # print to file
# with open('DU-2015-2018-Batch-Result.txt','w') as f:
#     print('{3:<5} {0:15} {1:25} {2:5}'.format("Roll No.","Name","SGPA","S.No"), file=f)
#     for i,marks in enumerate(college_sgpa_list):
#         print('{3:<5} {0:15} {1:25} {2:<5}'.format(marks[0],marks[1],marks[2], i+1), file=f)


# # print(soup.prettify())

# # with open("test.html", "w") as file:
# #     file.write(str(soup))
