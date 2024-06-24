rijecnik={"Pero Peric":175, "Marko Markic":180, "Jure Juric":165,"Marija Maric":190}

def filter(rijecnik, minVisina):
    noviRijecnik={}
    for ime, visina, in rijecnik.items():
        if visina>=minVisina:
            noviRijecnik[ime]=visina
            
    return noviRijecnik
    
print(filter(rijecnik, 100))