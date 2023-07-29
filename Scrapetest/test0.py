#!/usr/bin/python3
import requests

r = requests.get("http://www.ecclesiadei.org/index.html")

print(r)

print(r.content)

