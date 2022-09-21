from socket import SOL_UDP
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = input('Enter - ')
html = urllib.request.urlopen("https://www.ansheemet.org/engage/events/").read()
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
tags = soup('a')
events = []
for tag in tags:
    if("events" in tag.get('href', None) and "https://www.ansheemet.org/engage/events/" not in tag.get('href', None) 
        and not (tag.get('href', None) in events)):
        events.append(tag.get('href', None));
        print(tag.get('href', None))
event_objs = []
print(events)
for event_url in events:
    html = urllib.request.urlopen(event_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    strongs = soup('strong')
    h1s = soup("h1")
    imgs = soup("img")
    b = soup("body")
    links = soup.find_all("a", {"class" : "fasc-button fasc-size-large fasc-type-glossy fasc-rounded-medium"})
    div = soup.find_all("div", {"class": "row event-page"})
    time = " "
    heading = " "

    for strong in strongs:
        print(strong.contents[0])
        if ("pm" in strong.contents[0] or "am" in strong.contents[0] or "Day" in strong.contents[0]):
            time = strong.contents
    for h1 in h1s:
        heading = h1.contents
    for img in imgs:
        if("uploads" in img.get("src", None)):
            image = img.get("src", None)
    body = ""
    
        #if(not ("\n" in p.get_text() or "Add to iCalAdd to Google Calendar" in p.get_text())):
    body = div[0].get_text().split("Add to iCalAdd to Google Calendar")[1].strip()
    if("Register here" in body or "Register Here" in body):
        split = body.split("Register here")
        body = split[0] + "Register Here: " + links[0].get("href",None) + split[1]
    event_objs.append(Event(heading[0], time[0], image, body, event_url))
for e in event_objs:
    print("------------------------------------------------------------")
    print(e)
    
    






