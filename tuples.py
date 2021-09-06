demet = tuple()
demet = ()

demt = tuple([1,2,3,4])
demet = (1,2,3,4,5)

#demet = ("string",1.5,2)

#demet elemanlarina erisim 

demet = (1,2,3,4,5)

a = demet[0]
print(a)

#demet eleman sayisini bulma 

uzunluk = len(demet)
print(uzunluk)

print(demet)

for i in demet:
    print(i)

print("----------------------------")

for i in range(len(demet)):
    print(demet[i])


#demet parcalama 

#demet[baslangic:bitisi:artismiktari] 

print(demet[1:3])
    
#demette eleman varligini kontrol etme

demet = (1,2,3,4,5,1)

print(30 in demet)

print(30 not in demet)

print(demet.index(5))


#demet icerisinde bir elemanin kac kez tekrar ettigini bulma 

k = demet.count(1)
print(k)

#demet icerisinde en buyuk ve en kucuk degerleri bulma

buyuk = max(demet)
kucuk = min(demet)
print("buyuk eleman",buyuk,"kucuk eleman",kucuk)

#demet icerisindeki butun sayilarin toplamini donen fonksiyon

print(sum(demet))

