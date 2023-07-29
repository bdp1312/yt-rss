#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup

source=sys.argv[1]
#r = requests.get("http://www.youtube.com/@linuxfemboy")
r = requests.get(source)
soup=BeautifulSoup(r.content, "html.parser")
retval=soup.find(title="RSS")
print(retval['href'])