import requests
import json
import sys
e=sys.argv[1
]
url=("http://api.weatherapi.com/v1/current.json?key=9693d83b110342d9bd354744212212&q=")
url2="&aqi=no"
req=url+e+url2
x=requests.get(req)
y=(x.text)
z=json.loads(y)
a=z["location"]
name_p=a["name"]
cur=z["current"]
temp=cur["temp_c"]
print(name_p,temp,sys.argv)
