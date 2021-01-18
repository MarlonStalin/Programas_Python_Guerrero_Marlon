# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:16:36 2021

@author: MARLON GUERRERO
"""

dict1={'R1':'10.0.0.1',1:'AP',2:2.5,3:True,'R2':'172.17.0.1'}
print(dict1)
print(len(dict1))
print(type(dict1))
print(dict1[1])#imprime el primer caracter que esta en 1: o en 2:, etc
print(dict1[2])
print(dict1[3])
print(dict1['R1'])
print(dict1['R2'])
dict1['R3']='10.0.0.3'#agregar un nuevo valor al diccionario
print('R3' in dict1)
