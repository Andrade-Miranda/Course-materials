#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:56:15 2018

@author: Gustavo
"""
import random as rd

print("Juego del barco",end="")
municiones=int(input("Cuántas municiones?: "))

#inicializacion variables
bx=0
by=0
n_bx=0
n_by=0
hundido=0
pasos=[1,2,3]
direccion=['NORTE','SUR','ESTE','OESTE']

while (bx not in range(1,6) or by not in range(1,6)):
    bx=int(input("Barco Coordenada bx?: "))
    by=int(input("Barco Coordenada by?: "))
    
# número de municiones
for i in range(municiones):
    print("\nIntento %d" %(i+1))
    cx=int(input("Disparo Coordenada cx?: "))
    cy=int(input("Disparo Coordenada cy?: "))
    
    ##nueva posicion barco
    while (n_bx not in range(1,6) or n_by not in range(1,6)):
        N_pasos=rd.choice(pasos)
        N_direc=rd.choice(direccion)
        if (N_direc==direccion[0]):
            n_by=by+N_pasos
            n_bx=bx
        elif(N_direc==direccion[1]):
            n_by=by-N_pasos
            n_bx=bx
        elif(N_direc==direccion[2]):
            n_bx=bx+N_pasos
            n_by=by
        else:
            n_bx=bx-N_pasos
            n_by=by
            
    bx=n_bx
    by=n_by
    n_bx=0
    n_by=0
    print("bx=%d y by=%d" %(bx,by))
    print("Movimiento: %d, %s casillas" %(N_pasos,N_direc))
 
    if (bx==cx and by==cy):
        hundido+=1
        print ("Disparados: %d" %(i+1))
        print ("Hundido: %d" %(hundido))
        bx=0
        by=0
        if (i<municiones):
            while (bx not in range(1,6) or by not in range(1,6)):
                print("ingrese avistamiento nuevo barco",end="")
                bx=int(input("Barco Coordenada bx?: "))
                by=int(input("Barco Coordenada by?: "))
    else:
        print ("Disparados: %d" %(i+1))
        print ("Hundido: %d" %(hundido))
        
    
            
        
        
 

import random as rd

print("Juego del barco",end="")
municiones=int(input("Cuántas municiones?: "))

#inicializacion variables
bx=0 
by=0
n_bx=0
n_by=0
hundido=0
pasos=[1,2,3]
direccion=['NORTE','SUR','ESTE','OESTE']

while (bx not in ________ or by not in _________):
    bx=int(input("Barco Coordenada bx?: "))
    by=int(input("Barco Coordenada by?: "))
    
# número de municiones
for i in range(_________):
    print("\nIntento %d" %(i+1))
    cx=int(input("Disparo Coordenada cx?: "))
    cy=int(input("Disparo Coordenada cy?: "))
    
    ##nueva posicion barco
    while (n_bx not in ________ or n_by not in ________):
        N_pasos=rd.choice(pasos)
        N_direc=rd.choice(direccion)
        if (N_direc==direccion[0]):
            ___________
            ___________
        elif(N_direc==direccion[1]):
            ___________
            ___________
        elif(N_direc==direccion[2]):
            ___________
            ___________
        else:
            ___________
            ___________
            
    bx=n_bx
    by=n_by
    n_bx=0
    n_by=0
    print("bx=%d y by=%d" %(bx,by))
    print("Movimiento: %d, %s casillas" %(N_pasos,N_direc))
 
    if (_______ and ________):
        hundido+=1
        print ("Disparados: %d" %(i+1))
        print ("Hundido: %d" %(hundido))
        bx=0
        by=0
        if (i<municiones):
            while (bx not in range(1,6) or by not in range(1,6)):
                print("ingrese avistamiento nuevo barco",end="")
                bx=int(input("Barco Coordenada bx?: "))
                by=int(input("Barco Coordenada by?: "))
    else:
        print ("Disparados: %d" %(i+1))
        print ("Hundido: %d" %(hundido))
        





       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        