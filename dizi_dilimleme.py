import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[4:]) # 4'ten sonra dizinin sonuna kadar dilimler.
print(arr[:4]) # 4'e kadar dilimler.
print(arr[-3:-1]) # Sondan 3. indisten sondan 1. indise kadar dilimler.

print(arr[1:5:2]) # 1. indisten 5. indise kadar her 2 öğeden birini döndürür.
print(arr[::2]) # dizinin tamamındaki her 2 ögeden birini döndürür.

# Boyutlu Dizileri Dilimleme
arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr1[1, 1:4]) # 1. indisten 4. indise kadar ikinci öğeyi dilimler
print(arr1[0:2, 2]) # her iki öğeden 2. indisi döndürür.