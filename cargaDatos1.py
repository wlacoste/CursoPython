import numpy as np
import pandas as pd 

import os

#dirloc = [r"C:\Users\Usuario\Desktop\PythonCurso\DatosSole",]

#"/home/sol/charge_mut/graficos_perfiles"
dirloc = input('Ingrese la ruta')
c = []
d = []
for archivo in dirloc:
    for file in os.scandir(dirloc):
        if file.path.endswith(".dat") and file.path.startswith(dirloc+'\filtrados') and file.is_file():
            a = np.loadtxt(file)      #iterar por los registros        
        for iter in a:
                c.append(iter[0])
                d.append(iter[1])

print(c,d)
'''
print('Promedio col 0',np.average(c))
print('Desviacion col 0',np.std(c))

print('Promedio col 1',np.average(d))
print('Desviacion col 1',np.std(d))
'''