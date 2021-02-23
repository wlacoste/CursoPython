import numpy as np
import math
import curses

# Matriz de Proyeccion
mat4x4 = np.zeros((4,4))

fNear = 0.1
fFar = 1000.0
fFov = 90.0
# ! poner mejor el aspect ratio
fAspectRatio = 1.1

fFovRad = 1.0 / math.tan(fFov * 0.5 / 180.0 * 3.14159)

mat4x4[0][0] = fAspectRatio * fFovRad
mat4x4[1][1] = fFovRad
mat4x4[2][2] = fFar / (fFar - fNear)
mat4x4[3][2] = (-fFar * fNear) / (fFar - fNear)
mat4x4[2][3] = 1.0
mat4x4[3][3] = 0.0

# parametro a: vector en 3 dimensiones. 
# parametro b: matriz de proyeccion
def multiplicarMatrizxVector(a, b):

    m = [0.0,0.0,0.0]

    m[0] = a[0] * b[0][0] + a[1] * b[1][0] + a[2] * b[2][0] + b[3][0]
    m[1] = a[1] * b[0][1] + a[1] * b[1][1] + a[2] * b[2][1] + b[3][1]
    m[2] = a[2] * b[0][2] + a[1] * b[1][2] + a[2] * b[2][2] + b[3][2]

    w = a[0] * b[0][3] + a[1] * b[1][3] + a[2] * b[2][3] + b[3][3]

    if(w != 0.0):
        m[0] /= w
        m[1] /= w
        m[2] /= w
    
    return(m)




def matrizCuadrada():
    return np.zeros((4,4))






