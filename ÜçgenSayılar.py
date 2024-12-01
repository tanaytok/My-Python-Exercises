# Bu program üçgen sayıları bulur.

def ucgen_mi(sayi):

    dizi = []

    # Üçgen sayı formülü

    for i in range(1, sayi + 1):
        ucgen_sayi = i * (i + 1) // 2 # Üçgen sayı formülü
        dizi.append(ucgen_sayi)
    return dizi

terim_sayisi = int(input("Kaç tane üçgen sayı hesaplanacak: "))
sonuc = ucgen_mi(terim_sayisi)
print(f"İlk {terim_sayisi} üçgen sayısı: {sonuc}")