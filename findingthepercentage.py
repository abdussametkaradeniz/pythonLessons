studentsMarks = {}
l = []
for i in range(int(input())):
    l = input().split()
    studentsName=l[0]
    ort=(float(l[1])+float(l[2])+float(l[3]))/3
    studentsMarks[studentsName]=ort
name = input()
ort2 = studentsMarks[name]
print("{0:.2f}".format(ort2))    
