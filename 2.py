#Napisati Python funkciju koja filtrira vrijednosti rjecnika na osnovu visine i kao rezultat 
#daje novi rjecnik. Argumenti funkcije trebaju biti rjecnik, i visina po kojoj se filtrira. 
#(primjer: filtrira sve osobe koje su vece od odredene visine)

rijecnik={"Pero Peric":175, "Marko Markic":180, "Jure Juric":165,"Marija Maric":190}

def filter(rijecnik, minVisina):
    noviRijecnik={}
    for ime, visina, in rijecnik.items():
        if visina>=minVisina:
            noviRijecnik[ime]=visina
            
    return noviRijecnik
    
print(filter(rijecnik, 100))
