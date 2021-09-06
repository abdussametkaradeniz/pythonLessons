"""
sayi = 1
while sayi<=50:
    print(sayi)
    sayi+=1

"""
#sayi tahmin oyunu

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









