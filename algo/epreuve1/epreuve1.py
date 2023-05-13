#J1
#J2

J1 = [] # mémoire S
J2 = [] # mémoire Z
ptJ1 = 0 # point j1
ptJ2 = 0

# - supprimer n° le + grand (Z) *
# - supprimer n° médian de la MEMOIRE (S)


file = "epreuve1/fileepreuve.txt"
    
history = list()

with open(file, 'r') as f:
    for i in f:
        

        j = i.replace("\n", "")
        j = int(j)
        history.append(j)
        
        # Statégie J1  ###############SVATISKA################
        # SUPPRIMER PLIUS PETIT ELEMENT
        if j in J1: # si l'élément est dans la mémoire
            ptJ1 += 1 # on ajoute un point
        else: # si l'élément n'est pas dans la mémoire
            if len(J1) == 5:
                J1.remove(min(J1)) # on enlève l'élément le plus petit
            J1.append(j) # on ajoute le nouvel élément
        # print("J1",J1)
        
        # Statégie J2 #############ZINZOLINA################ 
        # SUPPRIMER LE NUMERO QUI N'A PAS ETE TIRE DEPUIS LE PLUS LONGTEMPS 
           
        if j in J2: # si l'élément est dans la mémoire
            ptJ2 += 1 # on ajoute un point
        else:
            if len(J2) == 5:
                # recpère le numéro qui n'a pas été tiré depuis le plus longtemps dans
                # history
                # et on l'enlève de J2
                last = J2[0] 
                tmp = history.copy()
                tmp.reverse()
                for mem in J2:
                    if tmp.index(mem) > tmp.index(last): # si l'index de mem est plus
                        #grand que l'index de last (donc plus vieux)
                        last = mem
                J2.remove(last)
            J2.append(j) # on ajoute le nouvel élément
                        




        # print("J2",J2)
        
        
            
        
        
print("CODE :", (ptJ2+2)*(ptJ1+3))