import requests
from bs4 import BeautifulSoup
import re
import sys
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://resultsarchives.nic.in/cbseresults/cbseresults2015/class12/cbse122015_all.asp"

headers = {
  'Host': 'resultsarchives.nic.in',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Origin': 'https://resultsarchives.nic.in',
  'Connection': 'keep-alive',
  'Referer': 'https://resultsarchives.nic.in/cbseresults/cbseresults2015/class12/cbse122015_all.htm',
  'Upgrade-Insecure-Requests': '1',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'TE': 'trailers'
}


allRolls = []
subjectToFind = 'COMPUTER SCIENCE'
completeList = []

allNames = []

for roll in allRolls:
    payload = { 'regno' : roll, 'B1' : 'Submit'}
    r = requests.post(url, data=payload, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')


    name_table = soup.findAll("table", {"width":"75%"})[1]
    rows = name_table.findAll("tr")

    name = rows[1].findAll("font")[2].text.strip()
    rollNo = int(rows[0].findAll("font")[1].text.strip())
    allNames.append([rollNo, name])
    # print(str(rollNo) + "\n")

    result_table = soup.find("table", {"bordercolor":"#000000"})
    # print(result_table)
    subRow = None
    subjectFound = False
    totalMarks = 0

    for row in result_table.findAll("tr")[1:6]:
        allFonts = row.findAll("font")
        # print(allFonts)
        for font in allFonts:
            if font.text == subjectToFind:
                subRow = row
                subjectFound = True
    
        try:
            sub = allFonts[1].text.strip()
            marksInSub = int(allFonts[4].text.strip())
            # print(marksInSub)
            totalMarks += marksInSub     
        except IndexError:
            # print(rollNo)
            continue
        except ValueError:
            # print("failure = " + str(rollNo))
            continue
        
    if(subjectFound is False):
        continue

    marksInSub = None
    overAllPercentage = None
    try:
        # only valid subjects proceed
        marksInSub = int(subRow.findAll("font")[4].text.strip())
        # print(marksInSub)
        overAllPercentage = float(totalMarks/5.0)
    except IndexError:
        # print(rollNo)
        continue
    except ValueError:
        # print("failure = " + str(rollNo))
        continue
        
    x = [rollNo, name, overAllPercentage, marksInSub]
    print(x)
    completeList.append(x)

    # FILENAME = "saved/" + str(roll) + '.txt'
    # with open(FILENAME,'w') as f:
    #     print(r.text, file=f)



# completeList.sort(key = lambda x : x[0], reverse=True)
completeList.sort(key = lambda x : x[0])
allNames.sort(key = lambda x : x[0])
# print(completeList)

with open('CBSE-2015.txt','w') as f:
    print('{0:<5} ,{1:<15} ,{2:25} ,{3:<15} ,{4:<15}'.format("S.No","Roll No.","Name","Percentage","Marks in CS"), file=f)
    for i,marks in enumerate(completeList):
        print('{0:<5} ,{1:<15} ,{2:25} ,{3:<15} ,{4:<15}'.format(i+1,marks[0],marks[1],marks[2], marks[3]), file=f)

with open('names-2015.txt','w') as f:
    print('{0:<5} ,{1:<15} ,{2:25}'.format("S.No","Roll No.","Name"), file=f)
    for i,marks in enumerate(allNames):
        print('{0:<5} ,{1:<15} ,{2:25}'.format(i+1,marks[0],marks[1]), file=f)

