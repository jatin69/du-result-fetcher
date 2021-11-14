import requests

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

# payload='regno=2605413&B1=Submit'



allRolls = [2605413]


for roll in allRolls:
    payload = { 'regno' : roll, 'B1' : 'Submit'}
    response = requests.post(url, data=payload, headers=headers, verify=False)
    print(response.text)
    filename = "saved/" + str(roll) + '.txt'
    with open(filename,'w') as f:
        print(response.text, file=f)
