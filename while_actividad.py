# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:35:11 2021

@author: MARLON GUERRERO
"""

while True:
    
    x=input('Ingrese un número para contar: ')
    if x== 'q' or x== 'quit':
        break
    else: #con otra función
        x=int(x) 
        y=1
        while True:
            print(y)
            y=y+1
            if y>x:
                break