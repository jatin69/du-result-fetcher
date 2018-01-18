import requests
from bs4 import BeautifulSoup

r = requests.get('http://duexam2.du.ac.in/RSLT_ND2017/Students/List_Of_Students.aspx?'
                 'StdType=REG'
                 '&ExamFlag=CBCS'
                 '&CourseCode=570'
                 '&CourseName=(CBCS)%20B.SC.(HONS.)%20COMPUTER%20SCIENCE&Part=I'
                 '&Sem=I')

soup = BeautifulSoup(r.text, 'html.parser')
students_table = soup.find("table", {"rules": "all"})
data = []
all_students = students_table.find_all('tr')

for student in all_students:
    cols = student.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values


data[0] = ['sno','srollno','sname','sfathername']
print(*data,sep="\n")
