
import curses
import time
from os import system, name
import numpy as np
import engine
import carga_cubo
import subprocess, platform


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def draw(pantalla,x,y,p):
    a = 170 * int(y) + int(x)
    pantalla[a] = str(p)
    return(pantalla)
    
    
def borrarPantalla():
    a = [' '] * 170 * 65
    return a

def drawLine(x1, y1, x2, y2 ,p,pantalla):

    a1,a2 = x1,x2
    b1,b2 = y1,y2


    dx = a2-a1
    dy = b2-b1
 
    dx1 = abs(dx)
    dy1 = abs(dy)

    px = 2 * dy1 - dx1
    py = 2 * dx1 - dy1

    xe = 0
    ye = 0

    if (dy1 <= dx1):
        if(dx >= 0):
            x = a1
            y = b1
            xe = a2
        else:
            x = a2
            y = b2
            xe = a1
        
           
        pantalla = draw(pantalla,x,y,p)
        
        while x < xe:
            x = x+1
            if(px < 0):
                px = px + 2 * dy1
             
            else:
                if(dx < 0 and dy <0) or (dx > 0 and dy >0):
                    y = y+1
                else:
                    y = y-1
                px = px + 2 * (dy1 - dx1)
            
            pantalla = draw(pantalla,x,y,p)
    else:
        if(dy >= 0):
            x = a1
            y = b1
            ye =b2
        else:
            x = a2
            y = b2
            ye = b1

        pantalla = draw(pantalla,x,y,p)

        while y < ye:
            y = y+1
            if(py <=0):
                py = py + 2 * dx1
            else:
                if(dx < 0 and dy <0) or (dx > 0 and dy >0):
                    x = x + 1
                else:
                    x = x-1
                py = py + 2 * (dx1 - dy1)
            pantalla = draw(pantalla,x,y,p)




char1 = chr(0x2588)
char2 = chr(0x2593)
char3 = chr(0x2592)
char4 = chr(0x2591)


fps = 1/60

def main():

    pantalla = borrarPantalla()

    fTheta = 0
    matRotZ = engine.matrizCuadrada()
    matRotX = engine.matrizCuadrada()

        
    while True:
        cero = time.time()
        
        
        matRotZ[0][0] = np.cos(fTheta)
        matRotZ[0][1] = np.sin(fTheta)
        matRotZ[1][0] = -np.sin(fTheta)
        matRotZ[1][1] = np.cos(fTheta)
        matRotZ[2][2] = 1
        matRotZ[3][3] = 1

        
        matRotX[0][0] = 1
        matRotX[1][1] = 1#np.cos(fTheta * 0.5)
        matRotX[1][2] = 1#np.sin(fTheta *0.5) 
        matRotX[2][1] = 1#-np.sin(fTheta *0.5)
        matRotX[2][2] = 1#np.cos(fTheta *0.5)
        matRotX[3][3] = 1

        for cara in carga_cubo.caras:
            
            a = cara[1:]

            for i in range(len(a)):
                
                #Selecciono dos pares de puntos que forman una arista(linea)
                x1,x2 = carga_cubo.puntos[a[i]],carga_cubo.puntos[a[i-1]]

                
                #rotar en Z
                p1 = engine.multiplicarMatrizxVector(x1,matRotZ)
                p2 = engine.multiplicarMatrizxVector(x2,matRotZ)

                #rotar en X
                q1 = engine.multiplicarMatrizxVector(p1,matRotX)
                q2 = engine.multiplicarMatrizxVector(p2,matRotX)

                
                w1 = q1
                w2 = q2

                #move dentro de la camara
                
                w1[2] = q1[2]+3.0
                w2[2] = q2[2]+3.0
                
                #Proyeccion 3d -> 2d
                e1 = engine.multiplicarMatrizxVector(w1,engine.mat4x4)
                e2 = engine.multiplicarMatrizxVector(w2,engine.mat4x4)

                #Escalar
                e1[0] += 1.0
                e1[1] += 1.0
                e1[0] *= 0.5 * float(170)                
                e1[1] *= 0.5 * float(65)
                
                
                e2[0] += 1.0
                e2[1] += 1.0
                e2[0] *= 0.5 * float(170)
                e2[1] *= 0.5 * float(65)

                drawLine(e1[0],e1[1],e2[0],e2[1],char1,pantalla)    
            dibujo = "".join(pantalla)
            print(dibujo)

            hola = "hola"
            
            
        
        dif = time.time() - cero
        sinf = fps-dif

        sinf = 0 if sinf<0 else sinf
        time.sleep(sinf)

        #stdscr.addstr(0,0,str(sinf))
        #drawLine(3,17,15,3,char1,stdscr)
        
        
        fTheta += 1 * dif
        clear()
        pantalla = borrarPantalla()

        #break

    return 0



main()

