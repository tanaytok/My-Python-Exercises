print("*** HESAP MAKİNESİ PROGRAMI ***")
print("********************************")
print("1. İşlem = Toplama")
print("2. İşlem = Çıkarma")
print("3. İşlem = Çarpma")
print("4. İşlem = Bölme")

a = float(input("Birinci sayıyı giriniz: "))
b = float(input("İkinci sayıyı giriniz: "))
islem = input("İşlemi giriniz: ")

if (islem == "1"):
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b))
elif (islem == "2"):
    print("{} ile {} in farkı {} dir.".format (a,b,a-b))
elif (islem == "3"):
    print("{} ile {} in çarpımı {} dir.".format(a,b,a*b))
elif (islem == "4"):
    print("{} ile {} in bölümü {} dir.".format(a,b,a/b))
else:
    print("Geçersiz İşlem!")