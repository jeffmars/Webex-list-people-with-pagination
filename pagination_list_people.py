import requests
import json
import time

def sendSparkGET(url):
    response = requests.get(url,
                           headers={"Accept" : "application/json",
                                    "Content-Type":"application/json",
                                    "Authorization": "Bearer "+bearer})
    return response


bearer = "YOUR_ACCESS_TOKEN" #my token

counter = 0
url = 'https://webexapis.com/v1/people'
items = []
while url != None:
    try:
        result = sendSparkGET(url)
        print(result.status_code)
        url = result.headers.get("Link")
        if url:
            url, extra = url.split(">;")
            url = url[1:]
        print(url)
        counter += 1
        print(counter)
        items += result.json()['items']
    except Exception as e:
        print(e)
        print(result.status_code)
        print(e.headers)
        print(dir(e))
        print(e.read())
print(items)
print("Final items length: {0}".format(len(items)))
