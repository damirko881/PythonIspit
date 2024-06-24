#Za danu listu stringova, vrati rječnik čiji će ključevi biti znakovi iz stringova, a vrijednosti 
#lista stringova koji sadrže taj znak po redoslijedu pojavljivanja u originalnom stringu. 
#Napravite vlastitu funkciju, 
#Npr. za listu ['dobar','dan'] će se dobiti rječnik 
# {'d': ['dobar', 'dan'], 'o': ['dobar'],'b':['dobar'],'a':['dobar', 'dan'], 'r': ['dobar'], 'n': ['dan']} 

def znakovi_u_stringovima(listaStringova):
    rezultat = {}

    for string in listaStringova:
        for znak in string:
            if znak in rezultat:
                if string not in rezultat[znak]:
                    rezultat[znak].append(string)
            else:
                rezultat[znak] = [string]

    return rezultat

listaStringova = ['dobar', 'dan']

rezultat = znakovi_u_stringovima(listaStringova)
print(rezultat)
