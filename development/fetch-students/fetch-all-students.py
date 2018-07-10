"""
Fetches all students of DU of one batch, as specified by URL
"""

import requests
from bs4 import BeautifulSoup

# URL is ever changing, update with actual URL before use.

URL = 'http://duexam2.du.ac.in/RSLT_ND2017/Students/List_Of_Students.aspx?'
    'StdType=REG'
    '&ExamFlag=CBCS'
    '&CourseCode=570'
    '&CourseName=(CBCS)%20B.SC.(HONS.)%20COMPUTER%20SCIENCE&Part=I'
    '&Sem=I'

r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')
students_table = soup.find("table", {"rules": "all"})
data = []
all_students = students_table.find_all('tr')

for student in all_students:
    cols = student.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])


data[0] = ['sno','srollno','sname','sfathername']
print(*data,sep="\n")
