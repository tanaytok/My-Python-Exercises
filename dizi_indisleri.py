import numpy as np

# 1-Boyutlu dizilerde erişim
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print(arr[-1])

# 2-Boyutlu dizilerde erişim
arr1 = np.array([[1, 2, 3, 4, 5],[6,7,8,9,10]])
print(arr1[0,1])
print(arr1[1,0])
print(arr1[1,-1])

# 3-Boyutlu dizilerde erişim
arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr2[0,1,2])

