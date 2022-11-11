print("**********\nKullanıcı Girişi\n**********\n")
sys_kullanici_adi = "TanAytok"
sys_parola = "123a123a"
giris_hakki= 3

while True:
    kullanici_adi = input("Kullanici Adi Giriniz: ")
    parola = input("Sifrenizi Giriniz: ")

    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanici Adi Yanlis!")
        giris_hakki -= 1
        print("Gecis Hakkı: ", giris_hakki)
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Sifre Yanlis!")
        giris_hakki -= 1
        print("Giris Hakki: ", giris_hakki)
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanici Adi ve Sifre Hatali!")
        giris_hakki -= 1
        print("Giris Hakki: ",giris_hakki )
    else:
        print("Basarili Giris...")
        break
    if (giris_hakki == 0):
        print("Giris Hakkiniz Bitti!")
        break

