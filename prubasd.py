name = input("Enter file:")
if len(name) < 1 : name = "mails.txt"
handle = open(name)

horas={}
for i in handle:
   if i.startswith("From "):
       hora = i.split()[5].split(':')[0]
       horas[hora] = horas.get(hora,0)+1

print(sorted((v,k) for v,k in horas.items()))

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x) 

import re

x = 'My 2 favorite numbers are 19 and 42'
y =  re.findall('[0-9]+',x)
print(y)