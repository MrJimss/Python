from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
sum=0
count=0
for tag in tags:
     if tag.contents[0] is not None:
        count=count+1
     sum = sum + int(tag.contents[0])
print(f"Count:{count}")
print(f"Sum:{sum}")