# Listenin en küçüğünü bulma (Bubble Sort Algorithm)

def bubble_sort(liste):
    n = len(liste)

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

liste = list(map(int, input("Bir liste giriniz: ").split()))
print("Sıralanmış liste: ", bubble_sort(liste))
