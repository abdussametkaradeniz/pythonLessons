def faktoriyel(sayi):
    carpim = 1
    for i in range(sayi,1,-1):
        carpim *= i
    return carpim


def recursiveFaktoriyel(sayi):
    if sayi == 1:
        return 1
    return sayi*(recursiveFaktoriyel(sayi-1))

#1 1 2 3 5 8 13 21 34

def Fibonacci(number):
    if number == 1 or number == 2:
        return 1
    return Fibonacci(number-1)+Fibonacci(number-2)


"""
sayi = int(input())
sonuc=faktoriyel(sayi)
print(sonuc)
"""
"""
sayi = int(input())
sonuc=recursiveFaktoriyel(sayi)
print(sonuc)
"""

sayi = int(input())
sonuc=Fibonacci(sayi)
print(sonuc)



