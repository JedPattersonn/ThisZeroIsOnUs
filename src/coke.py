import requests
import json
import names
import datetime
import random
import time
import os
from twilio.rest import Client

def cokeMain(email, location, i):
    
    account_sid = "AC98454ff8150b7d6275f9fd781ca7c32a"
    auth_token = "f7cd936e3e1f1bb5ef24d8cf44d83518"
    client = Client(account_sid, auth_token)
    
    lines = open('proxies.txt').read().splitlines()
    myline =random.choice(lines)
    proxies = {"http":myline}

    if i > 18:
        print(f"[TASK {i}] | Sleeping for a minute to prevent rate limits...")
        time.sleep(60)
    
    firstName = names.get_first_name(gender='male')
    lastName = names.get_last_name()
    emailArray = []
    f=lambda s:s[11:]and[s[0]+w+x for x in f(s[1:])for w in('.','')]or[s]
    for s in f(email):
        emailArray.append(s)
    
    email = random.choice(emailArray)
    
    
    url = "https://prod.api.atscale.digital/api/user/signup"
    payload = json.dumps({
    "firstName": firstName,
    "lastName": lastName,
    "email": email,
    "terms": True,
    "date": "01/09/1948",
    "country": "United Kingdom of Great Britain and Northern Ireland (the)",
    "socialType": "organic",
    "venueId": location
    })
    headers = {
    'authority': 'prod.api.atscale.digital',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'campaignid': '61daefc99f0e07129c4a87af',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'origin': 'https://www.thiszeroisonus.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.thiszeroisonus.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

    response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)

    if response.text != "":
        response = response.json()
        response1 = response["result"]
        if response1 == False:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{time_now}] | Email already signed up")
            print(response)
        elif response1 == True:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            id = response["data"]["_id"]
            print(f"\033[1;32;40m[TASK {i}] | [{time_now}] | {id} | Check email & phone")
            responseURL = f"https://www.thiszeroisonus.com/location-check/{id}/email"
            
            
            #https://www.thiszeroisonus.com/location-check/61f00b33d780017a3945a409/email
            
            
            
            
            
            
            
            
            
    else:
        print(f"[TASK {i}] | Error, retrying...")

