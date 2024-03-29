#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import random
IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
words = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente ara�a cig�e�a cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()
 
def obtenerPalabraAlAzar(listaDePalabras):
    # Esta funci�n devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]
 
def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()
 
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
 
    espaciosVac�os = '_' * len(palabraSecreta)
 
    for i in range(len(palabraSecreta)): # completar los espacios vac�os con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVac�os = espaciosVac�os[:i] + palabraSecreta[i] + espaciosVac�os[i+1:]
 
    for letra in espaciosVac�os: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()
 
def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado s�lo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmn�opqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento
 
def jugarDeNuevo():
    # Esta funci�n devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('�Quieres jugar de nuevo? (s� o no)')
    return input().lower().startswith('s')
 
print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(words)
juegoTerminado = False
 
while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
 
    # Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
 
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
 
        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('�S�! �La palabra secreta es "' + palabraSecreta + '"! �Has ganado!')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento
 
        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('�Te has quedado sin intentos!\nDespu�s de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True
 
    # Preguntar al jugador si quiere volver a jugar (pero s�lo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(words)
        else:
            break