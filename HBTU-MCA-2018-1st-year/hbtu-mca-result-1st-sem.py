import requests
from bs4 import BeautifulSoup

CombinedResult = []

for i in range(1,61):
    if(i<10):
        i = '0' + str(i)

    varRollNo = "1702310" + str(i)

    url = "http://hbtu.ac.in/stu_erp/BTechMCAdisply_studentresultfirstyr.php"
    payload = { "Roll_No": varRollNo }
    headers = {
        "Host": "hbtu.ac.in",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://hbtu.ac.in/stu_erp/BTechMCAresultfirstyr.php",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "17",
        "Cookie": "__cfduid=da573f785c99d8e7af3925eafb43a49281533622740",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    response = requests.post(url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')

    for img in soup.find_all('img'):
        img.decompose()
    VAR_filename = "htmlSave/" + varRollNo + '.html'
    with open(VAR_filename, "w") as file:
        file.write(str(soup.prettify()))

    # print(soup.prettify())

    if(soup.title.text == "Web"):
        continue

    # Get all tables
    allTables = soup.find_all('table')

    # Get result
    result = allTables[6].find_all('tr')[1].find_all('td')
    sstatus = result[2].text
    if sstatus == "FAIL":
        continue
    smarks = int(result[1].text.split('/')[0])
    sstatus = result[2].text
    sgpa = float(result[3].text)
    syear = str(result[0].text)

    # More Student Details
    sdetails =  allTables[1].find_all('tr')
    sname = sdetails[0].findAll("td")[1].text
    sfname = sdetails[1].findAll("td")[1].text
    srollno = sdetails[2].findAll("td")[1].text
    scourse = sdetails[3].findAll("td")[1].text

    res = {
        'rollno' : srollno,
        'name' : sname,
        'marks': smarks,
        'gpa' : sgpa,
        # 'fname' : sfname,
        # 'year' : syear,
        # 'course' : str(scourse)
    }
    # print(res)
    
    CombinedResult.append(res)

CombinedResult.sort(key = lambda x : x['marks'], reverse=True)
# print(CombinedResult)

with open('HBTU-MCA-2018-1st-year.txt','w') as f:
    print('{0:<5} {1:<11} {2:<25} {3:<9} {4:<7}'.format("S.No","Roll No.","Name","Marks","GPA"), file=f)
    for i,s in enumerate(CombinedResult):
        print('{0:<5} {1:<11} {2:<25} {3:<9} {4:<7}'.format(i+1,s['rollno'],s['name'],s['marks'],s['gpa']), file=f)


