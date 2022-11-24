#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:43:49 2018

@author: Gustavo
"""
# Escriba un progama que pida una cadena de caracteres. El programa deberá mostrar por pantalla lo siguiente:
#El número total de caracteres
#La cadena repetida 5 veces separada por un enter
#Los tres primeros caracteres de la cadena
#Los tres últimos caracteres de la cadena
#La cadena escrito al reves (Hola  aloH)
#La cadena en mayúsculas
#La cadena con cada letra “a” remplazada por una “e”

frase=input("Ingrese la frase: ")
print("\nEl numero total de caracteres es: %d\n" %(len(frase)))
print("La cadena repetida 5 veces separada por un enter es: \n%s" %((frase + "\n") *5))
print("Los tres primeros caracteres de la cadena: %s\n" %(frase[:3]))
print("Los tres últimos caracteres de la cadena: %s\n" %(frase[-3:]))
print("La cadena escrito al reves: %s\n" %(frase[::-1]))
print("La cadena en mayúsculas: %s\n" %(frase.upper()))
print("La cadena con cada letra \"a\" remplazada por una \"e\": %s\n" %(frase.replace("a","e")))


#Escriba un progama que pida una cadena de caracteres de 6 letras, 
#luego muestre cada letra de la cadena escrita doble y separada por un tab.
#Por ejemplo: s=Hola

frase = input("Ingrese la frase: ")
doble=""
for x in range(0,(len(frase))):
    doble+=(frase[x]*2) + "\t" 

print(doble.upper())
    


#Escriba un programa en el que pida 3 cadenas de caracteres: una materia, 
#un adjetivo y una actividad. Deberámostrar por pantalla el siguiente párrafo 
#con el siguiente formato (Utilizar un sólo print). Por ejemplo:

materia=input("Ingrese una materia:  ")
adjetivo=input("Ingrese una adjetivo:  ")
actividad=input("Ingrese una actividad:  ")
print("La clase de %s fue muy %s hoy.\nHemos aprendido como %s hoy en clases.\nNo puedo esperar a la clase del Lunes" %(materia,adjetivo,actividad))


#Escriba un programa que pida por teclado la hora en formato hh:mm:ss y 
#convierta todo a segundos.

hora_completa=input("Ingrese fecha completa en el formato hh:mm:ss :  ")
hora=int(hora_completa[:hora_completa.find(":")])*3600
minutos= int(hora_completa[hora_completa.find(":")+1:hora_completa.find(":",hora_completa.find(":")+1)])*60
segundos = int(hora_completa[(hora_completa.find(":",hora_completa.find(":")+1))+1:])
print("El valor en segundos es: %d " %(hora+minutos+segundos))


#Escriba un programa que pida por teclado los segundos (mas de 3600) y muestre 
#por pantalla la hora en formato hh:mm:ss

segundos=input("Ingrese tiempo en segundos: ")
horas=int(segundos)//3600
minutos=(int(segundos)%3600)//60
segundos=(int(segundos)%3600)%60
print("La hora es \t %d:%d:%d " %(horas,minutos,segundos))

#Escriba un programa en el que genere un número aleatorio entre 1 y 50 y otro 
#número aletorio entre 2 y 5. Muestre ambos números y la multiplicación de ellos

import random as rd

num1=rd.randint(1,50)
num2=rd.randint(2,5)
multiplicacion=num1*num2
print("El primer número es %d y el segundo es %d, su multiplicación %dX%d es: %d" %(num1,num2,num1,num2,multiplicacion))


#Escriba un programa que genere un número decimal entre 1 y 25  y muestre por 
#pantalla dicho número con 2 decimales.

import random as rd
num=rd.randint(1,25)+rd.random()
print("El número es %.2f" %(num))


#En cálculo la derivada de x^4 es 4x^3, la derivada de x^5 es 5x^4. 
#Escriba un programa que permita el ingreso de una ecuación y muestre por 
#pantalla la derivada de la misma.
import sympy as sp
sp.init_printing()

f=input("Ingresar la función:  ")
x=sp.Symbol('x')
f_int=sp.integrate(f)
f_deriv=sp.diff(f,x)
print("La integral es: ",f_int)
print("La derivada es: ",f_deriv)
f_int,f_deriv

#otra forma 
f=input("Ingresar la función:  ")
derivada=f[2]+f[0]+f[1]+str(int(f[2])-1)










    