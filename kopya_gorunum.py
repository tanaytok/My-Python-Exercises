# kopya yeni bir dizidir. verinin sahibidir. yapılan değişiklikler orj diziyi etkilemez.
# görünüm orijinal dizinin bir görünümüdür. verilere sahip değil. değişiklikler orj diziyi etkiler.

import numpy as np

# COPY İŞLEMİ

arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()
arr[0] = 42
print(arr)
print(copy)

# VIEW İŞLEMİ

arr1 = np.array([1, 2, 3, 4, 5])
view = arr1.view()
arr1[0] = 42
print(arr)
print(view)

# base fonkisyonu = dizinin kendi verisine sahip olup olmadığını kontrol eder

dizi = np.array([1, 2, 3, 4, 5])
adana = dizi.copy()
bursa = dizi.view()
print(adana.base)
print(bursa.base)