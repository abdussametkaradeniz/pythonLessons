class Calisan():   
    _personel = []
    
    def __init__(self,isim):
       self._isim=isim
       self.kabiliyetListesi = []
       self._personelEkle()

    @classmethod
    def _personelSayisiniGoruntule(cls):
        print(len(cls._personel))

    def _personelEkle(self):
        self._personel.append(self._isim)
        print(f"{self._isim} _isimli calisan listeye eklendi")

    @classmethod
    def _personeliYazdir(cls):
        print("_personel listesi : ") 
        for kisi in cls._personel:
            print(kisi)

    def kabiliyetEkle(self, kabiliyet):
        self.kabiliyetListesi.append(kabiliyet)

    def kabiliyetYazdir(self):
        print(f"{self._isim} sahsinin kabiliyetleri asagidadir")
        for kabiliyet in self.kabiliyetListesi:
            print(kabiliyet)

    @property
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self,yeniIsim):
        kisi=self._personel.index(self.isim)   
        self._personel[kisi]=yeniIsim
        print(f"{yeniIsim} ismi basariyla degistirildi") 

if __name__ == '__main__':
    c1 = Calisan("abdussamet")
    c2 = Calisan("veli")

    Calisan._personeliYazdir()
    c2.isim = "deli"

    
    
    Calisan._personeliYazdir()

    
    
    

