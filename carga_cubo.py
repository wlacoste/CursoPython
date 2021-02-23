import csv
import io
from pathlib import Path

#data_folder = Path("Objetos3d/")
data_folder = Path("Objetos/")


file_path = data_folder / "cubo3.ply"

with io.open("Objetos/cubo3.ply", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    line_count = 0
    puntos = []
    caras = []
    nro_puntos = 0
    for row in csv_reader:
        if(line_count == 3 ):
            nro_puntos = int(row[2])

        if(line_count >= 10):
            linea =[]
            if(line_count < 10 + nro_puntos):                
                for valor in row:
                    linea.append(float(valor))
                puntos.append(linea)
            else:
                for valor in row:
                    linea.append(int(valor))
                caras.append(linea)




       
        line_count += 1

