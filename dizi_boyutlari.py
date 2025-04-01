import numpy as np

# 1-Boyutlu Dizi
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-Boyutlu Dizi
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)

# 3-Boyutlu dizi
arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr2)

# ndim kullanarak boyut belirlemek

arr3 = np.array([1,2,3,4], ndmin = 5)
print(arr3)
print('shape: ', arr3.shape)


# ndim fonksiyonu dizilerin kaç boyutu olduğunu söyler
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)

# shape fonksiyonu dizi boyutunu verir ve a x b matrisini döndürür
print(arr2.shape)

# size fonksiyonu dizideki eleman sayısını verir
print(arr2.size)

# dtype dizideki eleman türünü döndürür
print(arr2.dtype)

arr5 = np.array(['banana', 'apple', 'cherry'])
print(arr5.dtype)
