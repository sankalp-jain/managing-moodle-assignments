import mechanicalsoup
import requests
from bs4 import BeautifulSoup
l1 = []

loginurl = 'http://moodlecc.vit.ac.in/login/index.php';

print("Enter username")
user = input()

print("Enter password")
password = input()
dashboard = 'http://moodlecc.vit.ac.in/?redirect=0'

s = requests.Session()
s.post(loginurl, {'id' : 'login', 'username' : user, 'password' : password}, allow_redirects=True)
r = s.get(dashboard)
r = r.text

soup = BeautifulSoup(r, 'html.parser')
divTag = soup.find_all("div", {"class": "courses frontpage-course-list-enrolled"})
l = []
for tag in divTag:
    tdTags = tag.find_all('a')
    for tag in tdTags:
        if tag["href"].startswith("http://moodlecc.vit.ac.in/course/view.php?id"):
            l.append(tag)
d = {}

for i in l:
    d[i["href"]] = i.text
for i in d.values():
    l1.append(i)


