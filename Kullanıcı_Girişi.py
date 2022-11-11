print("**********\nKullanıcı Girişi\n**********\n")

sys_kullanici_adi = "TanAytok"
sys_sifre = "123a123a"

kullanici_adi = input("Kullanıcı Adınızı Giriniz: ")
sifre = input("Şifrenizi Giriniz: ")

if (kullanici_adi != sys_kullanici_adi and sifre == sys_sifre):
    print("Kullanıcı Adı Hatalı!")
elif (kullanici_adi == sys_kullanici_adi and sifre != sys_sifre):
    print("Şifre Hatalı!")
elif (kullanici_adi != sys_kullanici_adi and sifre != sys_sifre):
    print("Kullanıcı Adı ve Şifre Hatalı!")
else:
    print("Başarıyla Giriş Yaptınız.")