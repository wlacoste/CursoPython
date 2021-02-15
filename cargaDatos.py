import numpy as np
import pandas as pd 

import os

dirloc = r'C:\Users\Usuario\Desktop\PythonCurso\DatosSole'

sumaValores = 0
contadorReg = 0
for file in os.scandir(dirloc):
    if file.path.endswith(".txt") and file.path.startswith(dirloc+'\dato') and file.is_file():
        a = pd.read_csv(file,sep=' ',header=None)
        #iterar por los registros
        for data in a.iterrows():
            print(data[1])
            '''
        if checkearSiSuma(registro):
            sumaValores = sumaValores + valor
            contadorReg = contadorReg + 1
            '''
        #print(a)