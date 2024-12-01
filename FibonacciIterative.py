# Fibonacci iterative yöntem

def fibonacci(n):
    a = 0
    b = 1

    for _i in range(n):
        a, b = b, a + b
    return a

n = int(input("Kaçıncı elemanı hesaplamak isterseniz?"))
print(f"{n}. fibonaccı sayısı: {fibonacci(n)}")