#Napisi program koji ispisuje cjelobrojne elemente koji se pojavljuju 3 ili vise puta unutar
#liste. Generiraj listu od 100 elemenata u rasponu vrijednosti od 0 do 30. 
import random
from collections import Counter
lista=[]
for x in range (0,100):
    lista.append(random.randint(0,30))

elementi=Counter(lista)

rezultat=[broj for broj, brojanje in elementi.items() if brojanje>=1]

print(rezultat)