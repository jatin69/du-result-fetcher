"""
From a list of students, filter students based on roll no pattern
"""

data = [
    ['1', '17001570001', 'ABHISHEK KUMAR', 'MR. NARESH KUMAR'],
    ['2', '17001530002', 'ABHISHEK SHUKLA', 'MR. RAKESH CHNADRA SHUKLA'],
    ['3', '17015570001', 'a', 'd']
]

print(data)

import re

dduc = []
for student in data:
    if re.match("17001570...", student[1]):
        dduc.append(student)

print(dduc)

'''
import re
mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
r = re.compile(".*cat")
newlist = filter(r.match, mylist)
print str(newlist)
'''
