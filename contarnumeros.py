import re
name = input("Enter file:")
if len(name) < 1 : name = "mails2.txt"
handle = open(name)

lista_num = []
for i in handle:
    numeros = re.findall('[0-9]+',i)
    if len(numeros)>0:
        for a in numeros:

            lista_num.append(int(a))

print(sum(lista_num))

print( sum( [ int(a) for a in re.findall('[0-9]+',open("mails2.txt").read()) ] ) )

GET http://data.pr4e.org/romeo.txt HTTP/1.0