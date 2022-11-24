#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:11:47 2018

@author: Gustavo
"""


#### listas ejemplos#######

peliculas=["Titanic","300","Avengers","Lo que el viento se llevo"]
print(peliculas[0])
print(peliculas[1])
print(peliculas[2])
print(peliculas[3])

peliculas_2=["Titanic",2000,"300",34.43,"Avengers",True,"Lo que el viento se llevo",
             ["Pepit2",23.45,"rt"]]

nombres1=["jorge","pepe"]
nombres2=["diego","jose","Manuel"]
del nombres2[1]

total=nombres1 + nombres2
nombres1 += nombres2 #nombres1=nombres1+nombres2


materias = ['matemáticas', 'física', 'química', 'biología','fundamentos']
print(materias)
print(len(materias))
print(materias[2])
print(max(materias))
print(min(materias))
list(materias)
materias.index("química")
materias.count("química")
materias.index("matemáticas")


notas = [5, 7.5, 6, 8,2]
print(max(notas))
print(min(notas))


materias = [ 'fisica', 'fisama','fundamentos']
print(max(materias))
print(min(materias))
list(materias)


a = ["apples", "bananas", "oranges"]
a[0] = "berries"
print(a)

a = ("apples", "bananas", "oranges")
a[0] = "berries"


#Una tienda cobra $12 por artículo si el usuario compra menos de 10 artículos. 
#Si el usuario compra entre entre 10 y 99 artículos, el costo por artículo es 
#de $10. Si el usuario compra mas de 100 artículos el costo por artículo es de 
#$7. Escriba un programa que pida al usuario cuantos items el está comprando e 
#imprima el costo total de la compra

items=int(input("Numero de compras de usuario:  "))

if items<10:
    costo=12
elif 10<=items<=99:
    costo=10
else: 
    costo=7
    
pago=items*costo    
print("El pago total {0} x {1} is {2}.".format(items,costo,pago))


#### crear una lista con elementos repetidos
lista1=[1,2,2,3,4,5,5,8,4]
lista2=[]
for elem in lista1:
    conteo=lista1.count(elem)
    if conteo>1:
        for i in range(conteo):
           lista1.remove(elem)
        lista2.append(elem) 


### separar unidades decenas y centenas y sumarlas
numero=int(input("Ingrese un numero entero positivo: " ))
acum=0
nuevo_num=numero

for i in range(len(str(numero))-1):
     digito=nuevo_num//10**(len(str(numero))-i-1)
     nuevo_num=nuevo_num%10**(len(str(numero))-i-1)
     acum=acum+digito
acum=acum+nuevo_num
          
print("la suma es %d" %(acum))  


### uso de listas de comprenhsion
letras_lista=[]
palabraA=input("Ingrese palabra: ")
for x in palabraA:
    letras_lista.append(x)
print(letras_lista)    
   
letras_lista=[]
palabraA=input("Ingrese palabra: ") 
letras_lista=[x for x in palabraA]
print(letras_lista)


#enumerate
ind=[]
choices = ['pizza', 'pasta', 'salad', 'nachos','pizza','hamburguesa','pizza']
list(enumerate(choices))
for index, item in enumerate(choices):
    if item == 'pizza':
      ind.append(index)
    
ind=[index for index, item in enumerate(choices) if item == 'pizza']
print(ind) 


####slicing
pares = [0,2,4,6,8]
pares[-1]
pares[1] = 9
pares[1:3]
pares[:2]
pares[3:]
pares[:]

#Clonar una lista
a = [1, 2, 3]
b = a[:]
a[1] = 'cambio'
print(a)
print(b)

#Escriba un programa que, dada dos listas de 4 elementos, 
#devuelva una lista con las suma de cada uno de los elementos (suma de vectores).

from operator import add

list1=[3,4,5,6]
list2=[4,6,6,7]
suma1=list( map(add, list1, list2) )


suma=[sum(J) for J in zip(list1, list2)]


suma=[]
for i in range(len(list1)):
    suma.append(list1[i]+list2[i])
    
suma=[]
for i in range(len(list1)):
    suma=suma+[list1[i]+list2[i]]

### crear lista a partir de una cadena
cadena = 'hola mundo'
lista_cadena=cadena.split(' ')
cadena.split('r')

######## crear una cadena a partir de una lista
palabras = ['esto','es','una','lista','de','palabras']
Nuevacadena=' '.join(palabras)
'HOLA'.join(palabras)
''.join(palabras)



#Diseñe una “calculadora Pokémon” la cual, dada una lista con los nombres 
#de los especímenes, pida al usuario que ingrese los puntos de ataque (PA) y 
#de defensa (PD) de cada pokemon. Calcule sus puntos de combate (PC) en base 
#a la siguiente fórmula: 	CP= (PA+PD)*1.2
#Muestre por pantalla el CP promedio de todos los pokemones, el pokémon con
#mayor CP y el pokemon con el menor CP. 
 #pokemons= [“omanyte”,”blastoise”,”venomoth”,”alakazam”,”vulpix”,”machop”,”rapidash”]

pokemons= ['omanyte','blastoise','venomoth','alakazam','vulpix','machop','rapidash']

pa=[]
pd=[]
cp=[]
for elem in pokemons:
    ataque=int(input('Ingrese puntos de ataque de {0}:'.format(elem)))
    defensa=int(input('Ingrese puntos de defensa de %s:'%(elem)))
    pa.append(ataque)
    pd.append(defensa)
    cp.append((ataque+defensa)*1.2)
maximCPindex=cp.index(max(cp))
MInCPindex=cp.index(min(cp))
print('%s tiene el CP mas alto: %.2f'%(pokemons[maximCPindex],cp[maximCPindex]))
print('%s tiene el CP mas bajo: %.2f'%(pokemons[MInCPindex],cp[MInCPindex]))
print('El CP promedio de mis pokemons es: %.2f'%(sum(cp)/len(cp)))




    

#################TUPLAS################



list1=['error','mistake', 11, 23.09]

tupla1=tuple(list1)
list2=list(tupla1)


t = (12345, 54321, ['hola','chao'])
t[2][1]

x, y, z = t


import math 
def funcion(r):
    c=2*math.pi*r
    a=math.pi*r*r
    t=(c,a)
    return t

circ, area = funcion(4)



julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress" )
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]

tuplaJulia=list(julia)
tuplaJulia.append('Actress')
julia=tuple(tuplaJulia)

ue={4,6,1,3,8,6}
set("holaholahola")
set1 = set() # Un nuevo set vacío
set1.add("cat") 

s = set([32, 9, 12, 14, 54, 26])
32 in s
s = set([12, 26, 54])
s.add(32)
s


#Crear un programa que muestre por pantalla una lista sin palabras 
#repetidas de una frase ingresada por el usuario. 

lista=['hola', 'mundo', 'mundo', 'como', 'estas' ,'estas']

def eliminar_repetido(lista):
    set_lista=set(lista)
    return list(set_lista)

sin_repetir=eliminar_repetido(lista)


#Una empresa de marketing desea saber que productos en común compran 
#tres usuarios en un supermercado. Para esto, la empresa tiene una lista
#de los productos comprados para cada usuario. Mostrar por pantalla cuáles 
#productos compran en común los tres usuarios. 
#usando interseccion set

a=set([1,2,3,4,5])
b=set([1,4,5,7,8])
c=set([1,4,25,7,8])
d=set("holaholahola")

def Intersec(a,b,c):
    return list(a&b&c)

inter=Intersec(a,b,c)


#Una empresa guarda la lista de correo de sus empleados en dos archivos 
#diferentes. Puede darse el caso de que en ambos archivos exista el correo 
#del mismo empleado. Se desea enviar un correo masivo a todos los empleados 
#de la empresa, de manera que los correos no se repitan en el destinatario. 
#Escriba un programa que dada dos listas de correos de empleados lista_A y lista_B,
#muestre una lista con los correos de todos los empleados de la empresa (sin repetir). 





#diccionario

x={123:'algebra',325:'fisica',215:'quimica'}

y={123:'algebra',133:'fisica',215:'quimica',122:'algebra'}

dic= {"200705080": 'Jhonny Pincay', "201525896": 'Martha Perez'}

dic["201685296"] = "Juan Castro" 
dic["200705080"] = "Jhonny Bravo"
dic["200978945"] = "Juana Rendon"

dic["200978945"] = "pepe malecom"

del dic["201685296"]

dic.clear()


midiccionario = {'Ciudad': 'Guayaquil', 'Nombre': 'Flavio', 'Apellido': 'Danesse', 'Edad': 30, 'FechaNac': '21/10/1986'}
midiccionario.keys()

claves=list(midiccionario.keys())
valores=list(midiccionario.values())

tuplas=tuple(midiccionario.items())
tuplas[0][1]


tuplas_list=list(midiccionario.items())
tuplas_list[0][1]


midiccionario.get('FechaNac')


dic = {123: ['Anita', 25], 234: ['Elena', 34], 456:['Carmen', 45]}

dic[456][1]
len(dic)
max(dic)
min (dic)
del dic 

a=(10,["Marcos",3],20,["Martha",3])
b=dict(a)


d={123: ['libro', 20], 234:['cuaderno', 30]}
for c in d:
	print(c,d[c])


for e in d.items():
	print(e)


for c,v in d.items():
	print(c,v)




d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)



Write a Python script to generate and print a dictionary that contains a number 
(between 1 and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) : 
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}






















n=int(input("Ingrese número: "))
d = dict()
for x in range(1,n+1):
    d[x]=x**x
print(d) 





L1=[3,2,4,5]
L2=[4,5,6,7]

z=[]
for i in range(len(L1)):
    y=L1[i]+L2[i]
    z=z+[y]

suma=L1+L2






a=[2,4,6,1]
b=[3,5,7,2]

z=[]
for x in range(len(a)):
    y=a[x]+b[x]
    z=z+[y]


    














