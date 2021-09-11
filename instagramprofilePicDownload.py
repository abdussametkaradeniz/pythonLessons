import instaloader
username = input("username: ")
insta = instaloader.Instaloader() #burasi visual studioda cikmiyor bu sekilde yazarsaniz calisir
insta.download_profile(username,profile_pic_only=True)



