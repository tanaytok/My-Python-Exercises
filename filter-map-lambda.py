# map, filter ve lambda fonksiyonlar.

# map: bir işlemi tüm diziye yapmanızı sağlar
# lambda: bir işlemi seçtiğiniz şeylere tek satırda yapmanızı sağlar
# filter: lambda ile beraber kullanılarak bir filtreleme yapmanıza yarar

sayilar = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

# Her sayının 3 katını alın:

uc_kat = list(map(lambda x: x *3, sayilar))

# Sadece 5'in katları olan sayılar

bes_kat = list(filter(lambda x: x % 5 == 0, sayilar))

# 5'in katı olanları 3 ile çarpalım

ujbej = list(map(lambda x: x * 3, filter (lambda x: x % 5 == 0, sayilar)))

print("5'in katı olan sayıların 3 katı: ", ujbej)