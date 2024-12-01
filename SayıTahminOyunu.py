# Sayı tahmin oyunu

import random 

def sayi_tahmin():
    
    rastgele_sayi = random.randint(1,100)
    tahmin_hakki = 10

    while(tahmin_hakki > 0):

        secilen_sayi = int(input("1 ile 100 arasından bir sayı giriniz: "))

        if secilen_sayi < rastgele_sayi:
            print("Daha büyük bir sayı söyleyin!")

        elif secilen_sayi > rastgele_sayi:
            print("Daha küçük bir sayı söyleyin.")
        
        else:
            print("Doğru tahmin ettiniz!")

        tahmin_hakki -= 1

        if tahmin_hakki == 0:
            print("Tahmin hakkınız bitmiştir!")
            print(f"Seçilen sayı {rastgele_sayi} idi.")
            break
            
