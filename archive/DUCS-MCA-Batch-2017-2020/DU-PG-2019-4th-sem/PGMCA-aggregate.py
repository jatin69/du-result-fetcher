# dependencies
import requests
from bs4 import BeautifulSoup
import re
import sys
import os

savePath = "html"
if not os.path.isdir(savePath):
    os.mkdir(savePath)

# link for 6th sem 2019 - new link
GradeCard = "http://duresult.in/students/Combine_GradeCard.aspx"

CONST_VIEWSTATE = """/wEPDwUJOTc3OTgxMzM3DxYEHgdjYXB0Y2hhBQYxODIyODkeCUlwQWRkcmVzcwUMMTAzLjc4LjE0OC44FgICAw9kFgwCAQ9kFgICBQ8PFgIeBFRleHQFNFJlc3VsdHMgKFNlbWVzdGVyL0FubnVhbCBFeGFtaW5hdGlvbiBNYXktSnVuZSAyMDE5IClkZAIHDw8WAh8CBRAgKE1heS1KdW5lIDIwMTkpZGQCFQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQlDT0xMX05BTUUeDkRhdGFWYWx1ZUZpZWxkBQlDT0xMX0NPREUeC18hRGF0YUJvdW5kZ2QQFX8SPC0tLS0tU2VsZWN0LS0tLS0+HEFjaGFyeWEgTmFyZW5kcmEgRGV2IENvbGxlZ2UkQWRpdGkgTWFoYXZpZGhsYXlhIChUZWFjaGluZyBDZW50cmUpE0FkaXRpIE1haGF2aWR5YWxheWElQXJ5YWJoYXR0YSBDb2xsZWdlIChUZWFjaGluZyBDZW50cmUpID1BcnlhYmhhdHRhIENvbGxlZ2UgW0Zvcm1lcmx5IFJhbSBMYWwgQW5hbmQgQ29sbGVnZSAoRXZlbmluZyldH0F0bWEgUmFtIFNhbmF0YW4gRGhhcmFtIENvbGxlZ2UYQmhhZ2luaSBOaXZlZGl0YSBDb2xsZWdlKkJoYWdpbmkgTml2ZWRpdGEgQ29sbGVnZSAoVGVhY2hpbmcgQ2VudHJlKQ9CaGFyYXRpIENvbGxlZ2UhQmhhcmF0aSBDb2xsZWdlIC0gVGVhY2hpbmcgQ2VudHJlKkJoYXNrYXJhY2hhcnlhIENvbGxlZ2Ugb2YgQXBwbGllZCBTY2llbmNlcxFDQU1QVVMgTEFXIENFTlRSRRdDYW1wdXMgb2YgT3BlbiBMZWFybmluZyJDbHVzdGVyIElubm92YXRpb24gQ2VudHJlIChDLkkuQy4pHUNvbGxlZ2UgT2YgVm9jYXRpb25hbCBTdHVkaWVzL0NvbGxlZ2Ugb2YgVm9jYXRpb25hbCBTdHVkaWVzIChUZWFjaGluZyBDZW50cmUpEkRhdWxhdCBSYW0gQ29sbGVnZRxEZWVuIERheWFsIFVwYWRoeWF5YSBDb2xsZWdlLkRlZW4gRGF5YWwgVXBhZGh5YXlhIENvbGxlZ2UgKFRlYWNoaW5nIENlbnRyZSkgRGVsaGkgQ29sbGVnZSBPZiBBcnRzICYgQ29tbWVyY2UaRGVsaGkgU2Nob29sIG9mIEpvdXJuYWxpc21kRGVwYXJ0bWVudCBvZiBCb3RhbnkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGREZXBhcnRtZW50IG9mIENoZW1pc3RyeSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgFkRlcGFydG1lbnQgb2YgQ29tbWVyY2VkRGVwYXJ0bWVudCBvZiBDb21wdXRlciBTY2llbmNlICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBEZXBhcnRtZW50IG9mIEVkdWNhdGlvbiAoQy5JLkUuKRVEZXBhcnRtZW50IG9mIEVuZ2xpc2gXRGVwYXJ0bWVudCBvZiBHZW9ncmFwaHkqRGVwYXJ0bWVudCBvZiBHZXJtYW5pYyBhbmQgUm9tYW5jZSBTdHVkaWVzE0RlcGFydG1lbnQgb2YgSGluZGkVRGVwYXJ0bWVudCBvZiBIaXN0b3J5G0RlcGFydG1lbnQgb2YgSGlzdG9yeSAoU0RDKS1EZXBhcnRtZW50IG9mIExpYnJhcnkgYW5kIEluZm9ybWF0aW9uIFNjaWVuY2VkRGVwYXJ0bWVudCBvZiBNYXRoZW1hdGljcyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIBNEZXBhcnRtZW50IG9mIE11c2ljZERlcGFydG1lbnQgb2YgUGh5c2ljcyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAfRGVwYXJ0bWVudCBvZiBQb2xpdGljYWwgU2NpZW5jZRZEZXBhcnRtZW50IG9mIFNhbnNrcml0ZERlcGFydG1lbnQgb2YgU29jaWFsIFdvcmsgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkRGVwYXJ0bWVudCBvZiBTdGF0aXN0aWNzICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGREZXBhcnRtZW50IG9mIFpvb2xvZ3kgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgGERlc2hiYW5kaHUgQ29sbGVnZSAoRGF5KStEci4gQW1iZWRrYXIgQ2VudGVyIGZvciBCaW9tZWRpY2FsIFJlc2VhcmNoI0RyLiBCLlIuIEFtYmVka2FyIChUZWFjaGluZyBDZW50cmUpHURyLiBCaGltIFJhbyBBbWJlZGthciBDb2xsZWdlNUR1cmdhYmFpIERlc2htdWtoIENvbGxlZ2Ugb2YgU3BlY2lhbCBFZHVjYXRpb24gKFYuSS4pGER5YWwgU2luZ2ggQ29sbGVnZSAoRGF5KRhEeWFsIFNpbmdoIENvbGxlZ2UgKEV2ZSkdRmFjdWx0eSBvZiBNYW5hZ2VtZW50IFN0dWRpZXMNR2FyZ2kgQ29sbGVnZRBIYW5zIFJhaiBDb2xsZWdlIkhhbnMgUmFqIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUNSGluZHUgQ29sbGVnZRVJLlAuQ29sbGVnZSBGb3IgV29tZW42SW5kaXJhIEdhbmRoaSBJbnN0aXR1dGUgb2YgUGh5LiBFZHUuICYgU3BvcnRzIFNjaWVuY2VzLkluc3RpdHV0ZSBvZiBDeWJlciBTZWN1cml0eSBhbmQgTGF3IChJLkMuUy5MLikbSW5zdGl0dXRlIE9mIEhvbWUgRWNvbm9taWNzG0phbmtpIERldmkgTWVtb3JpYWwgQ29sbGVnZS1KYW5raSBEZXZpIE1lbW9yaWFsIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUUSmVzdXMgJiBNYXJ5IENvbGxlZ2UmSmVzdXMgJiBNYXJ5IENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUMSnViaWxlZSBIYWxsD0thbGluZGkgQ29sbGVnZSFLYWxpbmRpIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUTS2FtbGEgTmVocnUgQ29sbGVnZSRLZXNoYXYgTWFoYXZpZGxheWEgKFRlYWNoaW5nIENlbnRyZSkUS2VzaGF2IE1haGF2aWR5YWxheWESS2lyb3JpIE1hbCBDb2xsZWdlEkxhZHkgSXJ3aW4gQ29sbGVnZR5MYWR5IFNyaSBSYW0gQ29sbGVnZSBGb3IgV29tZW4STGFrc2htaWJhaSBDb2xsZWdlJExha3NobWliYWkgQ29sbGVnZSAtIFRlYWNoaW5nIENlbnRyZQxMQVcgQ0VOVFJFLUkNTEFXIENFTlRSRS1JSRhNYWhhcmFqYSBBZ3Jhc2VuIENvbGxlZ2UqTWFoYXJhamEgQWdyYXNlbiBDb2xsZWdlIC0gVGVhY2hpbmcgQ2VudHJlJU1haGFyc2hpIFZhbG1pa2kgQ29sbGVnZSBvZiBFZHVjYXRpb24QTWFpdHJleWkgQ29sbGVnZSJNYWl0cmV5aSBDb2xsZWdlIC0gVGVhY2hpbmcgQ2VudHJlHU1hdGEgU3VuZHJpIENvbGxlZ2UgRm9yIFdvbWVuL01hdGEgU3VuZHJpIENvbGxlZ2UgRm9yIFdvbWVuIC0gVGVhY2hpbmcgQ2VudHJlDU1pcmFuZGEgSG91c2UfTWlyYW5kYSBIb3VzZSAoVGVhY2hpbmcgQ2VudHJlKRxNb3RpIExhbCBOZWhydSBDb2xsZWdlIChEYXkpHE1vdGkgTGFsIE5laHJ1IENvbGxlZ2UgKEV2ZSkoTW90aSBMYWwgTmVocnUgQ29sbGVnZSAoVGVhY2hpbmcgQ2VudHJlKSxOb24gQ29sbGVnaWF0ZSBXb21lbiBFZHVjYXRpb24gQm9hcmQgKE5DV0VCKRhQLkcuRC5BLlYuIENvbGxlZ2UgKERheSkYUC5HLkQuQS5WLiBDb2xsZWdlIChFdmUpJFAuRy5ELkEuVi4gQ29sbGVnZSAtIFRlYWNoaW5nIENlbnRyZRBSYWpkaGFuaSBDb2xsZWdlIlJhamRoYW5pIENvbGxlZ2UgKFRlYWNoaW5nIENlbnRyZSkbUmFtIExhbCBBbmFuZCBDb2xsZWdlIChEYXkpEVJhbWFudWphbiBDb2xsZWdlI1JhbWFudWphbiBDb2xsZWdlIChUZWFjaGluZyBDZW50cmUpDlJhbWphcyBDb2xsZWdlF1MuRy5ULkIuIEtoYWxzYSBDb2xsZWdlF1NhdHlhd2F0aSBDb2xsZWdlIChEYXkpF1NhdHlhd2F0aSBDb2xsZWdlIChFdmUpJFNhdHlhd2F0aSBDb2xsZWdlIChUZWFjaGluZyBDZW50cmUpIBdTY2hvb2wgb2YgT3BlbiBMZWFybmluZyJTaGFoZWVkIEJoYWdhdCBTaW5naCBDb2xsZWdlIChEYXkpIlNoYWhlZWQgQmhhZ2F0IFNpbmdoIENvbGxlZ2UgKEV2ZSk1U2hhaGVlZCBSYWpndXJ1IENvbGxlZ2Ugb2YgQXBwbGllZCBTY2llbmNlcyBmb3IgV29tZW4rU2hhaGVlZCBTdWtoZGV2IENvbGxlZ2Ugb2YgQnVzaW5lc3MgU3R1ZGllcw9TaGl2YWppIENvbGxlZ2UXU2h5YW0gTGFsIENvbGxlZ2UgKERheSkXU2h5YW0gTGFsIENvbGxlZ2UgKEV2ZSkxU2h5YW1hIFByYXNhZCBNdWtoZXJqZWUgQ29sbGVnZSAtIFRlYWNoaW5nIENlbnRyZShTaHlhbWEgUHJhc2FkIE11a2hlcmppIENvbGxlZ2UgZm9yIFdvbWVuFlNPTCBTdHVkeSBDZW50ZXIgU291dGgbU3JpIEF1cm9iaW5kbyBDb2xsZWdlIChEYXkpG1NyaSBBdXJvYmluZG8gQ29sbGVnZSAoRXZlKSdTcmkgQXVyb2JpbmRvIENvbGxlZ2UgKFRlYWNoaW5nIENlbnRyZSkpU3JpIEd1cnUgR29iaW5kIFNpbmdoIENvbGxlZ2UgT2YgQ29tbWVyY2U7U3JpIEd1cnUgR29iaW5kIFNpbmdoIENvbGxlZ2UgT2YgQ29tbWVyY2UgLSBUZWFjaGluZyBDZW50cmUhU3JpIEd1cnUgTmFuYWsgRGV2IEtoYWxzYSBDb2xsZWdlG1NyaSBSYW0gQ29sbGVnZSBPZiBDb21tZXJjZRhTcmkgVmVua2F0ZXN3YXJhIENvbGxlZ2UUU3QuIFN0ZXBoZW5zIENvbGxlZ2UaU3dhbWkgU2hyYWRkaGFuYW5kIENvbGxlZ2UTVW5pdmVyc2l0eSBvZiBEZWxoaRNWaXZla2FuYW5kYSBDb2xsZWdlJVZpdmVrYW5hbmRhIENvbGxlZ2UgLSBUZWFjaGluZyBDZW50cmUaWmFraXIgSHVzYWluIENvbGxlZ2UgKEV2ZSkgWmFraXIgSHVzYWluIERlbGhpIENvbGxlZ2UgKERheSkVfxI8LS0tLS1TZWxlY3QtLS0tLT4DMDAxBDEzMTQDMDAyBDEzMTUDMDU5AzAwMwMwMDcEMTMxNwMwMDgEMTMwNwMwMDkDMzA5A0NPTAMzMTIDMDEzBDEzMTgDMDE0AzAxNQQxMzI2AzAxNgMzMTYDMjE2AzIxNwMyNDEDMjM0AzI0MwMyMDMDMjI5AzIwNAMyMDUDMjMxAzI5MQMyMDYDMjM1AzI0MAMyMjIDMjMyAzIxMwMyMzMDMjM3AzIyMwMwMTkDMzE4BDEzMTYDMDEwAzMxNAMwMjEDMDIyAzEwOQMwMjQDMDI1BDEzMTMDMDI2AzAyOQMwMjgDMzE3AzAzMAMwMzEEMTMwNAMwMzIEMTMwOAMzMDYDMDMzBDEzMDUDMDM0BDEzMTkDMDM1AzAzNgMwMzgDMDM5AzA0MAQxMzEwAzMxMAMzMTEDMDQxBDEzMDIDMzE1AzA0MwQxMzA5AzA0NAQxMzAzAzA0NwQxMzIwAzA0OAMwNDkEMTMyMQMzMDcDMDUzAzA1NAQxMzExAzA1NQQxMzIyAzA1OAMwMjAEMTMyMwMwNTYDMDY4AzA2MgMwNjMEMTMyNANTT0wDMDY0AzA2NQMwNjYDMDY3AzA3MQMwNzMDMDc0BDEzMDYDMDc1BFNPTFMDMDc2AzA3NwQxMzI1AzA3OAQxMzEyAzA2OQMwNzIDMDc5AzA4MAMwODEDMTAwAzA4NAQxMzAxAzA4NgMwODUUKwN/Z2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAh0PZBYCZg9kFgICAw8PFgIeCEltYWdlVXJsBUNHZW5lcmF0ZUNhcHRjaGEuYXNweD9DYXB0Y2hhQ29kZT0xODIyODkmRGF0ZVRpbWU9NjM2OTczOTcyNzY0MDA1Nzk2ZGQCJw8PFgIeB1Zpc2libGVoZGQCLQ8PFgIfB2hkZGR2bl/3EI/pExtevTdMuWF0S/G/qQ=="""

CONST_VIEWSTATEGENERATOR = """35D4F7A9"""

CONST_EVENTVALIDATION = """/wEWhQECrP631AECq8PapwoCypTxxQ4CwPyMgQgCwfyo/goC5evuqgICwfzcmgMC6KaP6wkC/oLBtwQC4uX5gA8Cwfz0UALXj7neBwKsxZLHDgLoppvrCQLvppvrCQKewq+LCALY6+KqAgL+gsW3BALB/Ni7AgKTuKfBCQK017nqAwLa66LBDQLJzpv3BQLMzpv3BQLPzpv3BQLg5f2ADwLG/LyBCAKRuN/ACQL8gvG3BAL8gsG3BALuppPrCQKRuKPBCQKq14XqAwLG/LiBCALG/OCBCALPzuf3BQKq17HqAwKtxdr3BgLb6+aqAgLb65qqAgL8gsW3BAL8gv23BALg5fWADwL8gvm3BALopp/rCQLKj73eBwLB/MC3CAKvxa70BgKWuKfBCQLA/ISBCALl6+aqAgLpppvrCQKTuNvACQK0173qAwLB/ITFDQLJzp/3BQLoppPrCQLXj7HeBwLh5f2ADwKvxab0BgLA/LiBCAKsxdZUAuXrmqoCAqzFxq4IAszO5/cFAv6C/bcEAqzF+vEJApO438AJAsH8zNQKArTXseoDAsnOk/cFAtePtd4HAuiml+sJAq/F2vcGAsH8+NIHAqLFrvQGAsf8gIEIAsD8vIEIAqzFvp8DAqvXueoDAv6C8bcEAqzF6ksCk7jTwAkCrMWiuAgC4uXpgA8C2uva/wkC14+p3gcC6KaL6wkC2uvOmAYC4eX5gA8C/oL1twQCk7jXwAkCwfzsjwwCtNep6gMC2uvytQ8C14+t3gcCr8Wi9AYC2uvm7gcCyc6L9wUC14+h3gcC5euWqgIC/oLptwQC2uuKiwwCrsKviwgCk7jLwAkCtNet6gMCyc6P9wUC4uXhgA8CwPyogQgC/oLttwQCk7jPwAkCrMXuqgYCtNeh6gMCrsKr/gkCyc6D9wUC4uXlgA8C2uu+pAUC14+l3gcCwfyQqAUC6KaD6wkC5euKqgIC6KaH6wkCr8WK9AYCwPzsgQgCrMWq9AYCk7iDwQkCrMWK4goCyc7H9wUCtNfl6gMCtPew8AwCwJ/r5gwC75nRggMCpZ/ziwJBxkgslz2Udq2i1suw/QwLnFI92A=="""

# store marks list for all DU
college_sgpa_list = []

# list codes for all CS colleges
all_colleges = [
    "16001570001",
    "16003570001",
    "16009570001",
    "16013570001",
    "16015570001",
    "16020570001",
    "16021570001",
    "16025570001",  
    "16029570001",
    "16033570001",
    "16035570001",
    "16044570001",
    "16053570001",
    "16058570001",
    "16059570001",
    "16066570001",
    "16067570001",
    "16068570001",
    "16075570001",
    "16078570001"
    ]

# override for one college check
all_colleges = [
    "1724501"
]

for col in all_colleges:
    dduc = []
    constantCollegePart = col[:-2]
    for i in range(1,10):
        dduc.append([constantCollegePart + '0' + str(i)])
    for i in range(10,50):
        dduc.append([constantCollegePart + str(i)])
    
    # testing generation of rollnos
    # print(dduc)
    # break
    # dduc = [['1724514']]
    VAR_collegeCode = "234"   
    for VAR_stud in dduc:
        VAR_rollno = VAR_stud[0]
        # print(VAR_rollno)
        payload = {
            '__EVENTTARGET' : '',
            '__EVENTARGUMENT' : '',
            '__VIEWSTATE': CONST_VIEWSTATE,
            '__VIEWSTATEGENERATOR': CONST_VIEWSTATEGENERATOR,
            '__EVENTVALIDATION': CONST_EVENTVALIDATION,
            'ddlcollege' : VAR_collegeCode,
            'txtrollno' : VAR_rollno,
            'txtcaptcha' : '182289',
            'btnsearch': 'Print+Score+Card'
            }
        
        # infinite cookie life
        cookies = {'ASP.NET_SessionId': 'efstl5454kxusy45e35h45j1'}

        soup = None
        count = 0
        while(soup == None):
            r = requests.post(GradeCard, data=payload, cookies=cookies)
            # print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            if(soup==None):
                continue
            # print(soup.title.string)
            if(soup.title.string == "Runtime Error"):
                if count == 5:
                    break
                else:
                    count = count + 1
                soup = None
                continue
        
        if count == 5:
            continue
        # for img in soup.find_all('img'):
        #     img.decompose()

        #t = soup.find('span', attrs={'id':'lblstatement'}).decompose()
        #t = soup.find('span', attrs={'id':'lbl_sub_head3'}).decompose()
        #t = soup.find('span', attrs={'id':'lbldisclaimer'}).decompose()
        
        # // todo 
        # sgpa_table = soup.find("span", {"id": "lbl_gr_cgpa"})
        # print(soup)
        # print(college_sgpa_list)

        if soup.find("span", id="lblcollege") == None:
            continue
        if soup.find("span", id="lblname") == None:
            continue
        
        VAR_college = soup.find("span", id="lblcollege").text
        VAR_sname = soup.find("span", id="lblname").text

        # writing result to html file
        savePath = "html/"+VAR_college.replace(' ', '_')
        if not os.path.isdir(savePath):
            os.mkdir(savePath)
        VAR_filename = savePath + '/' + VAR_rollno + '__' + VAR_sname + '__' + '.html'
        with open(VAR_filename, "w") as file:
            file.write(str(soup))

        # print(VAR_college, VAR_sname);
        # total = soup.find("table", id="lblgrandtotal")
        sgpa_table = soup.find("table", {"id": "gvrslt"})
        if(sgpa_table == None ):
            continue
        try:
            sems = sgpa_table.findAll('tr')
            obtained_marks = 0
            for i in range(1,len(sems)):
                obtained_marks = obtained_marks + int(sems[i].findAll('td')[1].text)
            total_marks = 5*4
            FINAL_CGPA = (obtained_marks)/total_marks
            print([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])
        except IndexError:
            continue
        college_sgpa_list.append([VAR_rollno, VAR_sname, FINAL_CGPA, VAR_college])
        

exit
college_sgpa_list.sort(key = lambda x : x[2], reverse=True)
# print(college_sgpa_list)

# print to file
with open('DU-PG-MCA-2017-2019-aggregate.txt','w') as f:
    print('{3:<5} {0:15} {1:25} {2:10} {4:<40}'.format("Roll No.","Name","aggregate","S.No", "College"), file=f)
    for i,marks in enumerate(college_sgpa_list):
        print('{3:<5} {0:15} {1:25} {2:<10} {4:<40}'.format(marks[0],marks[1],marks[2], i+1, marks[3]), file=f)

# CSV print to file
with open('DU-PG-MCA-2017-2019-aggregate.csv.txt','w') as f:
    print('{3:<5} ,{0:15} ,{1:25} ,{2:10} ,{4:<40}'.format("Roll No.","Name","aggregate","S.No", "College"), file=f)
    for i,marks in enumerate(college_sgpa_list):
        print('{3:<5} ,{0:15} ,{1:25} ,{2:<10} ,{4:<40}'.format(marks[0],marks[1],marks[2], i+1, marks[3]), file=f)

# print(soup.prettify())

# with open("test.html", "w") as file:
#     file.write(str(soup))
