# Ortalama Hesaplama Uygulaması

ders_sayisi = int(input("Kaç adet dersiniz var?"))

notlar = []
toplam = 0

for i in range (ders_sayisi):
    not_deg = float(input(f"{i+1}. dersin notunu girin: "))
    notlar.append(not_deg)
    toplam = toplam + not_deg

ortalama = toplam / ders_sayisi
print(f"Ortalamanız: {ortalama:.2f}")

if ortalama >= 50:
    print("Tebrikler! Geçtiniz.")
else:
    print("Maalesef kaldınız!")