# Bu program, Asal Sayı bulmaya yarar.

sayi = int(input("Bir sayı giriniz: "))

if sayi > 1:

    for i in range(2,sayi):

        if (sayi % i) == 0:
            print(f"Sayı asal değildir!")
            break

        else:
            print(f"{sayi} asal bir sayıdır.")
            break
    else:
        print(f"{sayi} asal bir sayıdır.")