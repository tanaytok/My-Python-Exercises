import numpy as np

# array_split() kullanılır
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3) # 3'e böl demek
print(newarr)

arr1 = np.array([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12]])
newarr1 = np.array_split(arr1,3)
print(newarr1)