#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:30:27 2019

@author: Gustavo
"""

### LECCION GRUPO 1

# HACER UN PROGRAMA EN PYTHON QUE IMPRIMA 
#     a
#    aaa
#   aaaaa
#  aaaaaaa
# aaaaaaaaa
#DADO EL NUMERO DE LINEAS ejemplo lineas=5
num=5
for i in range(num):
    num1=num-i
    print((" "*num1)+('a'*((i*2)+1)))
    
# HACER UN PROGRAMA EN PYTHON QUE IMPRIMA 
# aaaaaaaaa
#  aaaaaaa
#   aaaaa
#    aaa
#     a
#DADO EL NUMERO DE LINEAS ejemplo lineas=5

num=5
for i in range(num):
    num1=num-i
    print((" "*i)+('a'*((num1*2)-1)))


### LECCION GRUPO 2
#   1
#  222
# 33333
#4444444

num=8
for i in range(num):
    num1=num-i
    print((" "*num1)+(str(i+1)*((i*2)+1)))


#4444444
# 33333
#  222
#   1
num=4
for i in range(num):
    num1=num-i
    print((" "*i)+(str(num1)*((num1*2)-1)))
    



#1 
#21 
#321 
#4321 
#54321 
    
num=int(input('Ingrese numero de filas: '))
for row in range(1,num+1):
    for colum in range(row,0,-1):
        print(colum,end='')
    print("")  




n=0
for row in range(1,num+1):
    while n<row:
        print(row-n,end='')
        n+=1
    n=0
    print("") 




#54321
#4321
#321
#21
#1 

num=int(input('Ingrese numero de filas: '))  
for row in range(num,0,-1):
    for column in range(row, 0, -1):
        print(column, end='')
    print("") 


for row in range(num):
    for colum in range(num-row):
        print(num-row-colum,end='')
    print("")

#12345
#2345
#345
#45
#5

num=int(input('Ingrese numero de filas: '))
for row in range(1,num+1):
    for colum in range(row,num+1):
        print(colum,end='')
    print("") 





#### crear una lista con elementos repetidos
lista1=[1,2,2,3,4,5,5,8,4]
lista2=[]
for elem in lista1:
    conteo=lista1.count(elem)
    if conteo>1:
        for i in range(conteo):
           lista1.remove(elem)
        lista2.append(elem) 








po=[1,2,3,0,4]

po.count(4)
po.index(4,3)
po.index(4,2,5)

po.append('o')

po.insert(1,10)

po.reverse()

po.sort(reverse=True)


elem=po.pop(1)


rep=[]
lista=[1,2,2,3]
for x in range(len(lista)):
    if lista[x]==2:
        rep=rep+[x]
        







ejemplo=[1,2,3,5,7,8,9]


ejemplo=ejemplo+[3]


ejemplo.append("hola")


ejemplo.remove(3)


ejemplo.insert(4,"a")

ejemplo.insert(1,10)

ejemplo.reverse()

ejemplo.sort()


palabras=['a','z','t','b']

palabras.sort()


palabras.sort()



palabras.clear()



ed=ejemplo.pop(1)




a=[2,3,90,45,78,2,45,90,34,90]

maximo=max(a)

while True:
    if maximo in a:
        a.remove(maximo)
    else:
        break
    


a=[2,3,90,45,78,2,45,90,34,90]

























  