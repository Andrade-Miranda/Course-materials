#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:48:31 2018

@author: Gustavo
"""

#Asuma que la lista ​palabras ​​contiene un número determinado de palabras que se 
#usarán para al juego “Conocimiento” que le han pedido implementar basado en la siguiente mecánica:

#1. La computadora selecciona aleatoriamente una palabra con la que se jugará de 
#la lista ​palabras​​. Esta palabra deberá ser almacenada en la variable ​secreto​​.
#2. La computadora escogerá una ​consonante​ de ​secreto​​ aleatoriamente y, asumiendo 
#que ​secreto​​ es “ESPOL” y la letra seleccionada es la ‘s’, mostrará por pantalla lo siguiente:
#-S---

#1. El usuario tendrá ​2 x (el tamaño de la palabra almacenada en ​secreto​​)​ turnos, 
#para adivinar el resto de la palabra.
#3. El usuario puede ingresar letras mayúsculas o minúsculas y esto no debe hacer 
#diferencia en el juego.
#4. Si la letra ingresada pertenece a la palabra en ​secreto​​, se mostrará por pantalla 
#la nueva letra adivinada en la posición que le corresponde.

import random as rd
palabras=["hola", "", "manuel", "josesito", "murcielaguito", "pereza", "manzana","perder"]
secreto=rd.choice(palabras)
secreto=list(secreto)

letra="e"
list_rell=[]

while letra in 'aeiouAEIOU':
    letra=rd.choice(secreto)


for elem in secreto:
    if elem==letra:
        list_rell=list_rell+[letra]
    else:
        list_rell=list_rell+["_"]
str_rell = ' '.join(list_rell)
print(str_rell)

estado="Perdistes"

for cont in range ((2*len(secreto))-1):
    n_letra=input("Ingrese nueva letra: ")
    if (n_letra.lower() in secreto):
        ind=[i for i, n in enumerate(secreto) if n == n_letra.lower()]
        for j in ind:
            list_rell[j]= n_letra.lower()
        str_rell = ' '.join(list_rell)
        print(str_rell)
    else:
        print(str_rell)
    
    if "_" not in str_rell:
        estado="Ganastes"
        break

if estado=="Ganastes":
    print(estado)
else:
    print(estado) 
    print("La palabra era: "+''.join(secreto))
    
    
     
#Escriba un programa que grafique un triangulo rectángulo invertido formado por 
#el caracter enviado como parámetro.  La base y la altura del mismo dependerá 
#del número de líneas. Por ejemplo:  3 lineas, caracter a 

#       aaa
#        aa
#         a

linea=int(input("Ingrese numero de lineas: "))
caracter=input("Ingrese caracter: ")

for i in range(linea+1):
    num=linea-i
    print((" "*i)+(caracter*num))



#Escribir un programa que convierta un valor dado en grados 
#Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: 
#F = 9/5 * C + 32.











#Escribir un programa que imprima todos los números pares entre dos números 
#que se le pidan al usuario.


num1=int(input("Ingrese numero uno: "))
num2=int(input("Ingrese numero dos: "))

for i in range(num1+1,num2-1):
    if i%2==0:
        print(i)



#Un número perfecto es aquel que es igual a la suma de todos sus divisores, 
#con excepción del mismo.
#Ejemplo:
# 6 es perfecto porque, 
#   sus divisores son: 1, 2, 3 (6 no se considera).
#   1+2+3=6
#Escriba una fucnion que te diga si un nuemro ingresado es perfecto o no


numero=int(input("Ingrese un número: "))

cont=0
for i in range(1,numero):
    if numero%i==0:
       cont+=i

if cont==numero:
   print('Es perfecto')
else:
   print('NO es perfecto')

 
      

#En el Fútbol el lanzamiento de penales intervienen el jugador que patea y el 
#arquero que tapa el penal.
#Este juego consiste en 5 lanzamientos por parte de los jugadores que patean el
#balón, los cuales pueden decidir lanzar en cualquiera de las seis secciones 
#del arco (1: arriba a la derecha, 2: arriba al centro, 3: arriba a la izquierda, 
#4 abajo a la izquierda, 5: abajo al centro, 6: abajo a la derecha).
#En cada lanzamiento, el arquero decide donde ubicarse para atajar el tiro y no 
#tiene oportunidad de cubrir otra sección, si éste coincide con la ubicación 
#donde disparó el jugador, entonces el lanzamiento fue atajado o fallado, caso 
#contrario se marcó un GOL
#Escriba un algoritmo que simule un juego de 5 lanzamientos de penales, en donde 
#la sección del arco donde cada jugador lanza es decidido por el usuario y la 
#sección cubierta por el arquero es simulado por el computador (aleatoria).
#Al final presente la siguiente información:

#Cantidad de goles conseguidos.
#Cantidad de penales fallados.
#La cantidad de goles realizados en la parte derecha, central e izquierda del arco.
#La ubicación del arco (derecha, centro o izquierda) por donde ingresaron más goles. 
#Suponga que existe una sola.
#La ubicación del arco (derecha, centro o izquierda) por donde no ingresaron goles. 
#Suponga que existe una sola.













#El índice de masa corporal (IMC) es el cociente entre el peso de una persona en 
#Kg dividido para su estatura al cuadrado en metros.
#La Organización Mundial de la Salud OMS, clasifica a las personas según su IMC
#de la siguiente forma:
#IMC	                            Tipo IMC
#Menos de 17	                      1. Infrapeso
#más de 17 hasta 18	             2. Bajo Peso
#mas de 18 hasta 25	             3. Peso Normal
#mas de 25 hasta 30	             4. Obesidad tipo I
#más de 30 hasta 35	             5. Obesidad tipo II
#mas de 35 hasta 40	             6. Obesidad tipo III
#mas de 40	                      7. Obesidad mórbida

#Escriba una programa  que reciba el peso y estatura de 
#una persona para dar como resultado el tipo de masa corporal 

#Ejemplo:
#peso=75 Kg; 
#estatura=1,70 m ; 
#75/(1,70*1,70)=25,95 equivale a tipo 4.







#Ingrese tres números correspondientes a un conjunto y tres números 
#correspondientes a otro conjunto. Muestre los números que corresponden a la 
#intersección de los dos conjuntos.







#Dado un número entero positivo, determine la suma de sus dígitos.

numero=input("Ingrese un numero entero positivo: " )
acum=0
for car in numero:
    acum=int(car)+acum
    
print("la suma es %d" %(acum))   
    

numero=int(input("Ingrese un numero entero positivo: " ))
acum=0
nuevo_num=numero

for i in range(len(str(numero))-1):
     digito=nuevo_num//10**(len(str(numero))-i-1)
     nuevo_num=nuevo_num%10**(len(str(numero))-i-1)
     acum=acum+digito
acum=acum+nuevo_num
          
print("la suma es %d" %(acum))     
     
    



#Encuentre todos los números naturales entre 1 y 100 tales que la suma de sus 
#dígitos de como resultado un numero primo.
#Ejemplo : 34: 3+4 = 7 debe mostrar el 34 pues 7 es un número primo


for i in range(100):
    numero_str=str(i)
    for car in numero_str:
            acum=int(car)+acum




#Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir 
#con los siguientes criterios de aceptación:

#La contraseña debe contener un mínimo de 8 caracteres.
#Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 
#1 carácter no alfanumérico.
#La contraseña no puede contener espacios en blanco.
#Contraseña válida, retorna True.
#Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".







#Generar un valor aleatorio entre 1 y 1000. Luego imprimir un mensaje indicando 
#cuantos dígitos tiene.







#Generar un valor aleatorio entre -10 y 10. Mostrar un mensaje si el valor 
#generado es negativo, nulo o positivo.






#Escriba un programa que pida dos números enteros y que calcule su división, 
#escribiendo si la división es exacta o no.







#Escriba un programa que pida dos números y que conteste cuál es el menor y cuál 
#el mayor o que escriba que son iguales.








#Escriba un programa que pida dos números enteros y que escriba si el mayor es 
#múltiplo del menor.





#Dado un entero positivo n, se desea verificar que la suma de los primeros n números
#impares es igual a n2
#Ej. n=5: 1+3+5+7+9 = 52





#Calcule un valor aproximado para la constante π usando la siguiente expresión: 
#π/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 ...
#La cantidad de términos es un dato que debe ser ingresado al inicio del algoritmo.







#Un modelo de crecimiento poblacional está dado por f(t) = kt + 2e0.1t, siendo k 
#una constante que debe determinarse y t es tiempo en años. Se conoce que 
#f(10)=50. Determine la población en el año 25








#Lea la cantidad de Kw que ha consumido una familia y el precio por Kw. 
#Si la cantidad es mayor a 700, incremente el precio en 5% para el exceso de 
#Kw sobre 700. Muestre el valor total a pagar.







#Dado un entero positivo encuentre sus factores primos
#Los factores primos son los números primos que conforman el mayor conjunto de 
#divisores enteros positivos de un número, tales que su producto es igual al 
#número dado.
#Ejemplo: si el dato es 120, sus factores primos son: 2, 2, 2, 3, 5 
#pues su producto es 120







#Escriba un programa que, dada dos listas de 4 elementos, 
#devuelva una lista con las suma de cada uno de los elementos (suma de vectores).


from operator import add

list1=[3,4,5,6]
list2=[4,6,6,7]
list3=[2,1,1,4]
suma1=list( map(add, list1, list2) )


suma=[sum(J) for J in zip(list1, list2)]


suma=list(range(len(list1)))
for i in range(len(list1)):
    suma[i]=list1[i]+list2[i]
    
suma=[]
for i in range(len(list1)):
    suma=suma+[list1[i]+list2[i]]


#Escribir un programa que elimine los elementos repetidos de una lista

lista1=[1,2,2,3,4,5,5,8,4]
for elem in lista1:
    conteo=lista1.count(elem)
    if conteo>1:
       for i in range(conteo):
           lista1.remove(elem)
           
lista1=[1,2,2,3,4,5,5,8,4]
lista2=[]
for elem in lista1:
    conteo=lista1.count(elem)
    if conteo>1:
        for i in range(conteo):
           lista1.remove(elem)
        lista2.append(elem) 
       
       

       
       
#comparar dos listas      
A=[1,2,3,4,5,6,7,8]
B=[8,4,10,3,11,20,2,9,16,30]
iguales=[]   

for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            iguales.append(B[j])
print(iguales)
            
       
#Escribir un programa en python que permita el ingreso de dos parámetros. 
#Primer parámetro: una cantidad de números enteros positivos hasta que el 
#usuario escriba -1. Segundo parámetro: un número.  Al finalizar el programa 
#deberá mostrar los números ingresados en el primer parámetro mayores al segundo
#parámetro. Por ejemplo: 

lista_param=[]
mayor=[]
while (1):
    primer=int(input("Ingrese primer numero: "))
    if primer==-1:
       break
    else:
       lista_param.append(primer)

segundo=int(input("Ingrese segundo numero: "))
for i in range(len(lista_param)):
    if lista_param[i]>segundo:
            mayor.append(lista_param[i])
print(mayor)
    
#Usted elaborará un programa que permita el ingreso de 15 números 
#(positivos y negativos). Al finalizar deberá mostrar por pantalla tres listas:
#Lista de números ingresados por el usuario.
#Lista de números positivos, y,
#Lista de números negativos. 

numeros=[]
positivos=[]
negativos=[]
for i in range(15):
    primer=int(input("Ingrese primer numero: "))
    numeros.append(primer)
    if primer>=0:
        positivos.append(primer)
    else:
        negativos.append(primer)
    
print("su lista es %s" %(numeros))      
       
       
       


#EXTRAS
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort(reverse=True)
lista=['pepe', 'juanito', 'menganito', "sutanito"]
lista.sort(reverse=True)

#crear string con los elementos de la lista
numeros = ['1','2','3','4','5','6','7']
frase=" ".join(numeros)
      
     
#enumerate
choices = ['pizza', 'pasta', 'salad', 'nachos','pizza','hamburguesa','pizza']
list(enumerate(choices))
for index, item in enumerate(choices):
    print (index, item)
    
ind=[index for index, n in enumerate(choices) if n == 'pizza']
print(ind)      
       
       
       
       
       
##ejercicio examen


################## ya
A=[1,2,3,4,5,6]    
B=[2,3,2,2,5,3]

for i in range(len(A)):
   numero=str(A[i])*B[i]
   print(numero)
#solucion
#11
#222
#33
#44
#55555
#666



########################### ya
palabra ='aabbbccdefggh'
final=''         
actual=''
for letra in palabra:
    if letra != actual:
        final = final + letra
        actual=letra
print(final)
#solucion 
#abcdefgh

######################### ya
secreto='fundamentos'
letra="n"
list_rell=[]
for elem in secreto:
    if elem==letra:
        list_rell=list_rell+[letra]
    else:
        list_rell=list_rell+["_"]
str_rell = ' '.join(list_rell)
print(str_rell)
#solucion
# _ _ n _ _ _ _ n _ _ _



########################## ya
numero="7654"
acum=0
for car in numero:
    acum=int(car)+acum
print(acum)
#solucion
#22


######################### ya
frase = "La materia mas facil del semestre es fundamentos"
palabras = frase.split()
longuitud = []
for palabra in palabras:
      if palabra not in "LalaLoloLele":
          longuitud.append(len(palabra))
print(palabras)
print(longuitud)
#solucion
#['la', 'materia', 'mas', 'facil', 'del', 'semestre', 'es', 'fundamentos']
#[7, 3, 5, 3, 8, 2, 11]



###################### ya
num=5
for i in range(num):
    num1=num-i
    print((" "*num1)+('a'*((i*2)+1)))
#solucion
#     a
#    aaa
#   aaaaa
#  aaaaaaa
# aaaaaaaaa


######################## ya
numero=10
ullman=numero
print(ullman, end=" ")
while ullman > 1:
      if ullman%2==0:
          ullman=ullman//2
      else:
          ullman=(ullman*3)+1
      print(ullman, end=" ")
#solucion
#  10 5 16 8 4 2 1      

######################### ya
for i in range(1, 5):
    print(str(i) * i)    
#solucion 
#1
#22
#333
#4444   


########################### ya
numero='153'
acum=0
n=len(numero)
for car in numero:
    acum=((int(car))**n)
    print(acum, end=' ')
###solucion
# 1 125 27




############################
A=[2,3,4,5]
B=[8,4,10,3,4]
lista=[]   
for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            lista.append(B[j])
print(lista)
#solucion
#[3,4,4]


##########################
n=15
for d in range (1,n+1):
    if n%d==0:
        print(d,end=' ')
#solucion
#1
#2      
#3
#4
#5
#10
#20



###########
palabra="Hola examen"
b=palabra[:palabra.find(" ")]+"_"+palabra[palabra.find(" ")+1:]
print(b)
#solucion
#Hola_examen

############




########### ya
#a=[2,3,1,4]
#b=a[    ]+a[2]
#print(a[   ])
#4
# 0 b a 4 1

############



###########
#a=[2,0,1,4]
#b=a[      ]-a[2]
#print(a[    ])
#0
# 0 b a 4 3

############









## Escriba un programa que evalua un numero entero positivo
## ingresado por el usuario y diga si es factoriano o no
#Ej:
	#145 = 1! + 4! + 5!
    #1+(4x3x2x1)+(5x4x3x2x1)=
    # ES FACTORIANO
##solucion  
numero=input('Ingrese número entero positivo: ')
acum=0
for car in numero:
    acum_factorial=1
    for dig in range(1,int(car)+1):
        acum_factorial=acum_factorial*dig
    acum=acum+acum_factorial
print(acum)


#Escriba un programa que evalua si un numero entero positivo ingresado por 
#el usuario es narcisista o no.
#Un número narcisista es un número de n dígitos, que coincide con la suma de 
#las potencias n-ésimas de sus dígitos. Por ejemplo, 153 es narcisista ya que 
#1^3+5^3+3^3=153.
numero=input('Ingrese número entero positivo: ')
acum=0
n=len(numero)
for car in numero:
    acum=acum+((int(car))**n)
print(acum)



#Elabore un programa tal que dado un valor n entero positivo, 
#calcule y muestre los elementos correspondientes a la CONJETURA DE ULLMAN 
#(en honor al matemático S. Ullman) que consiste en lo siguiente:
#Empiece con cualquier entero positivo.
#Si es par, divídalo entre 2.
#Si es impar multiplíquelo por 3 y agréguele 1.
#Obtenga enteros sucesivamente repitiendo el proceso.
#Al final se obtendrá el número 1, independientemente del entero inicial.
#   Por ejemplo:
#   cuando el entero inicial n es 52, la secuencia será:
#       52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

numero=int(input('Ingrese número entero positivo: '))
ullman=numero
print(ullman, end=" ")
while ullman > 1:
      if ullman%2==0:
          ullman=ullman//2
      else:
          ullman=(ullman*3)+1
      print(ullman, end=" ")


#Se ha realizado un muestreo con los precios del barril de petróleo durante 
#el último mes (de 30 días), suponga que dichos valores son enteros y que han 
#fluctuado entre $ 130 y $ 150 (en forma aleatoria).  
#Una vez elaborada la muestra, se desea determinar:
#a) El promedio del precio del petróleo
#b) ¿Cuál fue el día en el que estuvo más barato el barril de petróleo?
#c) ¿Cuántos días el petróleo tuvo precios superiores al promedio?

import random as rd

val=[rd.randint(130,150) for x in range (30)]
promedio=sum(val)/30
minimo=[str(i+1) for i, n in enumerate(val) if n==min(val) ]
superior=[i for i, n in enumerate(val) if n>promedio ]
mindias=' '.join(minimo)
print("El promedio del precio del petróleo es: %.2f" %(promedio))
print("El dia en el que estuvo más barato el barril de petróleo fue : %s" %(mindias))
print("%d dias el precio del petroleo fue superior al promedio" %(len(superior)))



#En un juego de adivinanza, un primer jugador escribe una palabraA, se desordenan 
#sus letras, y se muestran al otro jugador.
#El jugador que desea adivinar, usando las letras mostradas, escribe otra palabraB. 
#Si es igual a palabraA gana el juego, sino, tiene tantas oportunidades como 
#letras haya en la palabra.
#Ejemplo roma
#oram

import random as rd

desorden=[]
palabraA=input("Ingrese palabra: ")
letras_lista=[x for x in palabraA]
while(letras_lista!=[]):
     secreto=rd.choice(letras_lista)
     desorden.append(secreto)
     letras_lista.remove(secreto)
desordenada=''.join(desorden)
print('Desordenada: %s' %(desordenada))
for i in range(len(desordenada)):
    palabraB=input("Ingrese palabra: ")
    if palabraB==palabraA:
        print('Adivinastes....:)')
        break

     
     


#tema 1

list_rell=[]
letra='o'
secreto="Programacion"

for elem in secreto:
    if elem==letra:
        list_rell=list_rell+[letra]
    else:
        list_rell=list_rell+["_"]
str_rell = ' '.join(list_rell)
print(str_rell)

    
########################### ya
palabra ='aabbbccdefggh'
final=''         
actual=''
for letra in palabra:
    if letra != actual:
        final = final + letra
        actual=letra
print(final)
#solucion 
#abcdefgh  


palabra="Hola examen"
b=palabra[:palabra.find(" ")]
c=b+"_"+palabra[palabra.find(" ")+1:]
print(c)





x=[9,5,6,7,3,2,5,6,1,0,5]
print(x[3],x[x[2]],x[x[x[x[1]]]],x[x[x[x[-2]+2]]])

#7 5 2 2





x=[9,5,6,7,3,2,5,6,1,0,5]
print(x[4],x[x[-2]],x[x[x[x[5]]-1]],x[x[x[x[-1]+2]]])

#3 9 6 2







# 1ra Evaluación I Término 2017
# Tema 1. puntaje de palabras
# Tarea: considere los '*'como doble puntaje
#        para letra anterior
import numpy as np

# INGRESO
# variaspalabras = input('Analizar: ')
variaspalabras ='CAS*A*,S*ASTR*E*,R*EY*,A*ZOTE*'

# PROCEDIMIENTO
abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
equivale = [1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]

# unifica a mayúsculas
variaspalabras = variaspalabras.upper()
palabras = variaspalabras.split(',')

n = len(palabras)

# arreglo de puntos por palabra
puntos = np.zeros(n,dtype=int)

i = 0
while (i<n):
    unapalabra = palabras[i]
    m = len(unapalabra)

    # Analiza palabra, letra por letra
    j = 0
    while (j<m):
        letra = unapalabra[j]
        if (letra in abecedario):
            donde = abecedario.index(letra)
            puntos[i] = puntos[i]+equivale[donde]

        j = j+1
    i = i+1
cual = np.argmax(puntos)

# SALIDA
print('resultado: ')
i = 0
while (i<n):
    print(palabras[i],puntos[i])
    i = i+1

print('Mayor puntaje: ')
print(palabras[cual],puntos[cual])




# 1ra Evaluación II Término 2017
# tema 1. fabrica de juguetes
import numpy as np

# INGRESO
tareas = ['pintar soldados',
          'hornear galletas',
          'armar muñecos',
          'cortar papel de regalo']
inicio   = [ 678, 200, 240, 423]
duracion = [ 300, 800, 456, 112]

# PROCEDIMIENTO
n=len(tareas)
final = np.zeros(n,dtype=int)
i=0
while not(i>=n):
    final[i] = inicio[i]+duracion[i]
    i=i+1

# Determina el orden
finaliza=np.copy(final)
orden = np.zeros(n,dtype = int)
j=0
while not(j>=n):
    mayor = 0
    i=1
    while not(i>=n):
        if (final[i]>final[mayor]):
            mayor = i
        i=i+1
    orden[j]=mayor
    final[mayor]=0
    j=j+1
# dias de trabajo:
dia = np.zeros(n,dtype = int)
cual = 1
suma = 0
j=0
while not(j>=n):
    suma = suma + finaliza[j]
    if (suma>=1440):
        cual = cual+1
        suma = finaliza[j]
    dia[j]=cual
    j=j+1
   
# SALIDA
print('finaliza')
print(finaliza)
print('Tareas del dia')
s=0
i=0
while not(i>=n):
    cual = orden[i]
    s = s+finaliza[cual]
    print(i,cual,tareas[cual],s, dia[i])
    i=i+1



import random
import math

xh = -2
yh = 2

# PROCEDIMIENTO
xa = 10
ya = 8
dmayor = math.sqrt((xh-xa)**2+(yh-ya)**2)
encontrado = 0
turno = 0
while (turno<100 and encontrado==0):
    dir = int(random.random()*4)+1
    pasos = int(random.random()*3)+1

    if dir==1:
        yh = yh+pasos
    if dir==2:
        yh = yh-pasos
    if dir==3:
        xh = xh+pasos
    if dir==4:
        xh = xh-pasos
    if (xh==xa and yh==ya):
        encontrado = 1

    d = math.sqrt((xh-xa)**2+(yh-ya)**2)
    if d>dmayor:
        dmayor = d
    turno = turno+1

# SALIDA
print('estado encontrado: ')
print(encontrado)
print('turnos simulados: ')
print(turno)
print('distancia mas lejana: ')
print(dmayor)




#import random
#import math
#
#xh = -2
#yh = 2
#
## PROCEDIMIENTO
#xa = 10
#ya = 8
#dmayor = math.sqrt((xh-xa)**2+(yh-ya)**2)
#encontrado = 0
#turno = 0
#while (__________ and encontrado==0):
#    dir = int(random.random()*4)+1
#    pasos = int(random.random()*3)+1
#
#    if dir==1:
#       _______________
#    if dir==2:
#        ______________
#    if dir==3:
#        _______________
#    if dir==4:
#        _______________
#    if (______ and ________):
#        encontrado = 1
#
#    d = ___________________________
#    if d>dmayor:
#        _______________
#    turno = _____________
#
## SALIDA
#print('estado encontrado: ')
#print(encontrado)
#print('turnos simulados: ')
#print(turno)
#print('distancia mas lejana: ')
#print(dmayor)




































