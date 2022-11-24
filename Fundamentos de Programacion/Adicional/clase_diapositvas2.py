#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:30:50 2019

@author: Gustavo
"""


palabra= input("Ingrese palabra: ")
for letra in palabra:
    print("la letra es %s"%letra)
    if letra=='a':
        print('encontrado')
        break
        print('esto no se imprime')
print ('he terminado')










x=5
y=9
z=12



x=5;y=9;z=12

x, y, z =5, 9, 12
x=y=z=0

#Sume 2 números y divídalos para 2
num1 = '6' #primer numero
num2 = 10
suma = int(num1) + num2
print(suma)



# Calcule el valor a cancelar por una deuda de $2000, considerando IVA del 14%. Imprima el valor a cancelar.
deuda = 2000
iva =0.14
valor_cancelar = deuda + (iva*deuda)
print(int(valor_cancelar))


nombre=input("ingrese su nombre: ")

numero1=input("ingrese un numero: ")



# Calcule el valor
# correctamente
deuda = 2000
iva =0.14
valor_cancelar = deuda + (deuda*iva)
print(int(valor_cancelar))


num1=int(input("Ingrese primer numero: "))
num2=int(input("Ingrese segundo numero: "))

suma_str= num1+num2

suma_num= int(num1)+int(num2)

suma_nul= int(num1+num2)

print(suma_str)

print(suma_num)

print(suma_nul)




Fecha=45
fecha=45




#asignacion de variables
x=5; y=4; z=6 #asignacion multiple


#comentario de entrada de datos
nombre = input("Ingrese su nombre: ") 
print("Hola ", nombre, ", saludos." )

#comentario de salida de datos
base = input("Ingrese la base: ") 
altura = input("Ingrese la altura: ") 
print("La base es ", base, "y la altura", altura)




radio=float(input('introduce el radio: '))
pi=3.14
Area=pi*(radio**2)
print('El area del circulo de radio',radio, " es:", Area)




radio=input('introduce el radio: ')
area=[(int(radio)**2)*3.14]
print('El area del circulo de radio',radio, " es:", area)


pi=3.14
radio=int(input('introduce el radio: '))
area=pi*(radio**2)
print('El area del circulo de radio',radio, " es:", area)


pi=3.14
radio=float(input('introduce el radio: '))
print("radio es",radio,"xpi^2",pi*(radio**2))









radio=input('introduce el radio: ')
area=int(3.14*radio)**2
print('El area del circulo de radio',radio, " es:", "valor_del_area")








int((radio**2)(pi))




num1=345
num2=345.67890345
print("%d , %f"%(num1,num2))


nombre="gustavo"
apellido="cerrati"
print("hola",nombre,", saludos")
print("hola %s %s saludos" %(nombre,apellido))



print('hola \t \'como estas\' \nyo estoy bien')







nombre=input("ingrese nombres: ")
edad=int(input("ingrese edad: "))
semestre=input("ingrese semestre:")
nota=float(input("ingrese nota: "))
universidad=input("ingrese universidad: ")
facultad=input("ingrese facultad: ")
ciudad=input("ingrese ciudad: ")

print("""Hola me llamo %s, tengo \n%d años,
naci en %s \nestudio en la universidad 
      %s\t%s facultad \nestoy en el %s semestre 
      y \nmi nota de programacion sera %.1f"""
      %(nombre,edad,ciudad,universidad,facultad,
        semestre,nota))


print("""Hola me llamo %s, tengo
%d años,naci en %s
estudio en la universidad 
%s\t%s facultad 
estoy en el %s semestre y 
mi nota de programacion sera %.1f"""
%(nombre,edad,ciudad,universidad,facultad,
        semestre,nota))




3*apellido



apellido="cerrati"



apellido[6]





print("Hola \"como estas\"\nYo estoy bien.\tY tu como estas")




libro=input("Ingrese libro favorito: ")
precio=float(input("Ingrese precio: "))
tipo=input("Tipo de libro: ")
fecha=input("fecha de compra: ")
paginas=int(input("cuantas paginas tiene: "))

print("\n\nMi libro favorito es:\t\"%s\"\nEl precio es:\t%.2f\nLo compre el:\t%s\nEs un libro de:\t%s\nEl libro tiene %d paginas" %(libro,precio,fecha,tipo,paginas))

print("""\n\nMi libro favorito es:\t\"%s\"
\nEl precio es:\t%.2f
\nLo compre el:\t%s
\nEs un libro de:\t%s
\nEl libro tiene %d paginas""" %(libro,precio,fecha,tipo,paginas))












min('hola')





'holalala'.count('la')



k='hola'


clase='fundamentos'


clase[:5]
clase[5:]

s='bienvenidos \n \n al curso de programacion'

s.index('a')

s='saludos'

s.find('lu')


min('hola')

s='holalalalala'
s.count('la')
s.endswith('ho')

s.startswith('ho')


buscar = "nombre apellido" 
reemplazar_por = "Juan Pérez" 
print ("Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por) )







i=1
while i<4:
    print(i, end='')

libros=['condorito','Programacion para dummies', 'La biblia', 'crespusculo']

libros[0]

len(libros)


for letra in "Funda":
    print(letra)



palabra=input("Ingrese la palabra: ")

vocal=0
consona=0

for letra in palabra:
    if letra in 'AEIOUaeiou':
        vocal+=1
    else:
        consona+=1
        
print("""el numero de vocales es: %d 
y el numero de consonantes es: %d""" %(vocal,consona))    




for x in range(1,4):
    print("Tabla del %d" %x)
    for y in range(1,13):
        print("%d x %d = %d" %(x,y,x*y))
    print("\n")





palabra= input("Ingrese palabra: ")
for letra in palabra:
    print("la letra es %s"%letra)
    if letra=='a':
        print('encontrado')
        break
        print('esto no se imprime')
print ('he terminado')





cadena='Hola mundo cruel el proximo miercoles voy a .....'

lista=cadena.split()

' '.join(lista)

'_'.join(lista)

datos=[]
mayor=[]
while True:
    x=int(input("Ingrese un numero: "))
    if x==-1:
        break
    else:
        datos.append(x)
y=int(input("Ingrese segundo número: "))

for i in datos:
    if i>y:
        mayor.append(i)
        
        
datos=[]
mayor=[]
x=0
while x!=-1:
    x=int(input("Ingrese un numero: "))
    datos.append(x)
datos.pop(-1)
y=int(input("Ingrese segundo número: "))       
        
        
        
       
        
        
        
for i in range(len(datos)):
    if datos[i]>y:
        mayor.append(i)
 



       

x=input("Ingrese 15 numeros: ")  
numeros=x.split()
positivos=[]
negativos=[]

for num in numeros:
    if int(num)>=0:
        positivos.append(int(num))
    else:
        negativos.append(int(num))

print(numeros)
print(positivos)
print(negativos)



pokemons=['omanyte','blastoise','venomoth','alakazam','vulpix','machop','rapidash']
pa=[]
pd=[]
pc=[]

for nom_pokemon in pokemons:
    print("Ingrese los puntos de ataque de %s",end='' %nom_pokemon)
    x=int(input())
    pa.append(x)
    print("Ingrese los puntos de defensa de %s",end='' %nom_pokemon)
    y=int(input())
    pd.append(y)
    pc.append((x+y)*1.2)
    
    
    









cadena='Hola,mundo,cruel,el,jueves,es,el,examen'

palabras=cadena.split(',')

'0'.join(palabras)
















