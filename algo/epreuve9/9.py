danseur = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

file = "epreuve9/salle9.txt"

def rotation(taille: int, danseur: list) -> list[str]:
    newList = danseur.copy()
    for i in range(len(danseur)):
        newList[(i+taille)%len(danseur)] = danseur[i]
    return newList

def echangeIndice(indice1: int, indice2: int, danseur: list) -> list[str]:
    newList = danseur.copy()
    newList[indice1] = danseur[indice2]
    newList[indice2] = danseur[indice1]
    return newList

def echangeDanseur(danseur1: str, danseur2: str, danseur: list) -> list[str]:
    newList = danseur.copy()
    newList[danseur.index(danseur1)] = danseur[danseur.index(danseur2)]
    newList[danseur.index(danseur2)] = danseur[danseur.index(danseur1)]
    return newList

# res = danseur.copy()
# for i in range(5):
    
#     res = rotation(1, res)
#     print(res)

# res = echangeIndice(0, 1, res)
# print(res)
# res = echangeDanseur('a', 'g', res)
# print(res)

with open(file, 'r') as f:
    fichier = f.read().split(',')
    res = danseur.copy()
    for i in range(1000000000):
        for j in fichier:
            if j[0] == 's':
                res = rotation(int(j[1:]), res)
            elif j[0] == 'x':
                res = echangeIndice(int(j[1:j.index('/')]), int(j[j.index('/')+1:]), res)
            elif j[0] == 'p':
                res = echangeDanseur(j[1], j[3], res)
#  lmndopaecbfghijk
    
    