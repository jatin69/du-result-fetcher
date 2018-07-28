# fetch S.No, exam flag, course name and course code for ALL courses of DU 
# one time work - store in file
# Need to run at the end of this result session for complete list

# http://duexam.du.ac.in/RSLT_MJ2018/Students/List_Of_Students.aspx?
# StdType=REG&
# ExamFlag=CBCS&
# CourseCode=568&
# CourseName=(CBCS)%20B.SC.(HONS.)%20STATISTICS&
# Part=I&
# Sem=II

# above entries can help in extracting student details.
# But this old URL may go out of commission soon. & then we can't query the system
# >> super dependent on OLD URL
# If it goes out of commission, the script will be useless.

# Once we have access to student roll no & names
# also can simply filter students with regex & get result of that college
# we can simply extract college code from roll no and get his result.

