import requests
import json
import names
import datetime
import random
import time
import os

def cokeMain(email, location, i):
    
    
    
    lines = open('proxies.txt').read().splitlines() #Open proxy file
    myline =random.choice(lines) #Get a random line from file
    proxies = {"http":myline} #Format proxy
    
    firstName = names.get_first_name(gender='male') #Get random first name
    lastName = names.get_last_name() #Get random last name
    emailArray = [] #Array of emails collected
    f=lambda s:s[11:]and[s[0]+w+x for x in f(s[1:])for w in('.','')]or[s] #Gmail Dot trick to get thousands of sign ups forward to same gmail account
    for s in f(email):
        emailArray.append(s) #Add all emails to array
    
    email = random.choice(emailArray) #Pick a random email from array
    
    
    url = "https://prod.api.atscale.digital/api/user/signup" #API endpoint
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
    'campaignid': '61daefc99f0e07129c4a87af', #Campaign ID, update whenever a new campagin is started
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

    if response.text != "": #Check if the request response has a body
        response = response.json()
        response1 = response["result"] #Will return False if the user has signed up or there is an error
        if response1 == False:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[TASK {i}] | [{time_now}] | Email already signed up"
        elif response1 == True: #Will respond with True if successful
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            id = response["data"]["_id"] #Get the response ID which is used in the URL emailed
            print(f"\033[1;32;40m[TASK {i}] | [{time_now}] | {id} | Check email")
            responseURL = f"https://www.thiszeroisonus.com/location-check/{id}/email" #This is the URL format you will get emailed. In the event that you do not receive emails, you can use this string manually.
    
    else:
        print(f"[TASK {i}] | Error...") #There was no body

