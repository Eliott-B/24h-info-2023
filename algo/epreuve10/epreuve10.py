class Cube:
    
    def __init__(self,redirectionVrai, redirectionFaux, haveBalle: bool, valeur:int) -> None:
        self.valeur = valeur
        self.haveBalle = haveBalle
        self.redirectionFaux : Cube = redirectionFaux
        self.redirectionVrai : Cube = redirectionVrai

    def display(self):
        print("Cube n°:", self.nom, " si vrai =>",self.redirectionVrai , " si faux =>", self.redirectionFaux)

class Balle:
    def __init__(self,energie: int) -> None:
        self.energie = energie

c0 = Cube( None, None, True, 0)
c1 = Cube( None, None, False, 1)
c2 = Cube( None, None, False, 2)
c3 = Cube( None, None, False, 3)
c4 = Cube( c2, None, False, 4)
c5 = Cube( None, c4, False, 5)
c6 = Cube( None, c1, False, 6)
c7 = Cube( None, c6, False, 7)
c8 = Cube( c0, c3, False, 8)
c9 = Cube( c0, c1, False, 9)

c0.redirectionVrai = c2
c0.redirectionFaux = c5

c1.redirectionVrai = c4
c1.redirectionFaux = c2

c2.redirectionVrai = c3
c2.redirectionFaux = c8

c3.redirectionVrai = c7
c3.redirectionFaux = c4

c4.redirectionFaux = c6

c5.redirectionVrai = c6

c6.redirectionVrai = c8

c7.redirectionVrai = c9


balle = Balle(5)

def party():
    chemin = [c0.valeur]
    for _ in range(10000):
        if c0.haveBalle:
            balle.energie *= 13
            if balle.energie%2 == 0:
                c0.redirectionVrai.haveBalle = True
                chemin.append(c0.redirectionVrai.valeur)
            else:
                c0.redirectionFaux.haveBalle = True
                chemin.append(c0.redirectionFaux.valeur)
            c0.haveBalle = False
            
        elif c1.haveBalle:
            balle.energie *= 4

            if balle.energie%13 == 0:
                c1.redirectionVrai.haveBalle = True
                chemin.append(c1.redirectionVrai.valeur)
            else:
                c1.redirectionFaux.haveBalle = True
                chemin.append(c1.redirectionFaux.valeur)
            c1.haveBalle = False
        
        elif c2.haveBalle:
            balle.energie += 2
            
            if balle.energie%5 == 0:
                c2.redirectionVrai.haveBalle = True
                chemin.append(c2.redirectionVrai.valeur)
            else:
                c2.redirectionFaux.haveBalle = True
                chemin.append(c2.redirectionFaux.valeur)
            c2.haveBalle = False
            
        elif c3.haveBalle:
            balle.energie *= 2

            if balle.energie%3 == 0:
                c3.redirectionVrai.haveBalle = True
                chemin.append(c3.redirectionVrai.valeur)
            else:
                c3.redirectionFaux.haveBalle = True
                chemin.append(c3.redirectionFaux.valeur)
            c3.haveBalle = False
        
        elif c4.haveBalle:
            balle.energie += 7
            
            if balle.energie%11 == 0:
                c4.redirectionVrai.haveBalle = True
                chemin.append(c4.redirectionVrai.valeur)
            else:
                c4.redirectionFaux.haveBalle = True
                chemin.append(c4.redirectionFaux.valeur)
            c4.haveBalle = False
            
        elif c5.haveBalle:
            balle.energie *= 21

            if balle.energie%19 == 0:
                c5.redirectionVrai.haveBalle = True
                chemin.append(c5.redirectionVrai.valeur)
            else:
                c5.redirectionFaux.haveBalle = True
                chemin.append(c5.redirectionFaux.valeur)
            c5.haveBalle = False
        
        elif c6.haveBalle:
            balle.energie *= 3
            
            if balle.energie%23 == 0:
                c6.redirectionVrai.haveBalle = True
                chemin.append(c6.redirectionVrai.valeur)
            else:
                c6.redirectionFaux.haveBalle = True
                chemin.append(c6.redirectionFaux.valeur)
            c6.haveBalle = False
            
        elif c7.haveBalle:
            balle.energie += 15

            if balle.energie%17 == 0:
                c7.redirectionVrai.haveBalle = True
                chemin.append(c7.redirectionVrai.valeur)
            else:
                c7.redirectionFaux.haveBalle = True
                chemin.append(c7.redirectionFaux.valeur)
            c7.haveBalle = False
        
        elif c8.haveBalle:
            balle.energie += 1
            
            if balle.energie%7 == 0:
                c8.redirectionVrai.haveBalle = True
                chemin.append(c8.redirectionVrai.valeur)
            else:
                c8.redirectionFaux.haveBalle = True
                chemin.append(c8.redirectionFaux.valeur)
            c8.haveBalle = False
            
        elif c9.haveBalle:
            balle.energie *= 5
            
            if balle.energie%29 == 0:
                c9.redirectionVrai.haveBalle = True
                chemin.append(c9.redirectionVrai.valeur)
            else:
                c9.redirectionFaux.haveBalle = True
                chemin.append(c9.redirectionFaux.valeur)
            c9.haveBalle = False
            
    return chemin

res = party()

def resultat(li: list):
    sum = 0
    for val in li :
        sum+= val
    return sum

    
print(resultat(res))
print(party())

print((11+1)*resultat(res))