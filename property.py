class Program:

    def __init__(self):
        self._sayi=0

    @property
    def sayi(self):
        return self._sayi

    @sayi.setter
    def sayi(self,yenisayi):
        if yenisayi % 2 == 0:
            self._sayi = yenisayi
        else:
            print("sayi cift degil")

    @sayi.deleter
    def sayi(self):
        del self._sayi

p1 = Program()
p1.sayi = 20
print(p1._sayi)
