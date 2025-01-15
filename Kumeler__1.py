iller = {"İstanbul", "Niğde", "Ankara", "Bursa"}
print(iller)

x = set("ADANA")
print(x)

iller.add("Hatay")
iller.update("Manisa", "Eskişehir")
print(iller)

iller.clear()
print(iller)

iller = x.copy()
print(iller)

a={"a","b","c","d","e"}
b={"b","c"}
c={"c","d"}

print(a.difference(b))
print(a.difference(c))
print(a.symmetric_difference(b))
print(b.isdisjoint(c))
print(b.isdisjoint(iller))


