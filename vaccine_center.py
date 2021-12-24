import json
import requests
import sys
import time
import os
clear=lambda: os.system('cls')


url=("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=")
e=input("Enter the PIN CODE\n")
url2=("&date=")
f=input("Enter the date:[format:DD-MM-YYYY]\n")
req=(url+e+url2+f+":")


json_data=requests.get(req)
data_py=json.loads(json_data.text)
temp=data_py["sessions"]
for i in range(0,10,1):
    clear()
    temp_1=temp[i]
    name=temp_1["name"]
    availability=temp_1["available_capacity"]
    date=temp_1["date"]
    fee=temp_1["fee"]
    print("Centre Name:",name)
    print("Available capacity",availability)
    print("Date:",date)
    print("Fee:",fee)
    print("-----------------------------------------------------")
    time.sleep(2)
    
