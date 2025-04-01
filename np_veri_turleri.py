import numpy as np

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)

a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)

# Tanımlı Veri Türüne Sahip Dizi Oluşturma

dizi = np.array([12, 200, 3500, 40000, 5], dtype = 'S')
print(dizi)
print(dizi.dtype)

dizi1 = np.array([12, 200, 3500, 40000, 5], dtype = 'int')
print(dizi1)
print(dizi1.dtype)

# b = bool
# i = tam sayı
# u = işaretsiz tam sayı
# f = kayan nokta
# c = karmaşık kayan nokta
# m = timedelta
# M = tarih saat
# O = Nesneler
# S = byte dizisi
# U = unicode
# V = ham veriler