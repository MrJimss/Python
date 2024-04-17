import urllib.request, urllib.parse
<<<<<<< HEAD
import json, ssl
=======
import json,ssl
>>>>>>> origin/HEAD

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
     address = input('Enter location: ')
     if len(address) < 1: break

     address = address.strip()
     parms = dict()
     parms['q'] = address

     url = serviceurl + urllib.parse.urlencode(parms)

     print('Retrieving', url)
     uh = urllib.request.urlopen(url, context=ctx)
     data = uh.read().decode()
     print('Retrieved', len(data), 'characters') #, data[:20].replace('\n', ' ')

     js = json.loads(data)
<<<<<<< HEAD
     l=js['features'][0]
     print(l['properties']['plus_code'])
=======
     print(len(js))
     
#     lat = js['features'][0]['properties']['lat']
#     lon = js['features'][0]['properties']['lon']
#     print('lat', lat, 'lon', lon)
#     location = js['features'][0]['properties']['formatted']
#     print(location)
>>>>>>> origin/HEAD

