import time
import calendar

print(time.time())
print(time.localtime())

"""
sira no     ozellik     anlami
0           tm_year     yili gosteriyor 4 haneli olarak (2021)
1           tm_mon      0 12 arasi deger aliyor ay bilgisini gosteriyor
2           tm_mday     1 31 arasi deger aliyor gun bilgisini gosteriyor
3           tm_hour     0 23 arasi deger aliyor saat bilgisi
4           tm_min      0 ile 59 arasi deger aliyor dakika bilgis
5           tm_sec      0 ile 60 arasi deger aliyor saniye bilgisi
6           tm_wday     0 ile 6 arasi deger aliyor haftanin gunu bilgisi 0.gun pazartesi 
7           tm_yday     1 ile 366 arasi yilin kacinci gunu bilgisi
8           tm_isdst    dst uygulamasi var mi yok mu onun bilgisini donuyor 0 yok demek 1 var demek

"""
guncelZaman = time.localtime()
print(guncelZaman[1])

print(time.asctime())

print(time.strftime("%d %m %y %H:%M:%S"))

print(calendar.calendar(2021))
print(calendar.month(1998,7))

a= calendar.isleap(1992)
print(a)


