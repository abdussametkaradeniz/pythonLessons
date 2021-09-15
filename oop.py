#OOP nesneye yonelik programlama
#class Siniflar():


class Siniflar:

    def __init__(self):
        print("siniflar yapici metodu calisti")

    def fenSinifi(self):
        print("fen sinifina giris yapildi")

    def matematikSinifi(self):
        print("matematik sinifina giris yapildi")

    def edebiyatSinifi(self):
        print("edebiyat sinifina giris yapildi")


class Ogretmenler():

    def __init__(self):
        print("ogretmenler init fonksiyonu calisti")
    
    def edebiyatOgretmeniKaydet(self,isim,soyisim,yas):      
        print(f"edebiyat ogretmeninin adi {isim} soyadi {soyisim} yasi {yas}")               

    def matematikOgretmeniKaydet(self,isim,soyisim,yas):
        print(f"matematik ogretmeninin adi {isim} soyadi {soyisim} yasi {yas}")

    def fenOgretmeniKaydet(self,isim,soyisim,yas):
        print(f"fen ogretmeninin adi {isim} soyadi {soyisim} yasi {yas}")        

class Ogrenciler():

    def __init__(self,isim,soyisim,okulNo,sinif):

        self.isim=isim
        self.soyisim=soyisim
        self.okulNo=okulNo
        self.sinif=sinif


    def ogrenciKaydet(self,isim,soyisim,okulNo,sinif):
        print("{} {} isim soyisimli ogrencimize {} okul numarasi atanmistir ve {} sinifina kaydi gerceklesmistir".format(isim,soyisim,okulNo,sinif))



#objeler
okul = Siniflar()
ogretmenEdb1 = Ogretmenler()
ogretmenEdb2 = Ogretmenler()
ogretmenMtm1 = Ogretmenler()
ogretmenFen1 = Ogretmenler()

Ogrenci1 = Ogrenciler("elif","yilmaz",3456,9)
Ogrenci2 = Ogrenciler("abdussamet","karadeniz",3939,12)

#objeler yardimiyla metotlara erisim
okul.matematikSinifi()
okul.fenSinifi()
okul.edebiyatSinifi()

ogretmenEdb1.edebiyatOgretmeniKaydet("ayla","yilmaz",30)
ogretmenEdb2.edebiyatOgretmeniKaydet("mehmet","gunes",27)
ogretmenMtm1.matematikOgretmeniKaydet("sevim","yetkin",23)
ogretmenFen1.fenOgretmeniKaydet("feyza","yilmaz",45)

"""
Ogrenci1.isim = "elif"
Ogrenci1.soyisim="yilmaz"
Ogrenci1.okulNo=3456
Ogrenci1.sinif=9
"""

Ogrenci1.ogrenciKaydet(Ogrenci1.isim,Ogrenci1.soyisim,Ogrenci1.okulNo,Ogrenci1.sinif)
Ogrenci2.ogrenciKaydet(Ogrenci2.isim,Ogrenci2.soyisim,Ogrenci2.okulNo,Ogrenci2.sinif)


















