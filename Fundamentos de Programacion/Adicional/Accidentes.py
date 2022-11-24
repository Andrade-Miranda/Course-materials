#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:58:53 2019

@author: Gustavo
"""
import numpy as np
import pandas as pd



df=pd.read_csv("accidentes_provincias.csv", sep= ";",names=['Provincias','a','b','c','d','e','f','g','h','i','j'])

df.ix[0]
df.a
df['a']

df.loc[2:4,'a':'b']

f = open("accidentes_provincias.csv", "r")
content=f.readlines()
lista_nueva=[]
dic={}

for i in range(len(content)):
    lista_nueva.append(content[i].split(";"))
    dic[lista_nueva[i][0]]=lista_nueva[i][1:len(lista_nueva[i])]

s=pd.DataFrame(dic)
    
f.close()




f = open("miarchivo.txt", "w")
f.close()


f = open("foo.txt", "r")
line = f.readline()
f.close()


f = open("foo.txt", "r")
line = f.readlines()
f.close()

f = open("foo.txt", "a")
f.write('hola como estan\n')
f.write('yo estoy bien\n')
f.write('Gracias\n')
f.close()

f = open("foo.txt", "r")
lista=["manuel 30 Ecuador \n", "Remi 27 Francia \n", "Gorenkva 60 Rusia \n"]
f.writelines(lista)
f.close()


f = open("foo.txt", "r")
f.write('hola como estan\n')
f.tell()
f.seek(5)
lines = f.readlines()

f.close()



f = open("/Users/Gustavo/AnacondaProjects/pythonCode/clases_programacion/miarchivo.txt", "r")
line = f.readline()
lines=f.readlines()


f.write("Los alumnos del grupo uno no vienen a clases\n")
lista=["manuel 30 Ecuador \n", "Remi 27 Francia \n", "Gorenkva 60 Rusia \n"]
f.writelines(lista)
f.close()
f.tell()
f.seek(7)

# Open a file
fo = open("foo.txt", "w")
fo.write("primera linea \n segunda linea\n tercera linea\n cuarta linea\n")
print ("Nombre del archivo: ", fo.name)
fo.close()


fo = open("foo.txt", "r")
fo.readline()
print ("Read Line: %s" % (line))

# Again set the pointer to the beginning
fo.seek(3, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opend file
fo.close()



