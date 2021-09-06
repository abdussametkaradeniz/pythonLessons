import math

a = int(input())
b = int(input())
degree_sign = u"\N{DEGREE SIGN}"
c=math.sqrt(pow(a,2)+pow(b,2))
print(str(round(math.degrees(math.acos(b/c))))+degree_sign)


"""
aKare = pow(a,2)
bKare = pow(b,2)
#akare = a**2 or a*a
kareleriToplami = aKare + bKare
#ckare = kareleritoplami
c = math.sqrt(kareleriToplami)


teta = math.acos(b/c)
teta2 = math.degrees(teta)
teta3 = round(teta2)
stringteta3 = str(teta3)
sonuc = (stringteta3+degree_sign)
print(sonuc)
"""




