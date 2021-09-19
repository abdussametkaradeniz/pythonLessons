#https://www.hackerrank.com/challenges/python-mutations/problem

string = input()
i,c = input().split()
print(string[:int(i)]+c+string[int(i)+1:])