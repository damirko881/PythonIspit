# Kreirati listu prirodnih brojeva od 50 elemenata (koristiti random funkciju). Za danu
# listu prirodnih brojeva stvori rječnik u kojemu će se nalaziti frekvencija pojavljivanja
# određene brojčane znamenke u svim brojevima iz liste
# Npr. za [423, 54, 45] broj 4 se pojavljuje 3 puta, 2 - 1 put, 3 -1 put, itd
# Napomena: ključevi rječnika neka budu brojevi, a ne stringovi. 

from random import randint

lista=[]

for num in range(50):
    broj=randint(1,1000)
    lista.append(broj)

frekvencijaZnamenki = {}
for i in range(10):
    frekvencijaZnamenki[i] = 0

for broj in lista:
    for zanmenka in str(broj):
        frekvencijaZnamenki[int(zanmenka)]+=1

print(lista)
print(frekvencijaZnamenki)
