# Özyinelemeli fonksiyon ile Faktoriyel Hesaplama

def faktoriyel(n):

    if n == 0 or n == 1:
        return 1
    
    else:
        return n * faktoriyel(n-1)
    
sayi = int(input("Bir sayı giriniz: "))
sonuc = faktoriyel(sayi)
print(f"{sayi}! = {sonuc}")