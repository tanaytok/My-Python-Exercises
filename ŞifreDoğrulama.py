# Şifre doğrulama uygulaması

dogru_sifre = "12345"

giris_hakki = 3

while giris_hakki > 0:
    
    girilen_sifre = input("Şifrenizi giriniZ: ")

    if girilen_sifre == dogru_sifre:
        print("Şifre doğru.")
        break
    
    else:
        giris_hakki = giris_hakki - 1
        print("Şifre yanlış!")

    if giris_hakki == 0:
        print("Giriş hakkınız bitmiştir.")
        break
