import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count=int(input("Enter count:"))

position=int(input("Enter position:"))
tags = soup('a')
print(f"Retrieving:{url}")
while count > 0:
     links=[]
     for tag in tags:
          links.append(tag.get('href', None))
     url=links[position-1]
     html = urllib.request.urlopen(url, context=ctx).read()
     soup = BeautifulSoup(html, 'html.parser')
     tags = soup('a')
     print(f"Retrieving:{url}")
     count=count-1
