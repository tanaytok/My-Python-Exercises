sozluk = {"Ad" : "Merve"}
sozluk["Soyad"] = "Kılıç"
sozluk["Yaş"] = 24

print(sozluk)

del sozluk["Soyad"]
print(sozluk)

sozluk.clear()
print(sozluk)

baskentler={"Avusturya":"Viyana","Almanya":"Berlin","Hollanda":"Amsterdam"}
baskentler.pop("Hollanda")
print(baskentler)

baskentler.popitem()
print(baskentler)

# 10'a kadar olan sayılardan ve küplerinden oluşan bir sözlük oluşturalım.

kup = {x: x ** 3 for x in range(10)}
print(kup)
print(kup.keys())
print(kup.values())

for i in kup.items():
    print('{} sayısı {} sayısının küpüdür.'.format(i[0], i[1]))

# for döngüsü kullanarak bir dizinin içindeki sayıların toplamını ve ortalamasını bulan program

dizi=[40,50,60,70,30]
toplam = 0
ortalama = 0

for i in range(1,len(dizi)):
    toplam += dizi[i]

ortalama = toplam / len(dizi)

print("Ortalama: ",ortalama)
print("Toplam: ", toplam)