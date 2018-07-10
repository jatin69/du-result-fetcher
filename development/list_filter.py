data = [
['1', '17001570001', 'ABHISHEK KUMAR', 'MR. NARESH KUMAR'],
['2', '17001530002', 'ABHISHEK SHUKLA', 'MR. RAKESH CHNADRA SHUKLA'],
    ['3','17015570001','a','d']
    ]


print(data)

import re
dduc = []
for student in data:
    if re.match("17001570...",student[1]):
        dduc.append(student)
    
print(dduc)






'''
result_list = filter(lambda x: x, [[student for ele in student if re.match('(17015570)...', str(student[0]))] for student in data])


import re
mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
r = re.compile(".*cat")
newlist = filter(r.match, mylist)
print str(newlist)
'''

