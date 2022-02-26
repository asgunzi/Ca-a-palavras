#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:38:27 2022

@author: asgunzi
"""


import numpy as np


debugMode = False


tamGrid=9
grid = np.zeros((tamGrid,tamGrid), dtype = 'str')


palavras = []

palavras.append('UVA')
palavras.append('ABACAXI')
palavras.append('PERA')
palavras.append('BANANA')
palavras.append('LICHIA')
palavras.append('ABACATE')

#Para cada palavra,
#sorteia se é horizontal ou vertical
#Sorteia posicao possível
#Tenta encaixar no grid



for palav in palavras:
    
    #sorteia se é horizontal ou vertical
    vertical = np.random.choice([0,1])
    
    count= 1
    isOk = False

    while (not isOk):
        isOk = True

        if (vertical ==1):
            x = np.random.choice(range(0,tamGrid))
            y = np.random.choice(range(0,tamGrid-len(palav)+1))
            
            
            #Verifica se é possível alocar a palavra, se for, o faz
            if grid[x][y] =='':
                for i,p in enumerate(palav):
                    if (grid[x][y+i] =='' or grid[x][y+i] ==p):
                        isOk = isOk and True #tudo bem
                    else:
                        isOk = False #não pode alocar aqui
                
                if isOk:
                    #Aloca a palavra
                    for i,p in enumerate((palav)):
                        grid[x][y+i] = p
                else:
                    count +=1
            else:
                count +=1
        else:
            x = np.random.choice(range(0,tamGrid-len(palav)+1))
            y = np.random.choice(range(0,tamGrid))
            
            #Verifica se é possível alocar a palavra, se for, o faz
            if grid[x][y] =='':
                for i,p in enumerate(palav):
                    if (grid[x+i][y] =='' or grid[x+i][y] ==p):
                        isOk = isOk and True #tudo bem
                    else:
                        isOk = False #não pode alocar aqui
                
                if isOk:
                    #Aloca a palavra
                    for i,p in enumerate((palav)):
                        grid[x+i][y] = p
                else:
                    count +=1
            else:
                count +=1
        
        
        if count>200:
            #Desiste após 100 tentativas
            isOk = True



#Preenche o resto
if (debugMode):
    for i in range(tamGrid):
        for j in range(tamGrid):
            if grid[i][j] =='':
                grid[i][j] =' '
else:
    for i in range(tamGrid):
        for j in range(tamGrid):
            if grid[i][j] =='':
                grid[i][j] = np.random.choice(list(map(chr,range(ord("A"),ord("Z")))))
                
                                        
print(palavras) 
print(grid)





