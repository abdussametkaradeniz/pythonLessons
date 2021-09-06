#replace(degistirilecek string, degisecek hali yeni hali)

kelime = "python egitim serisi"
yeniKelime= kelime.replace("i","I",2)
print(yeniKelime)
buyukHarfliKelime = kelime.upper()
print(buyukHarfliKelime)

kucukHarfliKelime = buyukHarfliKelime.lower()
print(kucukHarfliKelime)

capDeneme = buyukHarfliKelime.capitalize()
print(capDeneme)

titleDeneme = buyukHarfliKelime.title()
print(titleDeneme)

swapCaseDeneme = kucukHarfliKelime.swapcase()
print(swapCaseDeneme)

stripDeneme = "   merhaba python dunyasi  "
print(stripDeneme)
denemeSonucu = stripDeneme.strip()
print(denemeSonucu)
#rstrip() ve lstrip()

strw = "abdussamet karadeniz"
print(strw.startswith("AB"))
print(strw.endswith("nIz"))

#a+b=c

a = 5
b = 7
sonuc = str(a)+"+"+str(b)+"="+str(a+b)
#print(sonuc)

sonuc1 = "{}+{}={}".format(a,b,a+b)
print(sonuc1)

