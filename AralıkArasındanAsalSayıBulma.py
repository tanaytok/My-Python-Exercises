# İki sayı arasından asal olanı bulma

def asal_mi(sayi):

    if sayi < 2:
        return False

    for i in range(2, int(sayi ** 0.5) + 1): # Kareköküne kadar kontrol ediyor.
        if sayi % i:
            return False
    return True

baslangic = int(input("Birinci sayıyı giriniz: "))
bitis = int(input("İkinci sayıyı giriniz: "))

print(f"{baslangic} ile {bitis} arasındaki asal sayılar: ")
for sayi in range(baslangic, bitis + 1):
    if asal_mi(sayi):
        print(sayi, end= " ")
        