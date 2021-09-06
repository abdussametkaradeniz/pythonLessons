#sozluk = {anahtar:value, anahtar2:value2, anahtar3:valu3}
#sozluk = {}
sozluk = {"book":"kitap", "computer":"bilgisayar", "keyboard":"klavye", "mouse":"fare"}

kelime = sozluk["mouse"]
kelime2 = sozluk.get("phone")
sozluk["monitor"]="ekran"
kelime3 = sozluk.get("monitor")
sozluk["book"]="defter"
kelime4 = sozluk.get("book")
del sozluk["book"]
#kelime5 = sozluk["book"]
#sozluk.clear()
"""
print("----------------")

for k in sozluk:
    print("ingilizcesi",k,"turkcesi",sozluk[k])

print("--------------------")

print(kelime)
print(kelime2)
print(kelime3)
print(kelime4)
#print(kelime5)
"""


print(sozluk.items())

print("*-------------------------------*")

for anahtar, deger in sozluk.items():
    print(anahtar,deger)

print("*-------------------------------*")

print("bunlar anahtarlarimiz")

for k in sozluk.keys():
    print(k)

print("*-------------------------------*")

print("bunlar degerlerimiz")

for v in sozluk.values():
    print(v)


print("*-------------------------------*")

print(len(sozluk))

print("*-------------------------------*")


print("book" not in sozluk)

print("*-------------------------------*")

sozluk = {"book":"kitap", "computer":"bilgisayar", "keyboard":"klavye", "mouse":"fare"}
sozluk2 = {"book":"roman", "computer":"bilgisayar", "keyboard":"klavye", "mouse":"fare"}

durum = sozluk!=sozluk2
print(durum)

print("*-------------------------------*")

sozluk.update(sozluk2)

for anahtar, deger in sozluk.items():
    print(anahtar,deger)

#sozluk2.clear()
#sozluk2 = {}
#del sozluk2

print("*-------------------------------*")

sozluk3 = sozluk2.copy()
for anahtar, deger in sozluk3.items():
    print(anahtar,deger)
