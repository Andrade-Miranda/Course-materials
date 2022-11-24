#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 22:14:13 2019

@author: Gustavo
"""
import numpy as np
from scipy.optimize import curve_fit


def function_f(x):
    y=2*x**2+1
    return y

def function_g(x):
    return 3*x**3+5


def menu():
    print('1 Para ingresar datos')
    print('2 Para iniciar juego')
    print('3 Para salir')
    


def crear_matriz(filas,columnas):
    matrix=np.random.randint(1,51,size=(filas,columnas))
    promedio=sum(sum(matrix))/matrix.size
    #promedio1=matrix.sum().sum()/matrix.size
    mayores=len(matrix[matrix>promedio])
    return promedio,mayores




def carreraObstaculos(filas,columnas):
    matrix=np.random.randint(2,size=(filas,columnas))
    ganador=np.where(matrix.sum(1)==max(matrix.sum(1)))
    resultado=matrix.sum(1)
    promedio=sum(matrix.sum(1))/matrix.size
    return matrix,ganador,resultado,promedio
    








def buscaminas(m,n,x,y):
    minas=np.zeros((n,n))
    mask=np.ones((3,3))
    cont=0
    while (1):
        ale=np.random.randint(0,n,2)
        if minas[ale[0],ale[1]]!= 1:
            minas[ale[0],ale[1]]=1
            cont+=1
        if cont==m:
            break
    if minas[x,y]==1:
        return 'perdistes',minas
    else:
         total=sum(sum(mask*minas[x-1:x+2,y-1:y+2]))
         return total,minas
   
    
    















#Diseñar un algoritmo que llene una matriz de m x n. 
#Calcular el promedio de la matriz, determinar cuántos valores son mayores 
#que el promedio. Visualizar en la pantalla los datos en el siguiente orden:

#Media
#Número de valores mayores que el promedio
#Lista de los valores mayores que el promedio


# Creating a function to model and create data
def func(x, a, b):
    return a * x + b

# Generating clean data
x = np.linspace(0, 10, 100)
y = func(x, 1, 2)
# Adding noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)
# popt returns the best fit values for parameters of
# the given model (func).
print(popt)
