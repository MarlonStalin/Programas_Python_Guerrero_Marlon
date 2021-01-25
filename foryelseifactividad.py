# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:48:38 2021

@author: MARLON GUERRERO
"""
listasw=[]
listasr=[]
listasdf=[]
lista=["R1",'R2','R3','S1','S2','S3','R4','R5','PC','Teléfono celular']
for i in lista:
    if 'S' in i:
        listasw.append(i)
    elif 'R' in i:
        listasr.append(i)
    else:
        listasdf.append(i)

print('switches: ',listasw,'\nRouters: ',listasr,'\nDispositivos Finales: ',listasdf)
