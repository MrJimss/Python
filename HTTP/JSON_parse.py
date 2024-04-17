import urllib.request as urlr
import urllib.parse as urlp 
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =input('Enter location: ')
if len(url) ==0:
     url = "http://py4e-data.dr-chuck.net/comments_1761777.json"
print('Retrieving', url)

uh = urlr.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('User count:', len(info['comments']))

sum =0
for item in info['comments']:
     count = int(item['count'])
     sum += count
print("Sum:",sum)