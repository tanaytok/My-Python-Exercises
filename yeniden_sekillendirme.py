import numpy as np

# reshape fonk. = diziye yeni bir boyut eklemek veya mevcut boyutları kaldırmak için kullanılır.

aylar = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# her birinde 3 eleman bulunan 4 dizi bulunsun
aylar2 = aylar.reshape(4,3)
print(aylar2)

print("###################################################")
# her birinde 2 eleman olan 3 diziden oluşan 2 dizi oluştur
aylar3 = aylar.reshape(2,3,2)
print(aylar3)

print("###################################################")
# Bilinmeyen Boyut
aylar4 = aylar.reshape(2,2,-1)
print(aylar4)

