#https://www.hackerrank.com/challenges/capitalize/problem



import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split()
    n = ""
    liste = ["0","1","2","3","4","5","6","7","8","9"]
    for i in range(len(words)):       
        if words[i].isalpha() == True:
            words[i]=words[i].capitalize()         
        elif words[i].isdigit() != True:    
            w = words[i]       
            for x in range(len(words[i])):              
                if w[x] in liste:
                    print("girdi3")
                    x=x+1
                else:
                    words[x]=words[x].capitalize()           

    for i in range(len(words)):
        n += words[i]+" "

    return n

if __name__ == '__main__':
    

    s = input()

    result = solve(s)
    print(result)
    



