# Taş - Kağıt- Makas

import random

secenekler = {"Taş", "Kağıt", "Makas"}
bilgisayar_skor = 0
kullanici_skor = 0

while True:

    kullanici_secimi = input("Taş, kağıt veya makas seçiniz. Çıkmak için = 'çık' ").lower()
    bilgisayar_secimi = random.choice(secenekler)

    if kullanici_secimi == 'çık':
        print("Oyundan çıktınız.")
        break

    if kullanici_secimi not in secenekler:
        print("Bunu seçemezsiniz.")
        continue

    if kullanici_secimi == bilgisayar_secimi:
        print("Berabere")
    
    elif kullanici_secimi == "Taş" and bilgisayar_secimi == "Makas":
        print("Kazandınız!")
        kullanici_skor += 1
    
    elif kullanici_secimi == "Taş" and bilgisayar_secimi == "Kağıt":
        print("Bilgisayar kazandı!")
        bilgisayar_skor += 1
    
    elif kullanici_secimi == "Kağıt" and bilgisayar_secimi == "Taş":
        print("Kazandınız!")
        kullanici_skor += 1
    
    elif kullanici_secimi == "Kağıt" and bilgisayar_secimi == "Makas":
        print("Bilgisayar kazandı!")
        bilgisayar_skor += 1
    
    elif kullanici_secimi == "Makas" and bilgisayar_secimi == "Taş":
        print("Bilgisayar kazandı!")
        bilgisayar_skor += 1

    elif kullanici_secimi == "Makas" and bilgisayar_secimi == "Kağıt":
        print("Kullanıcı kazandı!")
        kullanici_skor += 1

    if kullanici_skor == 3:
        print("Tebrikler! Oyunu kazandınız.")
        break

    elif bilgisayar_skor == 3:
        print("Kaybettiniz!")
        break
