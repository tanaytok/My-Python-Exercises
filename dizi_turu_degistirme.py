import numpy as np

# astype() dizinin kopyasını oluşturur ve girilen parametre ile veri tipini değiştirir.

arr = np.array([1.1, 2.1, 3.6])
new_arr = arr.astype('i')
print(new_arr)
print(new_arr.dtype)

arr1 = np.array([1.1, 2.1, 3.6])
new_arr1 = arr1.astype(bool)
print(new_arr1)
print(new_arr1.dtype)