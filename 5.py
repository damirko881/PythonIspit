# Robot se kreće po točkama pravokutnog koordinatnog sustava u ravnini, počevši od
# točke (5, 7). Zadana je njegova putanja kao string sastavljen od znakova (npr: „SJIJI“)
#  S (idi sjeverno),
#  J (idi južno),
#  I (idi istočno)
#  Z (idi zapadno)
# Ako korisnik unese S robot će ići na Sjever za 3 točke, a za sve ostale će ići po jednu
# točku. Na primjer, ako je robot u točki (0, 0) nakon naredbe Z putuje u točku (-1, 0), a
# nakon S putuje u točku (0,3). Napišite program koji određuje konačnu poziciju robota za
# proizvoljan broj točaka 

x=5
y=7

putanja=input("Unesite putanju: ")

def kretanje(putanja):
    global x, y

    for slovo in putanja:
        if(slovo=="S" or slovo=="s"):
            y+=3
        elif(slovo=="J" or slovo=="j"):
            y-=1
        elif(slovo=="Z" or slovo=="z"):
            x-=1
        elif(slovo=="I" or slovo=="i"):
            x+=1
        else:
            print("Unesena komanda je nevaljana")
        
    
kretanje(putanja)
print("Trenutne kooridnate su: ", x, y)