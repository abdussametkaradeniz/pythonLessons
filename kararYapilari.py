"""
sicaklik = 50 
if sicaklik < 25: #false durumunda
    print("sicaklik 25 dereceden azdir")

elif sicaklik >100:
    print("sicaklik 100 dereceden fazladir")   

elif 20<sicaklik and sicaklik <60:
    print("sicaklik 20 derece ile 60 derece arasindadir") 

else:
    print("sicaklik 18 dereceden fazladir")


#if 50%2==0 and 50%5==0:
    #print("sayi cifttir ve sayi ayni zamanda 5 e de tam bolunur")



renk1 = "kirmizi"
renk2 = "mavi"

if renk1 == "kirmizi":
    if renk2 =="mavi":
        print("iki rengin karisimi mordur")
    elif renk2 == "beyaz":
        print("iki rengin karisimi pembedir")
    else:
        print("renkler tutmadi") 

else:
    if renk1 ==  "mavi":
        print("elimizdeki renk mavidir")
    else:
        print("rengi bir turlu bulamadik")


"""

renk = (input("bir renk seciniz (kirmizi, mavi ve yesil)"))

if renk == "kirmizi" or renk == "mavi" or renk=="yesil":
    print("saglikli girdi yaptiniz")
    if renk =="kirmizi":
        print("rengi buldum yazdiginiz renk kirmizi")
    elif renk == "mavi":
        print("rengi buldum yazdiginiz renk mavi")
    else:
        print("rengi buldum yesil rengi yazdiniz")    
else:
    print("hatali giris yaptiniz kurallara uymadiniz diskalifiye oldunuz")

