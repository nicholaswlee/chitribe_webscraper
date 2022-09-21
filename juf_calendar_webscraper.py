from socket import SOL_UDP
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = input('Enter - ')
html = urllib.request.urlopen("https://apps.juf.org/Calendar/default.aspx").read()
# Gives an object that is cleaned up html essentially
soup = BeautifulSoup(html, 'html.parser')

class Event:
    title = " "
    time = " "
    body = " "
    img = " "
    url = " "
    def __init__(self, title, time, img, body, url):
        self.title = title
        self.time = time
        self.body = body 
        self.img = img
        self.url = url
    def __str__(self): 
        return ("URL: " + self.url + "\nTitle: " + self.title + "\nTime: " + self.time + "\nImage: " + self.img + "\nDescription: " + self.body)

# Retrieve all of the anchor tags and returns a list
tags = soup('span', {"id" : "dlEvents_lblDT_0"})

time_id = "dlEvents_lblDT_"
recur_id = "dlEvents_lblRecurrInfo_"
title_id = "dlEvents_lblEventName_"
body_id = "dlEvents_lblEventDesc_"
location_id = "dlEvents_lblLocation_"
contact_id =  "dlEvents_lblContact_"
register_id = "dlEvents_hlRegistrationURL_"
events = []
event_objs = []
for tag in tags:
    body = tag.get_text()
    event_objs.append(Event("", "", "", body, ""))
i = 0 
while(True):
    time_tag = soup('span', {"id" : "dlEvents_lblDT_" + str(i)})
    if(len(time_tag) == 0):
        break
    else:
        recur_tag = soup('span', {"id" : "dlEvents_lblRecurrInfo_" + str(i)})
        title_tag = soup('span', {"id" : "dlEvents_lblEventName_" + str(i)})
        body_tag = soup('span', {"id" : "dlEvents_lblEventDesc_" + str(i)})
        location_tag = soup('span', {"id" : "dlEvents_lblLocation_" + str(i)})
        contact_tag = soup('span', {"id" : "dlEvents_lblContact_" + str(i)})
        register_tag = soup('a', {"id" : "dlEvents_hlRegistrationURL_" + str(i)})
        print("------------------------------------------------------------")
        print("Time: " + time_tag[0].get_text())
        print("Recuring: " + recur_tag[0].get_text())
        print("Title: " + title_tag[0].get_text())
        print("Body: " + body_tag[0].get_text("\n"))
        # Location
        if(len(location_tag) == 0):
            print("No location")
        else:
            print(location_tag[0].get_text(" "))
        # Contact
        print(contact_tag[0].get_text(" "))
        if(len(register_tag) == 0):
            print("No register link")
        else:
            print("Register: " + register_tag[0].get("href",None))
    i += 1
        



    





