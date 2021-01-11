# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:39:55 2021

@author: MARLON GUERRERO
"""

lista=['R1',5,5.8,True,"R2"]
print(lista)
print(type(lista))
print(len(lista))#tamaño de la lista
print(" ")
print(lista[0],'\n')
print(lista[4],'\n')
print(lista[-1],'\n')
print(lista[-5],'\n')
print(lista[-2],'\n')
print("")
lista[3]=False #cambiando el valor del elemento 3 de la lista
print(lista)
del lista[4]#borra un elemento de la lista
print(lista)
print(len(lista))
lista.append("R2")#agregar un valor a la lista
print(lista)
lista.append("R3")
print(lista)