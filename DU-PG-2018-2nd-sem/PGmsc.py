"""
DU MSc 2018 2nd sem
"""

import sys
import requests
from bs4 import BeautifulSoup

CONST_VIEWSTATE = """/wEPDwUKMTU1ODI4OTc2Mw8WAh4JSXBBZGRyZXNzBQwxMDMuNzguMTQ4LjgWAgIDD2QWCgIBD2QWAgIFDw8WAh4EVGV4dAU0UmVzdWx0cyAoMy1ZZWFyIFNlbWVzdGVyIEV4YW1pbmF0aW9uIE1heS1KdW5lIDIwMTggKWRkAgcPDxYCHwEFECAoTWF5LUp1bmUgMjAxOClkZAIVDxAPFgYeDURhdGFUZXh0RmllbGQFCUNPTExfTkFNRR4ORGF0YVZhbHVlRmllbGQFCUNPTExfQ09ERR4LXyFEYXRhQm91bmRnZBAVYRI8LS0tLS1TZWxlY3QtLS0tLT4cQWNoYXJ5YSBOYXJlbmRyYSBEZXYgQ29sbGVnZRNBZGl0aSBNYWhhdmlkeWFsYXlhPUFyeWFiaGF0dGEgQ29sbGVnZSBbRm9ybWVybHkgUmFtIExhbCBBbmFuZCBDb2xsZWdlIChFdmVuaW5nKV0fQXRtYSBSYW0gU2FuYXRhbiBEaGFyYW0gQ29sbGVnZRhCaGFnaW5pIE5pdmVkaXRhIENvbGxlZ2UPQmhhcmF0aSBDb2xsZWdlKkJoYXNrYXJhY2hhcnlhIENvbGxlZ2Ugb2YgQXBwbGllZCBTY2llbmNlcxFDQU1QVVMgTEFXIENFTlRSRRdDYW1wdXMgb2YgT3BlbiBMZWFybmluZyJDbHVzdGVyIElubm92YXRpb24gQ2VudHJlIChDLkkuQy4pHUNvbGxlZ2UgT2YgVm9jYXRpb25hbCBTdHVkaWVzEkRhdWxhdCBSYW0gQ29sbGVnZRxEZWVuIERheWFsIFVwYWRoeWF5YSBDb2xsZWdlIERlbGhpIENvbGxlZ2UgT2YgQXJ0cyAmIENvbW1lcmNlGkRlbGhpIFNjaG9vbCBvZiBKb3VybmFsaXNtckRlcGFydG1lbnQgb2YgQm90YW55ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJEZXBhcnRtZW50IG9mIENoZW1pc3RyeSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAWRGVwYXJ0bWVudCBvZiBDb21tZXJjZXJEZXBhcnRtZW50IG9mIENvbXB1dGVyIFNjaWVuY2UgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAXRGVwYXJ0bWVudCBvZiBFZHVjYXRpb24VRGVwYXJ0bWVudCBvZiBFbmdsaXNoF0RlcGFydG1lbnQgb2YgR2VvZ3JhcGh5KkRlcGFydG1lbnQgb2YgR2VybWFuaWMgYW5kIFJvbWFuY2UgU3R1ZGllcxNEZXBhcnRtZW50IG9mIEhpbmRpFURlcGFydG1lbnQgb2YgSGlzdG9yeS1EZXBhcnRtZW50IG9mIExpYnJhcnkgYW5kIEluZm9ybWF0aW9uIFNjaWVuY2VyRGVwYXJ0bWVudCBvZiBNYXRoZW1hdGljcyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgE0RlcGFydG1lbnQgb2YgTXVzaWNyRGVwYXJ0bWVudCBvZiBQaHlzaWNzICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgH0RlcGFydG1lbnQgb2YgUG9saXRpY2FsIFNjaWVuY2UWRGVwYXJ0bWVudCBvZiBTYW5za3JpdHJEZXBhcnRtZW50IG9mIFNvY2lhbCBXb3JrICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICByRGVwYXJ0bWVudCBvZiBTdGF0aXN0aWNzICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgckRlcGFydG1lbnQgb2YgWm9vbG9neSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIBhEZXNoYmFuZGh1IENvbGxlZ2UgKERheSkdRHIuIEJoaW0gUmFvIEFtYmVka2FyIENvbGxlZ2UuRHVyZ2FiYWkgRGVzaG11a2ggQ29sbGVnZSBvZiBTcGVjaWFsIEVkdWNhdGlvbhhEeWFsIFNpbmdoIENvbGxlZ2UgKERheSkYRHlhbCBTaW5naCBDb2xsZWdlIChFdmUpHUZhY3VsdHkgb2YgTWFuYWdlbWVudCBTdHVkaWVzDUdhcmdpIENvbGxlZ2UQSGFucyBSYWogQ29sbGVnZQ1IaW5kdSBDb2xsZWdlFUkuUC5Db2xsZWdlIEZvciBXb21lbjZJbmRpcmEgR2FuZGhpIEluc3RpdHV0ZSBvZiBQaHkuIEVkdS4gJiBTcG9ydHMgU2NpZW5jZXMbSW5zdGl0dXRlIE9mIEhvbWUgRWNvbm9taWNzG0phbmtpIERldmkgTWVtb3JpYWwgQ29sbGVnZRRKZXN1cyAmIE1hcnkgQ29sbGVnZQxKdWJpbGVlIEhhbGwPS2FsaW5kaSBDb2xsZWdlE0thbWxhIE5laHJ1IENvbGxlZ2UUS2VzaGF2IE1haGF2aWR5YWxheWESS2lyb3JpIE1hbCBDb2xsZWdlEkxhZHkgSXJ3aW4gQ29sbGVnZR5MYWR5IFNyaSBSYW0gQ29sbGVnZSBGb3IgV29tZW4STGFrc2htaWJhaSBDb2xsZWdlDExBVyBDRU5UUkUtSQ1MQVcgQ0VOVFJFLUlJGE1haGFyYWphIEFncmFzZW4gQ29sbGVnZSVNYWhhcnNoaSBWYWxtaWtpIENvbGxlZ2Ugb2YgRWR1Y2F0aW9uEE1haXRyZXlpIENvbGxlZ2UdTWF0YSBTdW5kcmkgQ29sbGVnZSBGb3IgV29tZW4NTWlyYW5kYSBIb3VzZRxNb3RpIExhbCBOZWhydSBDb2xsZWdlIChEYXkpHE1vdGkgTGFsIE5laHJ1IENvbGxlZ2UgKEV2ZSkYUC5HLkQuQS5WLiBDb2xsZWdlIChEYXkpGFAuRy5ELkEuVi4gQ29sbGVnZSAoRXZlKRBSYWpkaGFuaSBDb2xsZWdlG1JhbSBMYWwgQW5hbmQgQ29sbGVnZSAoRGF5KRFSYW1hbnVqYW4gQ29sbGVnZQ5SYW1qYXMgQ29sbGVnZRdTLkcuVC5CLiBLaGFsc2EgQ29sbGVnZRdTYXR5YXdhdGkgQ29sbGVnZSAoRGF5KRdTYXR5YXdhdGkgQ29sbGVnZSAoRXZlKRdTY2hvb2wgb2YgT3BlbiBMZWFybmluZyJTaGFoZWVkIEJoYWdhdCBTaW5naCBDb2xsZWdlIChEYXkpIlNoYWhlZWQgQmhhZ2F0IFNpbmdoIENvbGxlZ2UgKEV2ZSk1U2hhaGVlZCBSYWpndXJ1IENvbGxlZ2Ugb2YgQXBwbGllZCBTY2llbmNlcyBmb3IgV29tZW4rU2hhaGVlZCBTdWtoZGV2IENvbGxlZ2Ugb2YgQnVzaW5lc3MgU3R1ZGllcw9TaGl2YWppIENvbGxlZ2UXU2h5YW0gTGFsIENvbGxlZ2UgKERheSkXU2h5YW0gTGFsIENvbGxlZ2UgKEV2ZSkfU2h5YW1hIFByYXNhZCBNdWtoZXJqZWUgQ29sbGVnZRZTT0wgU3R1ZHkgQ2VudGVyIFNvdXRoG1NyaSBBdXJvYmluZG8gQ29sbGVnZSAoRGF5KRtTcmkgQXVyb2JpbmRvIENvbGxlZ2UgKEV2ZSkpU3JpIEd1cnUgR29iaW5kIFNpbmdoIENvbGxlZ2UgT2YgQ29tbWVyY2UhU3JpIEd1cnUgTmFuYWsgRGV2IEtoYWxzYSBDb2xsZWdlG1NyaSBSYW0gQ29sbGVnZSBPZiBDb21tZXJjZRhTcmkgVmVua2F0ZXN3YXJhIENvbGxlZ2UUU3QuIFN0ZXBoZW5zIENvbGxlZ2UaU3dhbWkgU2hyYWRkaGFuYW5kIENvbGxlZ2UTVW5pdmVyc2l0eSBvZiBEZWxoaRNWaXZla2FuYW5kYSBDb2xsZWdlGlpha2lyIEh1c2FpbiBDb2xsZWdlIChFdmUpIFpha2lyIEh1c2FpbiBEZWxoaSBDb2xsZWdlIChEYXkpFWESPC0tLS0tU2VsZWN0LS0tLS0+AzAwMQMwMDIDMDU5AzAwMwMwMDcDMDA4AzAwOQMzMDkDQ09MAzMxMgMwMTMDMDE0AzAxNQMwMTYDMzE2AzIxNgMyMTcDMjQxAzIzNAMyNDMDMjAzAzIyOQMyMDQDMjA1AzIzMQMyMDYDMjM1AzI0MAMyMjIDMjMyAzIxMwMyMzMDMjM3AzIyMwMwMTkDMDEwAzMxNAMwMjEDMDIyAzEwOQMwMjQDMDI1AzAyNgMwMjkDMDI4AzAzMAMwMzEDMDMyAzMwNgMwMzMDMDM0AzAzNQMwMzYDMDM4AzAzOQMwNDADMzEwAzMxMQMwNDEDMzE1AzA0MwMwNDQDMDQ3AzA0OAMwNDkDMDUzAzA1NAMwNTUDMDU4AzAyMAMwNTYDMDY4AzA2MgMwNjMDU09MAzA2NAMwNjUDMDY2AzA2NwMwNzEDMDczAzA3NAMwNzUEU09MUwMwNzYDMDc3AzA3OAMwNjkDMDcyAzA3OQMwODADMDgxAzEwMAMwODQDMDg2AzA4NRQrA2FnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZGQCHw8PFgIeB1Zpc2libGVoZGQCJQ8PFgIfBWhkZGR9XUVyAZvwgdkIiNgitJxSMepGGQ=="""
CONST_EVENTVALIDATION = """/wEWZQLN36/3BAKrw9qnCgLKlPHFDgLA/IyBCALl6+6qAgLopo/rCQL+gsG3BALi5fmADwLXj7neBwLoppvrCQLvppvrCQKewq+LCALY6+KqAgL+gsW3BAKTuKfBCQK017nqAwLJzpv3BQLMzpv3BQLPzpv3BQLg5f2ADwLG/LyBCAKRuN/ACQL8gvG3BAL8gsG3BALuppPrCQKRuKPBCQKq14XqAwLG/LiBCALPzuf3BQKq17HqAwKtxdr3BgLb6+aqAgLb65qqAgL8gsW3BAL8gv23BALg5fWADwL8gvm3BALopp/rCQKvxa70BgKWuKfBCQLA/ISBCALl6+aqAgLpppvrCQKTuNvACQK0173qAwLJzp/3BQLoppPrCQLXj7HeBwKvxab0BgLA/LiBCALl65qqAgLMzuf3BQL+gv23BAKTuN/ACQK017HqAwLJzpP3BQLXj7XeBwLoppfrCQKvxdr3BgKixa70BgLH/ICBCALA/LyBCAKr17nqAwL+gvG3BAKTuNPACQLi5emADwLXj6neBwLopovrCQL+gvW3BAKTuNfACQK016nqAwLXj63eBwKvxaL0BgLJzov3BQLXj6HeBwLl65aqAgL+gum3BAKuwq+LCAKTuMvACQK0163qAwLJzo/3BQLi5eGADwLA/KiBCAL+gu23BAKTuM/ACQK016HqAwKuwqv+CQLJzoP3BQLi5eWADwLXj6XeBwLopoPrCQLl64qqAgLopofrCQKvxYr0BgLA/OyBCAKsxar0BgKTuIPBCQLJzsf3BQK01+XqAwK097DwDAKln/OLAsH7fo1IVVKIl4i/u9OVN2QRC4K4"""

college_sgpa_list = []

dduc= []
# s = 1
# e = 48
# for i in range(1,2):
#     if(i<10):
#         i = '0' + str(i)
#     el = '17245' + str(i)
#     dduc.append(el)

# print(dduc)

# student list URL
r= requests.get('http://duexam.du.ac.in/RSLT_MJ2018/Students/List_Of_Students.aspx?StdType=REG&ExamFlag=PG_SEMESTER_2Y&CourseCode=822&CourseName=(P.G)-%20MASTER%20OF%20COMPUTER%20APPLICATION%20(M.C.A.)&Part=I&Sem=II')
soup = BeautifulSoup(r.text, 'html.parser')
students_table = soup.find("table", {"rules": "all"})
data = []
all_students = students_table.find_all('tr')

for student in all_students:
    cols = student.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values


data[0] = ['sno','srollno','sname','sfathername']
data.pop(0)

dduc = data
#print(*dduc,sep="\n")

for VAR_stud in dduc:
    VAR_rollno = VAR_stud[1]
    
    payload = {
        'ddlcollege' : '234',
        'txtrollno' : VAR_rollno,
        'btnsearch': 'Print+Score+Card',
        '__EVENTTARGET' : '',
        '__EVENTARGUMENT' : '',
        '__LASTFOCUS':'',
        '__VIEWSTATE': CONST_VIEWSTATE,
        '__EVENTVALIDATION': CONST_EVENTVALIDATION
        }

    soup = None
    while(soup == None):
        # print('trying')
        r = requests.post("http://duexam.du.ac.in/RSLT_MJ2018/Students/Combine_GradeCard.aspx", data=payload)
        # print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        if(soup==None):
            continue
        # print(soup.title.string)
        if(soup.title.string == "Runtime Error"):
            soup = None
            continue
    
    # writing result to html file
    
    for img in soup.find_all('img'):
        img.decompose()

    VAR_filename = "htmlsavemsc/" + VAR_rollno + '.html'
    with open(VAR_filename, "w") as file:
        file.write(str(soup))

    sgpa_table = soup.find("table", {"id": "gvrslt"})
    # print(sgpa_table)
    if(sgpa_table == None ):
        continue
    
    xrows = sgpa_table.findAll('tr')
    sgpa_row = xrows[2].find_all('td')
    
    m = sgpa_row[1].text

    # print([VAR_rollno, int(m) ])
    name = VAR_stud[2]
    college_sgpa_list.append([VAR_rollno, name, int(m) ])
    
college_sgpa_list.sort(key = lambda x : x[2], reverse=True)
#print(college_sgpa_list)

with open('DU-PG-MSc-2nd-sem-Result.txt','w') as f:
    print('{0:<5} {1:10} {2:21} {3:5} {4:7}'.format("S.No","Roll No.","Name","Marks","Percentage"), file=f)
    for i,marks in enumerate(college_sgpa_list):
        print('{0:<5} {1:10} {2:21} {3:5} {4:7}'.format(i+1, marks[0], marks[1], marks[2],  float(marks[2]/5)),file=f)
