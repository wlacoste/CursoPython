import urllib.request, urllib.parse,urllib.error
import json

serviceurl = ' http://py4e-data.dr-chuck.net/comments_1047570.json'




url = serviceurl

print('Retrieving',url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('retrieved', len(data),'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure to retrieve ====')
    print(data)

contadorComment = 0
for i in js["comments"]:
    contadorComment += i["count"]
print("contador comentario", contadorComment)