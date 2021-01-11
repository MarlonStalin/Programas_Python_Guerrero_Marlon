# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:48:20 2021

@author: MARLON GUERRERO
"""

str1='Cisco'
str2="Networking"
str3="Academy"
space=" "
print(str1+space+str2+space+str3)
print('\n')
print(str1+str2+str3)#no da esapacios entre cada palabra
print(str1,str2,str3)#proceso contrario de conquetenacion 
                     #separa contextualemte una variable de otra
print('\n')
print(str1+str2+str3,'\n'*2)
print(str1,str2,str3, '\n'*2)
x=5
print(type(x),'\n')
print('El valor de x es: ',x)
print('El valor de x es: '+str(x))#tomando a x como string
print('\n')
x=str(x)
print(type(x))
print('El valor de x es: '+x)
print('\n')
x=int(x)
print(type(x))
x=float(x)
print(type(x))
x=bool(x)
print(type(x))