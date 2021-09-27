class hayvanlar():

    def __init__(self,isim,yas,cins):
        self.isim=isim
        self.yas=yas
        self.cins=cins
        
    def yemekye(self,isim):
        print(f"{isim} isimli {self.cins} yemek yedi")

    def suIc(self,isim):
        print(f"{isim} isimli {self.cins} su icti")

    def yuru(self,isim):
        print(f"{isim} isimli {self.cins} yurudu")

    def konus(self):
        print("hayvan ses cikardi")  

class kopek(hayvanlar):

    def __init__(self, isim, yas,cins,boy):
        super().__init__(isim,yas,cins)
        self.boy=boy

    def boyuDondur(self,boy):
        return boy

    def sadik():
        print("kopek oldugum icin sadigim")          

    def konus(self):
        print("kopek havladi")

class kedi(hayvanlar):

    def __init__(self, isim, yas,cins,disSayisi):
        super().__init__(isim,yas,cins)
        self.disSayisi=disSayisi


    def sacmala(self):
        print("ziplarken yere dustum")

    def itaatEttir():
        print("mama koy kole")

    def konus(self):
        print("kedi miyavladi")    

class kus(hayvanlar):

    def __init__(self, isim, yas,cins,kanatBoyu):
        super().__init__(isim,yas,cins)
        self.kanatBoyu=kanatBoyu

    def gagala():
        print("gaga saldirisi basladi")

    def pencele():
        print("pence saldirisi basladi")    

    def konus(self):
        print("kus cikcik ottu")

hayvan = hayvanlar("anasinif", 20,"havyan classi")
kopek1 = kopek("karabas",5,"kopek","1m")
kedi1 = kedi("minnos", 10,"kedi",20)
kus1 = kus("limon",3,"kus","1m")

hayvan.konus()
hayvan.suIc(hayvan.isim)
hayvan.yemekye(hayvan.isim)
hayvan.yuru(hayvan.isim)

print("==="*10)

kopek1.konus()
kopek1.suIc(kopek1.isim)
kopek1.yemekye(kopek1.isim)
kopek1.yuru(kopek1.isim)
print("kopegin boyu :",kopek1.boyuDondur(kopek1.boy))

print("==="*10)

kedi1.konus()
kedi1.suIc(kedi1.isim)
kedi1.yemekye(kedi1.isim)
kedi1.yuru(kedi1.isim)
print("kedinin dis sayisi:",kedi1.disSayisi)

print("==="*10)

kus1.konus()
kus1.suIc(kus1.isim)
kus1.yemekye(kus1.isim)
kus1.yuru(kus1.isim)
print(kus1.kanatBoyu)




