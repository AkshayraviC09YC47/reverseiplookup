#!usr/bin/env python3
import os
import requests

os.system("clear")

Banner = """.____                  __                 
|    |    ____   ____ |  | ____ ________  
|    |   /  _ \ /  _ \|  |/ /  |  \____ \ 
|    |__(  <_> |  <_> )    <|  |  /  |_> >
|_______ \____/ \____/|__|_ \____/|   __/ 
        \/                 \/     |__|    """

print(Banner)
print("<----------Coded By Copycat---------->")
print("")

url = input("site name: ")
api_url = "http://api.hackertarget.com/reverseiplookup/?q="

def lookup():
	r = requests.get(api_url + url)
	r.raise_for_status()
	print(r.text)
	
lookup()

