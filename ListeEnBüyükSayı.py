# Bu program, kullanıcıdan bir dizi sayı alır ve bu sayılar arasından en büyüğünü bulur.

n = int(input("Kaç sayı girmek istiyorsunuz?"))

sayilar = []

for i in range(n):
    sayi = int(input(f"{1+i}. sayıyı girin: "))
    sayilar.append(sayi)

en_buyuk = max(sayilar)
print(f"Girdiğniiz sayılar arasında en büyüğü: {en_buyuk}")