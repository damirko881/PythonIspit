# Za danu listu stringova vrati broj stringova iz liste kojima je duljina >=3 i koji imaju barem
# dvije znamenke jednake prvoj znamenci.
# Npr. za listu ['abc', 'aba', 'cc', 'ijki'] će vratiti 2

lista=['abc', 'aba', 'cc', 'ijki']

brojac=0

for rijec in lista:
    pocetnoSlovo=rijec[0]
    if(len(rijec)>=3):
        flag=False
        for slovo in rijec[1:]:
            if(pocetnoSlovo==slovo):
                flag=True
        if(flag==True):
            brojac+=1

print(brojac)