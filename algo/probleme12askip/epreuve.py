import json
import heapq
json_data = open('probleme12askip/data/data11.json')
data = json.load(json_data)
# print(data[0]['data'])




accumulation = []
print(data[0]['data'][0])
print("############")
for day in range(len(data)):
    accumulation.append(0)
    last_pic = data[day]['data'][0] # dernière accumulation
    start_accu = False
    actuelle_accumulation = 0
    tmp = 0
    for i in range(len(data[day]['data'])):
        # print(data[day]['data'][i], "NIVEAU")
        # si J+1 pas d'écoulement
        # print(i)
        if data[day]['data'][i] >= last_pic:  
            # print("CA MONTE")
            # on change le dernier pic
            last_pic = data[day]['data'][i]
            # donc pas d'accumulation 
            start_accu = False

            # on ajoute l'accumulation potentielle à l'accumulation actuelle
            actuelle_accumulation += tmp
            tmp = 0

        # si J+1 écoulement
        elif data[day]['data'][i-1] - data[day]['data'][i] > 0 or start_accu == True or data[day]['data'][i-1] < last_pic: 
            # on commence l'accumulation potentielle
            start_accu = True
            # print("CA DESCEND")

            # on ajoute l'accumulation potentielle
            tmp += last_pic - data[day]['data'][i-1]
        # print("TMP : ", tmp)
    accumulation[day] = actuelle_accumulation
        

print(accumulation)


# Jour problématique = variation de plus de 1000m3

jours_problematiques = []

for i in range(len(accumulation)):
    if accumulation[i] - accumulation[i-1] >= 1000:
        jours_problematiques.append(i)

print(jours_problematiques)
print(len(jours_problematiques))

for i in jours_problematiques:
    # print()
    print(data[accumulation.index(accumulation[i])]['code'], end='')

# SUJET 11  : 0 E 0 4 1 6 E 7 7 7
# SUJET 3 :   9 E 3 1 7 6 5 6 8 B

# 0E 04 16 E7 77 09 31 D9 99 15

# 30 à 39 : 0 à 9
# 41 à 5A : A à Z
# 61 à 7A : a à z

# quels caratères peuvent manquer pour que le code soit valide ?
# 9B3003C9B4717740C
