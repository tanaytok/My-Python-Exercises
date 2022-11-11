print("Uygulamadan çıkmak için 'q' ya basınız.")
def tambolenleribulma(sayi):
    tambolenler = list()

    for i in range(2,sayi):
        if (sayi % i == 0):
            tambolenler.append(i)
    return tambolenler
while True:
    print("Tam bölenlerini bulmak istediğiniz sayıyı giriniz.")
    sayi = input("Sayı: ")

    if (sayi == "q"):
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam Bölenler: ",tambolenleribulma(sayi))

