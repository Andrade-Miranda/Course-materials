#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:02:22 2018
Ejercicios adicionales encontrados en
https://github.com/pythonschool/Basics/tree/master/1%20-%20Variables/Additional%20Exercises
@author: Gustavo
"""

## codigo que presenta un formato diferente para la impresión
# y códigos extras

# Suma tres números
print("Number Addition")
print("This program asks for three numbers and then outputs the total")
print()
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
num3 = int(input("Please enter a third number: "))
print()
ans = num1 + num2 + num3
print("The total of {0} + {1} + {2} is {3}.".format(num1,num2,num3,ans))


# Multiplica y divide
print("Number Multiply and Divsion")
print("This program asks for three numbers, adds the first two together")
print("then divides the total by the third number before displaying the answer")
print()
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
num3 = int(input("Please enter a third number: "))
print()
ans = (num1 + num2) / num3
print("The total of ({0} + {1}) / {2} is {3}.".format(num1,num2,num3,ans))





#Pedir por teclado al usuario que ingrese tres palabras separadas por espacio y 
#a partir de estas tres palabras crear una primera lista (lista 1).

#a) calcule el tamaño total de datos de la lista 1
#b) Elimine los datos en la posicion 1 y 2 de la lista
#c) Ingrese por teclado una lista 2 con tres elementos
#d) sume a la lista 1 los valores en la lista 2
#e) calcule el valor máximo de la nueva lista 1
#f) calcule el valor minimo de la nueva lista 1


# primera forma
cadena=input("ingrese los datos de la lista 1: ")

eleList1=cadena[:cadena.find(" ")]
eleList2=cadena[cadena.find(" ")+1:cadena.find(" ",cadena.find(" ")+1)]
eleList3=cadena[cadena.find(" ",cadena.find(" ")+1)+1:]

lista1=[eleList1,eleList2,eleList3]
print(len(lista1))
del lista1[1:]

cadena2=input("ingrese los datos de la lista 2: ")
eleList1_2=cadena2[:cadena2.find(" ")]
eleList2_2=cadena2[cadena2.find(" ")+1:cadena2.find(" ",cadena2.find(" ")+1)]
eleList3_2=cadena2[cadena2.find(" ",cadena2.find(" ")+1)+1:]
lista2=[eleList1_2,eleList2_2,eleList3_2]

lista1+=lista2
print(lista1)

print(max(lista1))
print(min(lista1))

# segunda forma
cadena1=input("ingrese los datos de la lista 1: ")
lista1=cadena1.split()
print(len(lista1))
del lista1[1:3]
cadena2=input("ingrese los datos de la lista 2: ")
lista2=cadena2.split()
lista1+=lista2
print(lista1)

print(max(lista1))
print(min(lista1))

 

#programa que calcula area de circulo o de triangulo    
import math
print("Este programa va a realizar el calculo \n de las areas de un triangulo o de un circulo")
print("Ingrese el numero 1 si quiere calcular el area de un circulo \n o ingrese el numero 2 si quiere calcular el area de un triangulo" )

opcion=int(input("Ingrese la opcion: "))
area=0
if opcion==1:
    radio=float(input("Ingrese el radio: "))
    area=math.pi*(radio**2)
    print("Area es igual a: %.2f" % (area))
elif opcion==2:
    altura=float(input("Ingrese la altura: "))
    base=float(input("Ingrese la base: "))
    area= (base*altura)/2
    print("Area es igual a: %.2f" % (area))
else:
    print("ERROR opcion incorrecta")
    
    


#programa que calcula gasto total dependiendo de articulo

n=int(input("Ingrese el numero de articulos comprados: "))

costotal=0

if n<10:
    costotal=12*n
    print("el numero es menor que 10")
elif (n>=10 and n<=99):
    costotal= 10*n
    print("el numero esta entre 10 y 99")
else:
    costotal= 7*n
print(costotal)   




# Ejemplo de lazo infinito
i = 1 
while i <= 10: 
    print(i, end=" ")



# ejemplo de lazo infinito    
i = 1 
while i > 0: 
    print(i, end=" ") 
    i += 1

  

#Escriba un programa que pregunte primero si se quiere calcular el área de un 
#triángulo o la de un círculo. Si se contesta que se quiere calcular el área 
#de un triángulo, el programa tiene que pedir entonces la base y la altura y 
#escribir el área. Si se contesta que se quiere calcular el área de un círculo, 
#el programa tiene que pedir entonces el radio y escribir el área. Si se ingresa
# una opcion invalida repetir hasta que la opcion sea valida
#Se recuerda que el área de un triángulo es base por altura dividido por 2 y 
#que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
   
import math
print("Este programa va a realizar el calculo \n de las areas de un triangulo o de un circulo")
print("Ingrese el numero 1 si quiere calcular el area de un circulo \n o ingrese el numero 2 si quiere calcular el area de un triangulo" )

opcion=int(input("Ingrese la opcion: "))
area=0

while (opcion!=1 and opcion!=2):
      print ("Opcion Inválida")
      opcion=int(input("Ingrese la opcion: "))
    
if opcion==1:
   radio=float(input("Ingrese el radio: "))
   area=math.pi*(radio**2)
   print("Area es igual a: %.2f" % (area))
else: 
     altura=float(input("Ingrese la altura: "))
     base=float(input("Ingrese la base: "))
     area= (base*altura)/2
     print("Area es igual a: %.2f" % (area))
    

# Escribir un programa que imprima los numeros
for j in range(4):
	print (j)



# Escribir un programa que cuente el número de letras en una palabra
palabra=input("Ingrese una palabra:")
numero_letra=0

for letra in palabra:
    print("La letra %d es %s" %(numero_letra,letra))
    numero_letra+=1
    
print("El numero de letras en %s es %d" %(palabra,numero_letra))



#Escribir una función que pida una palabra y  
#devuelva el numero de vocales

## primera forma
palabra=input("Ingrese una palabra: ")
numero_vocales=0
numero_consonantes=0

for letra in palabra:
    if (letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u' or letra=='A' or 
        letra=='E' or letra=='I' or letra=='O' or letra=='U'): 
        numero_vocales+=1
    else:
        numero_consonantes+=1
print ("El numero de consonantes es %d y el de vocales es %d" %(numero_consonantes,numero_vocales))
        
    
#segunda forma
palabra=input("Ingrese una palabra: ")
numero_vocales=0
numero_consonantes=0
vocal=['a','e','i','o','u']
for letra in palabra:
    if letra in 'aeiouAEIOU': 
        numero_vocales+=1
    else:
        numero_consonantes+=1
print ("El numero de consonantes es %d y el de vocales es %d" %(numero_consonantes,numero_vocales))
        


    
## Definir un histograma procedimiento() que tome una lista de números enteros 
##e imprima un histograma en la pantalla. Ejemplo: procedimiento
##([4, 9, 7]) debería imprimir lo siguiente:

# ****
# *********
# *******

cadena1=input("ingrese la lista de numero enteros:  ")
lista1=cadena1.split()

for elem in lista1:
    for rep in range(int(elem)):
        print("*",end="")
    print('\n')
    


cadena1=input("ingrese la lista de numero enteros:  ")
lista1=cadena1.split()
for elem in lista1:
    print("*"*int(elem))
       





















