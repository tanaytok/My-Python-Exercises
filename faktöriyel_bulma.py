print("""*******************
Faktoriyel Bulma Programı
Progamdan Çıkmak İçin 'q' ya basın.
*******************
""")
while True:
    sayi = input("Bir Sayı Giriniz: ")
    if (sayi == "q"):
        print("Hoşçakalın...")
        break
    sayi = int(sayi)
    faktoriyel = 1
    for i in range(2,sayi+1):
        faktoriyel *= i
    print("Faktoriyel: ",faktoriyel)
