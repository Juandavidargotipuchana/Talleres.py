import os
from random import randint,uniform,random



###############################

jugadores = randint(1,6)
n = randint(1,3)

############################
os.system("clear")

  
print("Bienvenidos la cantidad de jugadores es: ", jugadores)

camino = 1 
while jugadores < 2  or jugadores > 5 :
        
    jugadores = randint(1,3)
    print("Lo siento, la cantidad de jugadores es invalida : ", jugadores)
else :
    os.system("clear")
    print("La cantidad de jugadores es : ", jugadores)
    print("Bienvenido al juego")

if n == 1 :
    print("1. Nivel Basico (Tablero de 20 posiciones)")
    camino = 20 
elif n == 2:
    print("2. Nivel Intermedio (Tablero de 30 posiciones)")
    camino = 30 
else:
    print("3. Nivel Intermedio (Tablero de 50 posiciones)")
    camino = 50

dado1 = []
dado2 = []
i = 1
j = 1

while i <= camino :    
    while j <= jugadores:
        print( "jugador ", j)
        if j == 1:
            numda= randint(1,6)
            numda2= randint(1,6)
            dado1.append(numda)
            dado2.append(numda2)
            r1 = dado2[0]
            r2 = dado1[0]
            resultado = r1 + r2
            camino1 = np.arange(1,resultado)
            print(camino1)     
        elif j == 2:
            numda= randint(1,6)
            numda2= randint(1,6)
            dado1.append(numda)
            dado2.append(numda2)
            resultado = dado1 + dado2 
            camino2 = np.arange(1,resultado) 
            print(camino2)
        else:
            numda= randint(1,6)
            numda2= randint(1,6)
            dado1.append(numda)
            dado2.append(numda2)
            resultado = dado1 + dado2
            camino3 = np.arange(1,resultado)
            print(camino3)
        
            

    


    





 
