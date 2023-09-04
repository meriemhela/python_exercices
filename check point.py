# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:17:30 2023

@author: dell
"""


#Exercice01 (La liste)  :
resultats = []  # Créez une liste vide pour stocker les résultats

for i in range(2000, 3201):  # Utilisez la plage de 2000 à 3200 inclus
    if (i % 7 == 0) and (i % 5 != 0):
        resultats.append(i)  # Ajoutez les valeurs qui satisfont les conditions à la liste

print(resultats)

#----------------------------------------------------------------------
#Exercice02 (Le factoriel) : 
x = int(input ("donnez un nombre :"))
if x == 0 :
    print("le factoriel de ",x, "est : 1")
else :
    for i in range(1,x,1):
        x = x*i
    print("le factoriel de ",i+1,"est :", x)


#----------------------------------------------------------------------
#Exercice03 (le dictionnaire) : 
def carres (n):
    dictionary = {}
    for i in range (1,n+1):
        dictionary[i] = i*i
    return dictionary
    
n = int(input ("donnez un nombre :"))
resault = carres(n)
print( resault)

#----------------------------------------------------------------------
#Exercice04 (la chaine de caractere) : 
def slicing_str (s,n):
    if n >= 0 and n < len(s):
        string = s[:n] + s[n+1:] #concatination entre debut de la chaine jusqu'a l'index n avec la suite des lettres apres ce index
        return string
    else :
        print ("index not fond !")
        return s



#----------------------------------------------------------------------
#Exercice05 (table numpy -> liste python) : 
import numpy as np
x= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(x)
print("Array to list:")
print(x.tolist())

#----------------------------------------------------------------------
#Exercice06 (la covariance) :
import numpy as np
tab1= np.array([0,1,2])
tab2= np.array([2,1,0])

covariance= np.cov(tab1,tab2)
print(covariance)
