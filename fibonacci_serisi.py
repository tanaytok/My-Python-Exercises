ilksayi = 1
ikincisayi = 1

fibonacci = [ilksayi,ikincisayi]

for i in range(20):
    ilksayi,ikincisayi = ilksayi,ikincisayi + ikincisayi
    fibonacci.append(ikincisayi)

print(fibonacci)