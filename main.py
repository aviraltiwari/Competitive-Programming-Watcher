#!/usr/bin/env python3

# @author - aviraltiwari
#

# TODO Duration
# TODO startTimeinSeconds

import requests, time

response = requests.get('https://codeforces.com/api/contest.list').json()

#for data in response['result']:
#    print(data)

for data in response['result']:
    if data["phase"] == "BEFORE":
        #startTime = time.strftime('%H:%M:%S', time.gmtime(data["startTimeSeconds"]))
        startTime = time.ctime(data["startTimeSeconds"])
        duration = time.ctime(data["durationSeconds"])
        print("🐱‍👤 Name: " + data["name"] + " +  "⏲ Start Time" + startTime + " +  "⏳ Duration" + duration)

