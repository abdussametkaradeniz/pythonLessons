#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    liste = list(s) # abdussamet123
    liste1 = ["0",'1','2','3','4','5','6','7','8','9']
    liste3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    listesayilar = []
    listeharfler = []

    for i in range(0,len(liste1)):
        
        if liste1[i] not in liste:
            listesayilar.append(liste1[i])

    for i in range(0,len(liste3)):
        
        if liste3[i] not in liste:
            listeharfler.append(liste3[i])

    sonliste = listesayilar+listeharfler
    sonliste = listesayilar+listeharfler
    metin = ""
    for harf in sonliste:
        metin=metin+harf
    return metin
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
