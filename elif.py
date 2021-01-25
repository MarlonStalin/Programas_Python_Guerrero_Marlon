# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:18:08 2021

@author: MARLON GUERRERO
"""

acl=int(input("Ingrese el número de ACL: "))
if acl>=1 and acl <=99:
    print("es una ACL estándar")
elif acl>=100 and acl<=199:
    print("es una ACL extendida")
else:
    print('No es un número de ACL válido')
    

#try:
    #print('mensaje')
#except:
    #print("ERROR")