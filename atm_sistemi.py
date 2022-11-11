print("*********\nATM Sistemine Hosgeldiniz\n*********")
print("""
İslemler:
1. Bakiye Sorgulama
2. Para Yatirma
3. Para Cekme

Programdan 'q' tusu ile cikabilirsiniz.

""")

bakiye = 1000

while True:
    islem = input("Lütfen İşlem Giriniz: ")

    if (islem == "q"):
        print("Yine Bekleriz...")
        break

    elif (islem == "1"):
        print("Bakiyeniz {} TL'dir.".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak İstediğiniz Miktar: "))
        bakiye += miktar
    elif (islem == "3"):
        miktar = int(input("Çekmek İstediğiniz Miktar: "))
        if (bakiye - miktar < 0 ):
            print("Çekmek istediğiniz miktar bakiyenizi aşıyor!")
            print("Bakiyeniz {} TL'dir.".format(bakiye))
            continue
        bakiye -= miktar
    else:
        print("Geçerli Bir İşlem Giriniz!")
