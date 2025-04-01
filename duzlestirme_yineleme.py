import numpy as np

# flatten (düzleştirme) = çok boyutlu bir diziyi 1 boyutlu bir diziye dönüştürmek.

arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.reshape(-1) # bunu kullanarak tek boyutlu bir diziye dönüştürebiliriz.
print(new_arr)

# iterating (yineleme) = for döngüsü kullanarak öğeleri tek tek incelemek.
arr1 = np.array([1,2,3])
for x in arr1:
    print(x)

for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)

arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

for x in arr2:
    for y in x:
        for z in y:
            print(z)

# nditer() kullanarak dizileri yineleme

for x in np.nditer(arr2):
    print(x)

# farklı veri türlerinde yineleme

arr4 = np.array([1,2,3])
for x in np.nditer(arr4,flags=['buffered'], op_dtypes=['S']):
    print(x)

# ndenumarate() kullanarak yineleme
arr4 = np.array([1,2,3])
for idx, x in np.ndenumerate(arr4):
    print(idx,x)
