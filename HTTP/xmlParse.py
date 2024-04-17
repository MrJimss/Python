import urllib.request as urlr
import urllib.parse as urlp 
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =input('Enter location: ')
print('Retrieving', url)

uh = urlr.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print(f"Count: {len(counts)}")

sum=0
for item in counts:
    count=int(item.text)
    sum=sum+count
    
print(f"Sum:{sum}")