# Mükemmel Sayı Bulma

def mukemmel_sayi(sayi):

    toplam = 0

    # Mükemmel sayı bulma fonksiyonu

    for i in range(1, sayi):

        if sayi % i:
            toplam = toplam + i
    return toplam == sayi

baslangic  = int(input("Başlangıç değeri: "))
bitis = int(input("Bitiş değeri: "))

print(f"{baslangic} ile {bitis} değerleri arasındaki mükemmel sayılar: ")

for sayi in range(baslangic, bitis + 1):
    if mukemmel_sayi(sayi):
        print(sayi, end=" ")


