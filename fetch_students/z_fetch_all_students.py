import requests
from bs4 import BeautifulSoup

r = requests.get('http://duexam2.du.ac.in/RSLT_ND2017/Students/List_Of_Students.aspx?'
                 'StdType=REG'
                 '&ExamFlag=CBCS'
                 '&CourseCode=570'
                 '&CourseName=(CBCS)%20B.SC.(HONS.)%20COMPUTER%20SCIENCE&Part=I'
                 '&Sem=I')

# print(r)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

# get the students table from all of html
students_table = soup.find("table", {"rules": "all"})

data = []

# get all students => contents
all_students = students_table.find_all('tr')

for student in all_students:
    cols = student.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])  # Get rid of empty values

data[0] = ['sno', 'srollno', 'sname', 'sfathername']
print(*data, sep="\n")

data = []
table = soup.find('table', attrs={'class': 'lineItemsTable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])  # Get rid of empty values

# Final data format
student_data = [
    ['sno', 'srollno', 'sname', 'sfathername'],
    ['1', '17001570001', 'ABHISHEK KUMAR', 'MR. NARESH KUMAR'],
    ['2', '17001570002', 'ABHISHEK SHUKLA', 'MR. RAKESH CHNADRA SHUKLA']
]

'''
# Demo

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<table>
chill
</table>
<table cellspacing="0" rules="all" border="1" id="gvshow" style="width:100%;border-collapse:collapse;">
        <tr>
            <th scope="col">Sr. No.</th><th scope="col">Rollno</th><th scope="col">Student Name</th><th scope="col">Father's Name</th>
        </tr><tr>
            <td align="center">1</td><td>17001570001</td><td>ABHISHEK KUMAR</td><td>MR. NARESH KUMAR</td>
        </tr>
        </table>
        """
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

#'''
