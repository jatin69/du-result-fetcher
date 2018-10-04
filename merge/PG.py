"""
Merge of PGmca and PGmsc from DU-PG-2018-2nd-sem
"""
import pathlib

import requests
from bs4 import BeautifulSoup

from . import config


def main(course_code: str, output_dir: str, result_file: str):
    get_payload = {
        'StdType': 'REG',
        'ExamFlag': 'PG_SEMESTER_2Y',
        'CourseCode': course_code,
        'CourseName': '(P.G)-%20MASTER%20OF%20COMPUTER%20APPLICATION%20(M.C.A.)',
        'Part': 'I',
        'Sem': 'II',
    }

    r = requests.get('http://duexam.du.ac.in/RSLT_MJ2018/Students/List_Of_Students.aspx', params=get_payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    students_table = soup.find("table", {"rules": "all"})
    all_students = students_table.find_all('tr')
    data = []

    for student in all_students:
        cols = [ele.text.strip() for ele in student.find_all('td')]
        cols = [ele for ele in cols if ele]  # Get rid of empty values
        if not cols:
            continue
        data.append(cols)

    college_sgpa_list = []

    for stud in data:
        # stud rows: 'sno', 'srollno', 'sname', 'sfathername'
        roll_no = stud[1]

        post_payload = {
            'ddlcollege': '234',
            'txtrollno': roll_no,
            'btnsearch': 'Print+Score+Card',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': config.VIEWSTATE,
            '__EVENTVALIDATION': config.EVENTVALIDATION
        }

        while True:
            # print('trying')
            r = requests.post("http://duexam.du.ac.in/RSLT_MJ2018/Students/Combine_GradeCard.aspx", data=post_payload)
            # print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup is None:
                continue
            # print(soup.title.string)
            if soup.title.string == "Runtime Error":
                continue
            break

        # writing result to html file

        for img in soup.find_all('img'):
            img.decompose()

        pathlib.Path(f'./{output_dir}/').mkdir(parents=True, exist_ok=True)  # create output dir

        with open(f"{output_dir}/{roll_no}.html", "w") as file:
            file.write(str(soup))

        sgpa_table = soup.find("table", {"id": "gvrslt"})
        # print(sgpa_table)

        if sgpa_table is None:
            continue

        xrows = sgpa_table.findAll('tr')
        sgpa_row = xrows[2].find_all('td')

        m = sgpa_row[1].text

        # print([roll_no, int(m) ])
        name = stud[2]
        college_sgpa_list.append([roll_no, name, int(m)])

    college_sgpa_list.sort(key=lambda x: x[2], reverse=True)
    # print(college_sgpa_list)

    with open(result_file, 'w') as f:
        print('{0:<5} {1:10} {2:21} {3:5} {4:7}'.format("S.No", "Roll No.", "Name", "Marks", "Percentage"), file=f)
        for i, marks in enumerate(college_sgpa_list):
            print('{0:<5} {1:10} {2:21} {3:5} {4:7}'.format(i + 1, marks[0], marks[1], marks[2], float(marks[2] / 5)),
                  file=f)
