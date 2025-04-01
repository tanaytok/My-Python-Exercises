import numpy as np

# concatenate() ile yapılır

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)

arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[1,2,3],[4,5,6]])
arr1231 = np.concatenate((arr3,arr4))
print(arr1231)

# iki boyutlu diziyi satır boyunca birleştirme
satir = np.concatenate((arr3,arr4), axis=1)
print(satir)

# stack ile dizi birleştirme
stack_birlestirme = np.stack((arr1,arr2), axis=1)
print(stack_birlestirme)

# hstack() = satır boyunca birleştirir
# vstack() = sütun boyunca birleştirir
# dstack() = derinlik boyunca birleştirir