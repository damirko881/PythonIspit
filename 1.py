import random
from collections import Counter
lista=[]
for x in range (0,100):
    lista.append(random.randint(0,30))

elementi=Counter(lista)

rezultat = []
for broj, brojanje in elementi.items():
    if brojanje >= 1:
        rezultat.append(broj)

print(rezultat)
