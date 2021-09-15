#bilgisayar classi
#fare metodu
#klavye metodu
#yazici metodu
#main 

class Bilgisayar():
    
    bilgisayardurum=False

    def __init__(self,model,marka,islemci,ekranKarti,ramMiktari,anakart,ssd,hdd):
        self.model=model
        self.marka=marka
        self.islemci=islemci
        self.ekranKarti=ekranKarti
        self.ramMiktari=ramMiktari
        self.anakart= anakart
        self.ssd=ssd
        self.hdd=hdd
        hafiza = hdd+ssd
        self.SistemBilgisi(model,marka,islemci,ekranKarti,ramMiktari,anakart,hafiza)

    def klavyeKullanimDurumu(self):
        print("klavye kullanima hazir")

    def klavyedengiridial(self):
        return input("klavyeden girdi bekleniyor ")
        
    def mouse(self):
        print("mouse kullaniliyor")

    def yazici(self,belge):
        print(f"{belge} yazdiriliyor") 

    def ekran(self):
        print("ekran goruntu gostermeye basladi")   

    def bilgisayarDurum(self,bilgisayardurum):
        if bilgisayardurum == True:
            self.ekran()
            self.mouse()
            self.klavyeKullanimDurumu()
        else:
            print("bilgisayar acilmadi once bilgisayar ac metodunu cagirin")

    def bilgisayariAc(self):
        bilgisayardurum=True
        return bilgisayardurum

    def SistemBilgisi(self,model,marka,islemci,ekrankarti,rammiktari,anakart,hafiza):
        print(f"model : {model} marka: {marka} islemci: {islemci} ekran karti {ekrankarti} rammiktari {rammiktari} anakart {anakart} hafiza {hafiza}")

bilgisayar = Bilgisayar("a","b","c","d",16,"e",120,1024)
bilgisayardurum = bilgisayar.bilgisayariAc()
bilgisayar.bilgisayarDurum(bilgisayardurum)
belge = bilgisayar.klavyedengiridial()
bilgisayar.yazici(belge)

bilgisayar2 = Bilgisayar()



