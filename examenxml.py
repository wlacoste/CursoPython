import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = str(input('Enter URL-'))
if address == '':
    address = ' http://py4e-data.dr-chuck.net/comments_1047569.xml'

fhand = urllib.request.urlopen(address ,context=ctx)

data = fhand.read()
tree = ET.fromstring(data)
#print(data)
'''
for child in tree:
    for childa in child:
        for childe in childa:
            print(childe.tag,childe.attrib)
'''
cuenta = 0
suma = 0
for child in tree.findall('comments/comment'):
    
    cuenta +=1
    suma = suma + int(child[1].text)
    print('cuenta',child[1].text)

    print('suma  ',suma)
       # print(child[1].text)

print('La cuenta es',cuenta)
print('La suma es', suma)
#print(aba)