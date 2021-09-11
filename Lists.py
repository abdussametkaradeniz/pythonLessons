"""
liste = list()#bu bir ornek bos liste tanimlamasidir
liste1 = [] #bu da bos bir liste tanimlamanin farkli bir yoludur

liste = ([1,2,3,4,5])#icerisinde 1 den5 e kadar olan sayilari barindiran liste tanimladik

liste = [1,2,3,4,5] 

liste = ["abdussamet","karadeniz"] #string tipinde bir liste tanimlamis olduk

liste = ["abdussamet",3,2.5,"karadeniz"]

#LISTE ELEMANLARINA ERISIM

liste3 = [1,2,3,4,5,6,7,8,9] 

Degisken = liste3[4]
#print(Degisken)

degisken2 = liste3[-1]
#print(degisken2)

degisken3 = liste3[-2]

#print(degisken3)

#liste eleman sayisini bulma - len()

liste4 = [1,2,3,4,5,6,7,8,9]

uzunluk = len(liste4)

#print(uzunluk)

#listeyi ekrana yazdirma



print(liste4)

for i in liste4:
    print(i)

print("---------------------------------------------------------------------")

for i in range(0,len(liste4)):
    print(liste4[i])

"""
#liste parcalama islemi 

#liste = [1,2,3,4,5,6,7,8,9]

#liste[baslangic indisi : bitis : artis] listeyi bolme/parcalama islemi yapisi

#print(liste[5:2:-1])

#liste elemanini degistirme

#liste[4]=85

#print(liste)

#for i in range(0,len(liste)):
    #liste[i]=liste[i]*liste[i]

#print(liste)

#liste = [1,2,3,4,5,6,7,8,9]

#liste birlestirme ve liste cogaltma 

#liste2 = ["a","b","c"]

#liste3 = liste+liste2+[7]

#print(liste3)

#liste4 = liste*5
#print(liste4)




#listeye eleman ekleme/cikarma/silme 

"""
liste = []

liste.append(10)
liste.append(20)
liste.append(30)
liste.append(40)
liste.append(50)
liste.append(50)
liste.append(50)
liste.append(100)

print(liste)

liste.insert(-1,90)

print(liste)

liste.remove(50)
print(liste)

del liste[-1]

print(liste)

a=liste.pop(5)

print(a)
print(liste)
"""

#listenin icerisinde bir elemanin varligini kontrol etme

#liste = [1,2,3,4,4,4,5,6,7,8,9,4]

#sonuc = liste.index(4,6)
#print(sonuc)


#liste kopyalama islemi

#liste = [1,2,3,4,4,4,5,6,7,8,9,4]
#liste2 = liste[2:5]


#print(liste2)

#liste2[3]= 94
#print(liste2)
#print(liste)

"""liste = []
liste.append(20)
liste.append(10)
liste.append(1000)
liste.append(-20)
liste.append(50)
liste.append(90)
liste.append(-60)

print(liste)
liste.sort()
print(liste)

stringListe = ["abdussamet","xorg","ali","zambak","veli","49","50"]
#stringListe.sort()
print(stringListe)
stringListe.reverse()
print(stringListe)
"""

#count max min sum metotlari

#liste = [-1,1,2,3,4,4,4,5,6,7,8,9,4]
#k = liste.count(2)
#print(k)

#b = max (liste)
#print(b)
#kucuk = min(liste)
#print(kucuk)

#toplam = sum(liste)
#print(toplam)


