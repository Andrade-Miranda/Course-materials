#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:25:41 2018

@author: Gustavo
"""

import random as rad

print (" \t Bienvenidos al Juego de piedra, papel o tijera \n", 
       " \t \t Este juego simula el  famoso juego de \n  \t \t \t Piedra Papel", 
       "y tijera \n \n")

jugador1=rad.randint(1,3)
jugador2=rad.randint(1,3)

frase1="Piedra le gana a tijera"
frase2="Tijera le gana a papel"
frase3="Papel le gana a piedra"
frase4="SON IGUALES"

if jugador1 == jugador2:
    frase=frase4
    ganador = "Empate entre Jugador 1 y Jugador 2"
    if jugador1==1:
        opcjuga1= opcjuga2 = "piedra"
    elif jugador1==2:
        opcjuga1= opcjuga2 = "papel"
    else:
        opcjuga1= opcjuga2= "tijera"
elif jugador1 == 1 and jugador2 ==2:
    frase=frase3
    opcjuga1, opcjuga2 = "piedra", "papel"
    ganador = "Jugador 2 es el ganador"
elif jugador1 == 1 and jugador2 ==3:
    frase=frase1
    opcjuga1, opcjuga2 = "piedra", "tijera"
    ganador = "Jugador 1 es el ganador"
elif jugador1 == 2 and jugador2 ==1:
    frase=frase3
    opcjuga1, opcjuga2 = "papel", "piedra"
    ganador = "Jugador 1 es el ganador"
elif jugador1 == 2 and jugador2 ==3:
    frase=frase2
    opcjuga1, opcjuga2 = "papel", "tijera"
    ganador = "Jugador 2 es el ganador"
elif jugador1 == 3 and jugador2 ==1:
    frase=frase1
    opcjuga1, opcjuga2 = "tijera", "piedra"
    ganador = "Jugador 2 es el ganador"
else:
    frase=frase2
    opcjuga1, opcjuga2 = "tijera", "papel"
    ganador = "Jugador 1 es el ganador"


print("El primer jugador saco %s y el segundo saco %s \n"
      "%s, porque %s" %(opcjuga1,opcjuga2,ganador,frase))
