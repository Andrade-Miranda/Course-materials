#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:17:04 2019

@author: Gustavo
"""

# pandas

import pandas as pd 
import numpy as np



#### Series

#Create an Empty Series

#import the pandas library and aliasing as pd
s = pd.Series()
print (s)


# crear una series a partir de un array
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)


data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)

jugadores = np.array(['Casillas','Kante','mbappe','Ronaldo','messi'])
s = pd.Series(jugadores)
        
        
s = pd.Series(jugadores,index=['A','M','M','D','D'])
s['DE']='Pique'

s[1:3]

s[3]='Rey'

##### Crear una serie a partir de un diccionario
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)

s = pd.Series(data,index=['b','c','d','a'])
print (s)


data = {'a' : [0., 0.3, 0.2], 'b' : [1.,1.1,1.2], 'c' : [2.,2.1,2.3]}
s = pd.Series(data)

s=pd.DataFrame(data)



s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first three element
print (s[0:3])




datos={'Estado':['Guanajuato','Querétaro','Jalisco','Durango','Colima'],
   
       'Poblacion':[5486000,1828000,7351000,1633000,723455],
       
       'superficie':[30607,11699,78588,123317,5627]}

Datos_estados=pd.DataFrame(datos)

Datos_estados['Estado']
Datos_estados.Estado
Datos_estados.superficie
Datos_estados['superficie']



Datos_estados.ix[2:4]

Datos_estados.iloc[0]

Datos_estados['rural']=[500,600,4873,984,3453]



Datos_estados.loc[1:2,'Estado':'Poblacion']
Datos_estados.loc[1:2,'Poblacion':'superficie']





s_dataframe.superficie

s_dataframe['superficie']

Datos_estados.ix['J']

f = pd.read_csv("/Users/Gustavo/Downloads/Datos_abiertos_EDG_2017-2/BBD_EDG_2017_csv.csv",sep=";")

x=range(0,120,5)
f.hist(column='edad',bins=x,rwidth=0.9,grid=False)

f.ix[20:25]['sexo']


import pandas as pd 
df = pd.DataFrame(
    {'valor': [1, 2, 3, 4],
     'palabra': ['hola','ni hao','Bonjour','Hello']
    }
)
df['square'] = df['valor'] ** 2
print(df)
print(df[df['value'] % 3 == 0])








