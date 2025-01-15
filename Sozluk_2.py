# Aynı şehirde yaşayan kişiler.

# Küme kullanarak

sehirler = {"İstanbul", "Ankara", "İzmir"}
yeni_sehirler = {"Bursa", "Ankara", "İstanbul"}

print(sehirler.intersection(yeni_sehirler))

# Sözlük kullanarak

kisiler = {
"Ali": "İstanbul",
"Ayşe": "Ankara",
"Fatma": "İzmir"
}
aranan_sehir = "İstanbul"

sonuc = [isim for isim, sehir in kisiler.items() if sehir == aranan_sehir]
print(sonuc)