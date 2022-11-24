#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:20:20 2019

@author: Gustavo
"""


lista1=['hola','mundo','cruel']
for elem in lista1:
    print('elemento',elem,'valor')
    
print('elemento',lista1[1],'valor')



import numpy as np

a = np.array([1, 2, 3], float)



b=[1, 2, 3]

a = np.array(b)


matrix=np.array([[2,3,4],[3,5,6],[3,1,0]],float)


vector=np.array(b,float)




a=np.array([1,2,3])
a.ndim
a.size
a.dtype






b=a.tolist()
a = a.astype(np.int)

a = np.array([1,2,3])
a = a.astype(np.float)


a=np.zeros((5,4))
b=np.zeros((4,),int)
b=np.zeros(4,int)
a=np.full((3,4),5,int)




a=np.arange(5)


a=np.random.randint(2,size=10)

a_2d=np.random.randint(5,size=(2,4))

a_2d=np.random.randint(2,7,size=(2,3))




a=np.random.rand(5)
a=np.random.rand(2,4)

a=np.random.randint(1,7,size=(2,3))

a=np.arange(6)
b=a.reshape((2,3))


a=np.arange(0,10,0.2)
a.size

a=np.array([2.4,3.5,7.8])

a[2]


lista = [1,2,3,4,5,6,7,8,9]
a = np.array(lista, float)
b = np.array(lista, int)
c = a.reshape(3,3)
tam = c.size
filas = c.shape[0]
cols = c.shape[1]
rank = c.ndim 
tipo = c.dtype



m = 2
n = 3
solo_unos = np.ones((m,n))
matriz_nula = np.zeros((m,n), dtype=int)
pasos = np.arange(5,dtype=float)
nuevo = np.arange(0,10,2)
nuevo_2 = np.arange(0,10,.2)
nuevo_2.size

nuevo_2=nuevo_2.reshape(5,10)



np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])

np_2d[1,0] #  np_2d[1][0]
np_2d[1,3]

np_2d[1,:]



notas=np.array([ 4.13,  3.76,  3.68,  1.62,  8.77,  8.7 ,  8.89,  6.75])

notas[0]=10


arreglo1D = np.arange(0,11,2)
for el in arreglo1D:    
        print(el*2)


arreglo2D = np.array([[1, 2, 3], [4, 5, 6]], float)
for x in range(arreglo2D.shape[0]):
    for y in range(arreglo2D.shape[1]):
	    print("indices",x,y,"valor", arreglo2D[x,y]) 
        # print("indices",x,y,"valor", arreglo2D[x][y]) 
        


arreglo1d=np.random.randint(-10,11,size=20)
for x in range(arreglo1d.size):
    if arreglo1d[x]<0:
        arreglo1d[x]=1

arreglo1d=np.random.randint(-10,11,size=20)
arreglo1d[arreglo1d<0]=1



#Cree un arreglo de dos dimensiones de tamaño 5x5 
#con valores aleatorios entre cero y seis [0,5] y muestre el resultado.
#Reemplace los elementos del arreglo menores o iguales a 3 por 0 y los 
#mayores a 3 con 6.

import numpy as np
arreglo2d=np.random.randint(0,6,size=(5,5))
arreglo2d[arreglo2d<=3]=0
arreglo2d[arreglo2d>3]=6



a = np.array([1, 0, 3], float)
np.all(a>0)
np.any(a>0)
index=np.where(a>0)

a[index[0][0],index[1][0]]

a = np.arange(6)
b=a.reshape((2,3))


a = np.arange(6).reshape((2,3))
np.all(a>3)
np.any(a>3)
index=np.where(a>3)

#Dado dos arreglos, nota_1 y nota_2, con las notas de los estudiantes del primero 
#y segundo parcial. Calcular:
    #El promedio final de cada alumno
    #El promedio final del curso.
import numpy as np

nota_1=np.zeros(5)
nota_2=np.zeros(5)
acum=0
for x in range(5):
    print('Ingrese la nota',x+1,'del estudiante',end =" ")
    nota_1[x]=input("ingrese las notas del primer parcial: ")
    nota_2[x]=input("ingrese las notas del segundo parcial: ")
promedio= (nota_1+nota_2)/2

for y in range(5):
    acum+=promedio[y]
acum=acum/5

promed_final=sum(promedio)/promedio.size
print('La notas promedios de los estudiantes son: ',promedio)

#####################
import numpy as np
notas=np.zeros((3,5), dtype=float)
for x in range(5):
    print('Ingrese la nota',x+1,'del estudiante',end =" ")
    notas[0,x]=input("ingrese las notas del primer parcial: ")
    notas[1,x]=input("ingrese las notas del segundo parcial: ")
    #notas[2,x]=(notas[0,x]+notas[1,x])/2
    
notas[2,:]= (notas[0,:]+notas[1,:])/2
promed_final=sum(notas[2,:])/notas.shape[1]
print('La notas promedios de los estudiantes son: ',promedio)

promedio_notas1=notas.sum(1)/5

################
import numpy as np
notas1P=[]
notas2P=[]
x=1
while(True):
    print('Ingrese la nota',x,'del estudiante',end =" ")
    notas1P.append(float(input("ingrese las notas del primer parcial: ")))
    notas2P.append(float(input("ingrese las notas del segundo parcial: ")))
    x+=1
    continuar=input('Ingrese f para terminar: ')
    if continuar=='f':
        break
notas1=np.array(notas1P)
notas2=np.array(notas2P)
promed=(notas1+notas2)/2
promed_final=sum(promed)/notas1.size





import numpy as np
a_1D = np.array([2, 4, 3], float) 
b=a_1D.sum(axis=0) #suma columnas
d=a_1D.prod(axis=0)#producto columnas
a_1D.argmax() #indice con el valor maximo
a_1D.argmin() #indice con el valor minimo
a_1D.argsort(0)
print(a_1D.sort(0))




import numpy as np
a_2D = np.array([[2,4,3],[4,5,5],[3,4,5]], float) 
b=a_2D.sum(axis=0) #suma columnas
d=a_2D.sum(axis=1)#suma filas
a_1D.argmax() #indice con el valor maximo
a_1D.argmin() #indice con el valor minimo
a_1D.argsort(0)
print(a_1D.sort(0))





a_2D = np.arange(6).reshape((2,3))
b=a_2D.sum(axis=0) #suma columnas
c=a_2D.sum(axis=1) #suma filas
d=a_2D.prod(axis=0)#producto columnas
e=a_2D.prod(axis=1)#producto filas
a_2D.argmax(0) #indice con el valor maximo
a_2D.argmin(1)
a_2D.argsort(1)


#¿Cuál es el valor del polinomio x^3 - 5 * x^2 + 1 en los puntos x = [1.3, 22, 99]?.

# Creating an image
img1 = np.zeros((20, 20)) + 3
img1[4:-4, 4:-4] = 6
img1[7:-7, 7:-7] = 9
# See Plot A




#¿Cuál es el valor del polinomio x^3 - 5 * x^2 + 1 en los puntos x = [1.3, 22, 99]?.
import numpy as np

n=int(input('Ingrese el numero de datos: '))
x=np.zeros(n)
for i in range(n):
    x[i]=float(input('dato: '))


y=np.zeros(x.shape)

for i in range(x.size):
    y[i]=x[i]**2-(6*x[i]**2)+x


#####
n=int(input('Ingrese los datos de la lista: '))
x=np.random.randint(0,101,size=(n,))
acum=0

for i in range(x.shape[0]):
    if x[i]%2==0:
        acum+=x[i]



######
#Simular el juego de una carrera de obstáculos con n participantes y m obstáculos, el corredor ganador es aquel que 
#Llega primero a la meta derribando el menor número de obstáculos. Simular el derribo de un obstaculo mediante 
#la generación aleatoria de 1 o 0 y generar el tiempo final de cada participante como un valor real entre 9 y 10    
import numpy as np
import math

n=int(input('Ingrese el numero de participantes: '))
m=int(input('Ingrese el numero de obstaculos: '))
minim=math.inf

carrera2D=np.random.randint(0,2,size=(n,m))
resultados1D=carrera2D.sum(axis=1) #suma filas

tiempo1D=np.random.rand(n)+9
maximo=resultados1D.max(axis=0)

if np.any(resultados1D==maximo):
    ind_ganadores=np.where(resultados1D==maximo)
    for i in range(len(ind_ganadores[0])):
        if tiempo1D[ind_ganadores[0][i]]<minim:
            minim=ind_ganadores[0][i]
            index=i
    print('ganador es:',index+1,'participante')
else:
    print('ganador es:',resultados1D.argmax(axis=0)+1,'participante')


    






####

import numpy as np

n=int(input('Ingrese el numero de ranas: '))
m=int(input('Ingrese el numero de metros: '))

ranas=np.zeros(n)
pasos=np.zeros(n)
juegos=0

while(True):
        pasos=np.random.randint(0,3,size=n)
        ranas=ranas+pasos
        if np.any(ranas>=m):
           ganador=np.where(ranas>=m)
           break
        pasos=np.zeros(n)
        juegos+=1

print('Numero de juegos:',juegos,'las ranas ganadoras',ganador+1)
        

            

    




import numpy as np
a_2D = np.array([[2,4,1],[4,2,5],[2,1,5]], float) 
b=a_2D.sum(axis=1) 
d=a_2D.sum(axis=0)
print(b,d,a_2D[2][1])


















