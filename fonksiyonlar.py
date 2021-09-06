# def fonksiyonadi(varsa parametre):
    #islevler

"""
def toplamaYap():
    sonuc = 3+5
    print(sonuc)

def cikarmaYap(a,b):
    if a>b:
        print(a-b)   
    else:
        print(b-a)

def carpmaYap(e,f,g):
    sonuc = e*f*g
    return sonuc

def ikiDegerDondur(o,p):
    return o, p

toplamaYap()
cikarmaYap(3,8)
carpmametodusonucu = carpmaYap(2,3,4)
cikarmaYap(carpmametodusonucu,10)
tutucu1,tutucu2 = ikiDegerDondur(5,10)
print(tutucu1,tutucu2)
"""

def sayiTahminOyunu():
    print("sayi tahmin oyunumuza hos geldiniz")
    bulunacaksayi = 70
    sayac = 0 
    while True:
        alinansayi = int(input("0 ile 100 arasinda sayi giriniz "))
        if alinansayi<0 or alinansayi>100:
            print("oyunu kurallarina gore oynamadin programi sonlandirdim.")
            break
        elif alinansayi>bulunacaksayi:
            print("daha kucuk bir sayi giriniz")
            sayac+=1
        elif alinansayi<bulunacaksayi:
            print("daha buyuk bir sayi giriniz")
            sayac+=1
        else:
            print("sayiyi dogru tahmin ettiniz. tutulan sayi =",bulunacaksayi)
            print("oyunu",sayac,"hamlede tamamladiniz")
            break

def FindTheRunnerUpScore():
    n = int(input("kac adet sayi gireceksiniz "))
    liste = list()
    gecici=-10000
    for i in range(n):
        liste.append(int(input("giris yapiniz ")))
    
    for a in range(len(liste)):
        for x in range(len(liste)):
            if liste[a]<liste[x]:
                gecici=liste[a]
                liste[a]=liste[x]
                liste[x]=gecici   
    print(liste[-2])

def oyunSec():
    while True:
        print("1 veya 2 sayilarindan birini seciniz")
        girdi = int(input())
        if girdi == 1 or girdi == 2:
            return girdi
        else:
            print("hatali girdi yaptiniz tekrar deneyiniz")

def oyunYonetenMetot():

    print("oyunlar klasorune hos geldiniz bir oyun secme islemi ile baslayalim")
    tutucu = oyunSec()
    if tutucu == 1:
        sayiTahminOyunu()
    else:
        FindTheRunnerUpScore()  
        print("oyunu tamamladiniz")  


#oyunYonetenMetot()

def toplamaYap(a=0,b=1):
    sonuc = a+b
    print(sonuc)


#toplamaYap()

def yazdir(sembol,satir,sutun):
    for i in range(satir):
        print(sembol*sutun)

#yazdir(satir=5,sutun=5,sembol="*")

def toplama(*sayilar):
    sonuc = 0
    for i in sayilar:
        sonuc+=i
    return sonuc    

print(toplama(5,4,6,3,7))
