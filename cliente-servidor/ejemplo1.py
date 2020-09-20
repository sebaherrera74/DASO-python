import requests

#URL="http://localhost:8080/cgi-bin/inde.py"
URL="http://www.google.com"


r=requests.get(url=URL)

if r.status_code==200:
    print(r.text)
else:
    print("error code :" +str(r.status_code))
 