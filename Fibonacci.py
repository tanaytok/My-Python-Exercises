# Bu program, Fibonacci serisindeki belirli sayıda terimi hesaplar.

terim_sayisi = int(input("Kaç terim hesaplanacak: "))
fibonacci = [0,1]

for i in range(2,terim_sayisi):
    yeni_terim = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(yeni_terim)

print(f"İlk {terim_sayisi} Fibonacci terimi: {fibonacci}")
