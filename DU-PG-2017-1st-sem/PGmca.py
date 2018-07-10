"""
Fetches students of a college based on roll no of one student.
"""

# roll no of a college student
CONST_college_roll_no = "1724501"


# constant POST parameters per college
CONST_VIEWSTATE = """/wEPDwUJMjIwMjE3NzMyD2QWAgIDD2QWFgIBD2QWAgIFDw8WAh4EVGV4dAUzUmVzdWx0cyAoMy1ZZWFyIFNlbWVzdGVyIEV4YW1pbmF0aW9uIE5vdi1EZWMgMjAxNyApZGQCBQ8PFgIfAAUPIChOb3YtRGVjIDIwMTcpZGQCCw8PFgIeB1Zpc2libGVoZGQCEQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQlDT0xMX05BTUUeDkRhdGFWYWx1ZUZpZWxkBQlDT0xMX0NPREUeC18hRGF0YUJvdW5kZ2QQFVMSPC0tLS0tU2VsZWN0LS0tLS0+IkFjaGFyeWEgTmFyZW5kcmEgRGV2IENvbGxlZ2UtKDAwMSkZQWRpdGkgTWFoYXZpZHlhbGF5YS0oMDAyKUNBcnlhYmhhdHRhIENvbGxlZ2UgW0Zvcm1lcmx5IFJhbSBMYWwgQW5hbmQgQ29sbGVnZSAoRXZlbmluZyldLSgwNTkpJUF0bWEgUmFtIFNhbmF0YW4gRGhhcmFtIENvbGxlZ2UtKDAwMykeQmhhZ2luaSBOaXZlZGl0YSBDb2xsZWdlLSgwMDcpFUJoYXJhdGkgQ29sbGVnZS0oMDA4KTBCaGFza2FyYWNoYXJ5YSBDb2xsZWdlIG9mIEFwcGxpZWQgU2NpZW5jZXMtKDAwOSkXQ0FNUFVTIExBVyBDRU5UUkUtKDMwOSkfQ2x1c3RlciBJbm5vdmF0aW9uIENlbnRyZS0oMzEyKSNDb2xsZWdlIE9mIFZvY2F0aW9uYWwgU3R1ZGllcy0oMDEzKRhEYXVsYXQgUmFtIENvbGxlZ2UtKDAxNCkiRGVlbiBEYXlhbCBVcGFkaHlheWEgQ29sbGVnZS0oMDE1KSZEZWxoaSBDb2xsZWdlIE9mIEFydHMgJiBDb21tZXJjZS0oMDE2KSBEZWxoaSBTY2hvb2wgb2YgSm91cm5hbGlzbS0oMzE2KXhEZXBhcnRtZW50IG9mIENvbXB1dGVyIFNjaWVuY2UgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtKDIzNCkdRGVwYXJ0bWVudCBvZiBFZHVjYXRpb24tKDI0MykdRGVwYXJ0bWVudCBvZiBHZW9ncmFwaHktKDIyOSkwRGVwYXJ0bWVudCBvZiBHZXJtYW5pYyBhbmQgUm9tYW5jZSBTdHVkaWVzLSgyMDQpM0RlcGFydG1lbnQgb2YgTGlicmFyeSBhbmQgSW5mb3JtYXRpb24gU2NpZW5jZS0oMjA2KRlEZXBhcnRtZW50IG9mIE11c2ljLSgyNDApeERlcGFydG1lbnQgb2YgU29jaWFsIFdvcmsgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0oMjMzKR5EZXNoYmFuZGh1IENvbGxlZ2UgKERheSktKDAxOSkjRHIuIEJoaW0gUmFvIEFtYmVka2FyIENvbGxlZ2UtKDAxMClIRHVyZ2FiYWkgRGVzaG11a2ggQ29sbGVnZSBvZiBTcGVjaWFsIEVkdWNhdGlvbiAoVmlzdWFsIEltcGFpcm1lbnQpLSgzMTQpHkR5YWwgU2luZ2ggQ29sbGVnZSAoRGF5KS0oMDIxKR5EeWFsIFNpbmdoIENvbGxlZ2UgKEV2ZSktKDAyMikjRmFjdWx0eSBvZiBNYW5hZ2VtZW50IFN0dWRpZXMtKDEwOSkTR2FyZ2kgQ29sbGVnZS0oMDI0KRZIYW5zIFJhaiBDb2xsZWdlLSgwMjUpE0hpbmR1IENvbGxlZ2UtKDAyNikbSS5QLkNvbGxlZ2UgRm9yIFdvbWVuLSgwMjkpPEluZGlyYSBHYW5kaGkgSW5zdGl0dXRlIG9mIFBoeS4gRWR1LiAmIFNwb3J0cyBTY2llbmNlcy0oMDI4KSFJbnN0aXR1dGUgT2YgSG9tZSBFY29ub21pY3MtKDAzMCkhSmFua2kgRGV2aSBNZW1vcmlhbCBDb2xsZWdlLSgwMzEpGkplc3VzICYgTWFyeSBDb2xsZWdlLSgwMzIpEkp1YmlsZWUgSGFsbC0oMzA2KRVLYWxpbmRpIENvbGxlZ2UtKDAzMykZS2FtbGEgTmVocnUgQ29sbGVnZS0oMDM0KRpLZXNoYXYgTWFoYXZpZHlhbGF5YS0oMDM1KRhLaXJvcmkgTWFsIENvbGxlZ2UtKDAzNikYTGFkeSBJcndpbiBDb2xsZWdlLSgwMzgpJExhZHkgU3JpIFJhbSBDb2xsZWdlIEZvciBXb21lbi0oMDM5KRhMYWtzaG1pYmFpIENvbGxlZ2UtKDA0MCkSTEFXIENFTlRSRS1JLSgzMTApE0xBVyBDRU5UUkUtSUktKDMxMSkeTWFoYXJhamEgQWdyYXNlbiBDb2xsZWdlLSgwNDEpK01haGFyc2hpIFZhbG1pa2kgQ29sbGVnZSBvZiBFZHVjYXRpb24tKDMxNSkWTWFpdHJleWkgQ29sbGVnZS0oMDQzKSNNYXRhIFN1bmRyaSBDb2xsZWdlIEZvciBXb21lbi0oMDQ0KRNNaXJhbmRhIEhvdXNlLSgwNDcpIk1vdGkgTGFsIE5laHJ1IENvbGxlZ2UgKERheSktKDA0OCkiTW90aSBMYWwgTmVocnUgQ29sbGVnZSAoRXZlKS0oMDQ5KR5QLkcuRC5BLlYuIENvbGxlZ2UgKERheSktKDA1MykeUC5HLkQuQS5WLiBDb2xsZWdlIChFdmUpLSgwNTQpFlJhamRoYW5pIENvbGxlZ2UtKDA1NSkhUmFtIExhbCBBbmFuZCBDb2xsZWdlIChEYXkpLSgwNTgpF1JhbWFudWphbiBDb2xsZWdlLSgwMjApFFJhbWphcyBDb2xsZWdlLSgwNTYpHVMuRy5ULkIuIEtoYWxzYSBDb2xsZWdlLSgwNjgpHVNhdHlhd2F0aSBDb2xsZWdlIChEYXkpLSgwNjIpHVNhdHlhd2F0aSBDb2xsZWdlIChFdmUpLSgwNjMpHVNjaG9vbCBvZiBPcGVuIExlYXJuaW5nLShTT0wpKFNoYWhlZWQgQmhhZ2F0IFNpbmdoIENvbGxlZ2UgKERheSktKDA2NCkoU2hhaGVlZCBCaGFnYXQgU2luZ2ggQ29sbGVnZSAoRXZlKS0oMDY1KTtTaGFoZWVkIFJhamd1cnUgQ29sbGVnZSBvZiBBcHBsaWVkIFNjaWVuY2VzIGZvciBXb21lbi0oMDY2KTFTaGFoZWVkIFN1a2hkZXYgQ29sbGVnZSBvZiBCdXNpbmVzcyBTdHVkaWVzLSgwNjcpFVNoaXZhamkgQ29sbGVnZS0oMDcxKR1TaHlhbSBMYWwgQ29sbGVnZSAoRGF5KS0oMDczKR1TaHlhbSBMYWwgQ29sbGVnZSAoRXZlKS0oMDc0KSVTaHlhbWEgUHJhc2FkIE11a2hlcmplZSBDb2xsZWdlLSgwNzUpIVNyaSBBdXJvYmluZG8gQ29sbGVnZSAoRGF5KS0oMDc2KSFTcmkgQXVyb2JpbmRvIENvbGxlZ2UgKEV2ZSktKDA3NykvU3JpIEd1cnUgR29iaW5kIFNpbmdoIENvbGxlZ2UgT2YgQ29tbWVyY2UtKDA3OCknU3JpIEd1cnUgTmFuYWsgRGV2IEtoYWxzYSBDb2xsZWdlLSgwNjkpIVNyaSBSYW0gQ29sbGVnZSBPZiBDb21tZXJjZS0oMDcyKR5TcmkgVmVua2F0ZXN3YXJhIENvbGxlZ2UtKDA3OSkaU3QuIFN0ZXBoZW5zIENvbGxlZ2UtKDA4MCkgU3dhbWkgU2hyYWRkaGFuYW5kIENvbGxlZ2UtKDA4MSkZVW5pdmVyc2l0eSBvZiBEZWxoaS0oMTAwKRlWaXZla2FuYW5kYSBDb2xsZWdlLSgwODQpIFpha2lyIEh1c2FpbiBDb2xsZWdlIChFdmUpLSgwODYpJlpha2lyIEh1c2FpbiBEZWxoaSBDb2xsZWdlIChEYXkpLSgwODUpFVMSPC0tLS0tU2VsZWN0LS0tLS0+AzAwMQMwMDIDMDU5AzAwMwMwMDcDMDA4AzAwOQMzMDkDMzEyAzAxMwMwMTQDMDE1AzAxNgMzMTYDMjM0AzI0MwMyMjkDMjA0AzIwNgMyNDADMjMzAzAxOQMwMTADMzE0AzAyMQMwMjIDMTA5AzAyNAMwMjUDMDI2AzAyOQMwMjgDMDMwAzAzMQMwMzIDMzA2AzAzMwMwMzQDMDM1AzAzNgMwMzgDMDM5AzA0MAMzMTADMzExAzA0MQMzMTUDMDQzAzA0NAMwNDcDMDQ4AzA0OQMwNTMDMDU0AzA1NQMwNTgDMDIwAzA1NgMwNjgDMDYyAzA2MwNTT0wDMDY0AzA2NQMwNjYDMDY3AzA3MQMwNzMDMDc0AzA3NQMwNzYDMDc3AzA3OAMwNjkDMDcyAzA3OQMwODADMDgxAzEwMAMwODQDMDg2AzA4NRQrA1NnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAhkPEGRkFgECAWQCIQ8QDxYGHwIFCUVYQU1fRkxBRx8DBQlFWEFNX0ZMQUcfBGdkEBUFEzwtLS0tLVNlbGVlY3QtLS0tLT4EQ0JDUw5VR19TRU1FU1RFUl8zWQ5VR19TRU1FU1RFUl80WQ5QR19TRU1FU1RFUl8yWRUFEzwtLS0tLVNlbGVlY3QtLS0tLT4EQ0JDUw5VR19TRU1FU1RFUl8zWQ5VR19TRU1FU1RFUl80WQ5QR19TRU1FU1RFUl8yWRQrAwVnZ2dnZxYBAgRkAikPEGRkFgECAmQCMQ8QDxYGHwIFC0NPVVJTRV9OQU1FHwMFC0NPVVJTRV9DT0RFHwRnZBAVDBI8LS0tLS1TZWxlY3QtLS0tLT4tKEMuSS5DKSAtIE0uU2MuIChNQVRIRU1BVElDUyBFRFVDQVRJT04pLSg5MTMpNChQLkcpLSBNQVNURVIgT0YgQ09NUFVURVIgQVBQTElDQVRJT04gKE0uQy5BLiktKDgyMykpKFAuRyktKE4uQy5XLkUuQikgTS5TYy4gTUFUSEVNQVRJQ1MtKDgxMykYKFAuRyktTS5TYy4gQk9UQU5ZLSg4MTgpHChQLkcpLU0uU2MuIENIRU1JU1RSWSAtKDgxNCkiKFAuRyktTS5TYy4gQ09NUFVURVIgU0NJRU5DRS0oODIyKR0oUC5HKS1NLlNjLiBNQVRIRU1BVElDUy0oODE1KRkoUC5HKS1NLlNjLiBQSFlTSUNTLSg4MTYpHChQLkcpLU0uU2MuIFNUQVRJU1RJQ1MtKDgyMCkZKFAuRyktTS5TYy4gWk9PTE9HWS0oODE5KSUoUC5HKS1NLlNjLk9QRVJBVElPTkFMIFJFU0VBUkNILSg4MjEpFQwSPC0tLS0tU2VsZWN0LS0tLS0+AzkxMwM4MjMDODEzAzgxOAM4MTQDODIyAzgxNQM4MTYDODIwAzgxOQM4MjEUKwMMZ2dnZ2dnZ2dnZ2dnFgECAmQCOQ8QDxYGHwIFBFBBUlQfAwUEUEFSVB8EZ2QQFQUSPC0tLS0tU2VsZWN0LS0tLS0+AUkCSUkDSUlJAklWFQUSPC0tLS0tU2VsZWN0LS0tLS0+AUkCSUkDSUlJAklWFCsDBWdnZ2dnFgECAWQCPw8QDxYGHwIFA1NFTR8DBQNTRU0fBGdkEBUDEjwtLS0tLVNlbGVjdC0tLS0tPgFJAklJFQMSPC0tLS0tU2VsZWN0LS0tLS0+AUkCSUkUKwMDZ2dnZGQCVw8PFgIfAWhkZGQW21NlztastCsQYpVXWAJ74oe2Rg=="""
CONST_EVENTVALIDATION = """/wEWfwKvm/XHCAKrw9qnCgKCqc+VAQLKlPHFDgLA/IyBCALl6+6qAgLopo/rCQL+gsG3BALi5fmADwLXj7neBwLoppvrCQLvppvrCQLY6+KqAgL+gsW3BAKTuKfBCQK017nqAwLJzpv3BQLMzpv3BQKRuN/ACQL8gvG3BALuppPrCQKRuKPBCQLPzuf3BQKtxdr3BgL8gv23BALopp/rCQKvxa70BgKWuKfBCQLA/ISBCALl6+aqAgLpppvrCQKTuNvACQK0173qAwLJzp/3BQLoppPrCQLXj7HeBwKvxab0BgLA/LiBCALl65qqAgLMzuf3BQL+gv23BAKTuN/ACQK017HqAwLJzpP3BQLXj7XeBwLoppfrCQKvxdr3BgKixa70BgLH/ICBCALA/LyBCAKr17nqAwL+gvG3BAKTuNPACQLi5emADwLXj6neBwLopovrCQL+gvW3BAKTuNfACQK016nqAwLXj63eBwKvxaL0BgLJzov3BQLXj6HeBwLl65aqAgL+gum3BAKuwq+LCAKTuMvACQK0163qAwLJzo/3BQLi5eGADwLA/KiBCAL+gu23BAKTuM/ACQK016HqAwLJzoP3BQLi5eWADwLXj6XeBwLopoPrCQLl64qqAgLopofrCQKvxYr0BgLA/OyBCAKsxar0BgKTuIPBCQLJzsf3BQK01+XqAwKjosWyCQLs3ZO5CgLR2dWyDALpvqyACALYz62KDAKAjfS0DwKAxvzOBwL25u3uBwL/5u3uBwKEw+/uBwLM9PumDwLLnPhJAoTjrsIDAo7DtdIEAqbz5rkMAv2OmvwHAuXzrHECqoz6+gMC55nOiAkC5pnyiAkC5pnOiAkCv5e24QoC+6Cs/gQCjfPtlQ8C3M+y1Q4CsdaQyAgC192pywsCkL6U1AQCqOSPvgUCgYSW4wICzvvA6AEC5uu8jQ4C5uvQkw4C1enQ5gUC5uvEkw4C3L7XvQ0C9K6r2AIC9K7HxgICtPew8AwCxISEgAsCpZ/ziwJV+y6cNPsG+dkUfCxxcet8+GG4Sw=="""



import requests
from bs4 import BeautifulSoup

r= requests.get('http://duexam2.du.ac.in/RSLT_ND2017/Students/List_Of_Students.aspx?StdType=REG&ExamFlag=PG_SEMESTER_2Y&CourseCode=823&CourseName=(P.G)-%20MASTER%20OF%20COMPUTER%20APPLICATION%20(M.C.A.)&Part=I&Sem=I')
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
#print(data)

#roll_no_pattern = CONST_college_roll_no[:-2] + '...'

#import re
#dduc = []
#for student in data:
#    if re.match(roll_no_pattern,student[1]):
#        dduc.append(student)

dduc = data
#print(*dduc,sep="\n")


# for these students make html
# works on same college level only



#dduc = [['1', '17015570016', 'NAVEEN KUMAR ROHILLA', 'MR. NARESH KUMAR'], ['2','17015570022','SACHIN YADAV','dd'] ]

college_sgpa_list = []

#for i in range(45):
#    dduc.pop()

for VAR_stud in dduc:
    VAR_rollno = VAR_stud[1]
    VAR_sname = VAR_stud[2]


    payload = {
        'ddlcollege' : '234',
        'ddlexamtype' : 'Semester',
        'ddlexamflag' : 'PG_SEMESTER_2Y',
        'ddlstream' : 'SC',
        'ddlcourse' : '823',
        'ddlpart' : 'I',
        'ddlsem': 'I',
        'txtrollno' : VAR_rollno,
        'txtname' : VAR_sname,
        'btnsearch': 'Print Score Cart/Transcript',
        '__EVENTTARGET' : '',
        '__EVENTARGUMENT' : '',
        '__LASTFOCUS':'',
        '__VIEWSTATE': CONST_VIEWSTATE,
        '__EVENTVALIDATION': CONST_EVENTVALIDATION
        }

    r = requests.post("http://duexam2.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx", data=payload)

    #print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')

    for img in soup.find_all('img'):
        img.decompose()

    #soup.find('span', attrs={'id':'lblstatement'}).decompose()
    #soup.find('span', attrs={'id':'lbl_sub_head3'}).decompose()
    #soup.find('span', attrs={'id':'lbldisclaimer'}).decompose()

    sgpa_table = soup.find("table", {"id": "gvrslt"})
    if(sgpa_table == None ):
        continue
    sgpa_row = sgpa_table.find_all('td')
    
    temp = []
    for cols in sgpa_row:
        cols = [ele for ele in cols]
        temp.append([ele for ele in cols if ele!=[]]) # Get rid of empty values

    #print([VAR_rollno, VAR_sname, int(temp[1][0]) ])
    college_sgpa_list.append([VAR_rollno, VAR_sname, float(temp[1][0]) ])

    
    '''
    # writing result to html file
    
    VAR_filename = "dduc_marks/" + VAR_rollno + '__' + VAR_sname + '__' + '.html'
    with open(VAR_filename, "w") as file:
        file.write(str(soup))
    '''

college_sgpa_list.sort(key = lambda x : x[2])
#print(college_sgpa_list)

#import sys
#sys.stdout = open('oMCA_first_sem.txt', 'w')
print('{3:5} {0:15} {1:25} {2:5} {4:10}'.format("Roll No.","Name","Marks","S.No","Percentage"))
for i,marks in enumerate(college_sgpa_list):
    print('{3:5} {0:15} {1:25} {2:5} {4:10}'.format(marks[0],marks[1],marks[2], i+1, float(marks[2]/5)))

#print('{0:15} {1:25} {2:5}'.format("Roll No.","Name","Marks"))
#for marks in college_sgpa_list:
#    print('{0:15} {1:25} {2:5}'.format(marks[0],marks[1],marks[2]))
