# Postaviti parametre kružnice (r i koordinate središta (a, i b). Zatim je potrebno učitavati
# 10 točaka koordinatnog sustava (realni brojevi).
#  Za učitane točke provjeriti nalaze li se na kružnici. (25 bodova)
#  Nakon što se učita točka (0, 0), ispisati koliki je omjer pogodaka kružnice ((broj
# točaka na kružnici)/(ukupni broj točaka)) u postotku (25 bodova)
# Formula kružnice : (x-a)2+(y-b)2=r2

import math

r=int(input("Postavite radijus: "))
a=int(input("Postavite koordinate kruznice a: "))
b=int(input("Postavite kooridnate kruznice b: "))

def izracunajRadijus(x,y):
    radijus = math.sqrt((x-a)**2+(y-b)**2)
    return radijus

brojac=0
pogodci=0

for i in range(10):
    print(f"Unesite {i+1}. kordinate")
    x=int(input("Unesite tocku x: "))
    y=int(input("Unesite tocku y: "))

    if(x==0 and y==0):
        omjerPogodaka=(pogodci/brojac)*100
        print("Omjer pogodaka: ", omjerPogodaka, "%")
    else:
        if izracunajRadijus(x,y)>r:
            print("Tocka se nalazi van kruznice!")
            brojac+=1
        else:
            print("Tocka se nalazi unutar kruznice.")
            brojac+=1
            pogodci+=1