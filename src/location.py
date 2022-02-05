from django.http import JsonResponse
from itsdangerous import exc
import requests
import json
import random

def locationModule(postcode):

  

    postcode = postcode.replace(' ', '%20')

    url = f"https://api.promaptools.com/service/uk/postcode-lat-lng/get/?postcode={postcode}&key=17o8dysaCDrgv1c"

    payload={}
    headers = {
    'authority': 'api.promaptools.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://www.freemaptools.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.freemaptools.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    try:
        responseJSON = response.json()
        longitude = responseJSON["output"][0]["longitude"]
        latitude = responseJSON["output"][0]["latitude"]
    except:
        print("Could not get co-ordinates")
        input("Press enter to go back to the menu...")
        


    url = "https://prod.api.atscale.digital/api/user/locations"

    payload = json.dumps({
    "latitude": latitude,
    "longitude": longitude,
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

    response = requests.request("POST", url, headers=headers, data=payload)

    JsonResponse = response.json()
    results = JsonResponse["data"]
    for i in results:
        print("{} | {}".format(i["name"], i["_id"]))


