"""
a = int(input())
b = int(input())
c = a / b
print(c)


liste = [1,3,4]
print(liste[5])

print(10+"++")

try:
    a = int(input())
    b = int(input())   
    c = a / b
    print(c)

except ValueError:
    print("sayi girisi yapiniz hatali girdi yaptiniz")
except ZeroDivisionError:
    print("sayilar 0 a bolunemez")
except:
    print("hatali girdi yapildi")
finally:   
    print("program basariyla sonlandi")


vizenotu = int(input())
if vizenotu > 100 or vizenotu < 0:
    raise OverflowError("vize notu 100 den buyuk veya 0 dan kucuk olamaz")
else:
    print(vizenotu)

kullaniciAdi = input("kullanici adinizi giriniz ")
assert kullaniciAdi == "admin"
sifre = int(input("sifrenizi giriniz "))
assert sifre == 123456
print("giris basarili")


try:
    print (1/0)
except ZeroDivisionError as e:
    print(e)

"""
