#https://www.hackerrank.com/challenges/python-lists/problem

l = []
for i in range(int(input())):
    x=input().split()
    command=x[0]
    param=x[1:]
    if command == "print":
        print(l)
    else:
        command = command+"("+",".join(param)+")"     
        eval("l."+command)