
file = "epreuve6/test.txt"
file2 = "epreuve6/input2.txt"


# Création de la matrice
matrice = []
for i in range(700):
    mtmp = []
    for j in range(3200):
        mtmp.append([])
    matrice.append(mtmp)



def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

with open(file, 'r') as f:
    i = 0
    j = 0

    fichier = f.readlines()

    
    # mat = []
    # for i in fichier:
    #     mat.append(i.split(' '))
    # for i in range(len(mat)):
    #     for j in range(len(mat[i])):
    #         if '\n' in mat[i][j]:
    #             mat[i][j] = mat[i][j].replace('\n', '')

    matricetriplet = []

    for i in fichier:
        matricetriplet.append(i.split(' '))
    for i in range(len(matricetriplet)):
        for j in range(len(matricetriplet[i])):
            if '\n' in matricetriplet[i][j]:
                matricetriplet[i][j] = matricetriplet[i][j].replace('\n', '')

    matriceptn = []

    for i in range(700):
        matriceptn.append(list(split(matricetriplet[i], 3200)))


with open(file2, 'r') as f2:
    input = f2.readlines()
    for i in range(75209):
        change = input[i].split(';')
        change[1] = change[1].replace('\n', '')
        for j in range(700):
            matriceptn[j][int(change[0])], matriceptn[j][int(change[1])] = matriceptn[j][int(change[1])], matriceptn[j][int(change[0])]  # noqa: E501

with open("res.txt", 'w') as f:
    for i in matriceptn:
        for j in i:
            for k in j:
                f.write(str(k) + ' ')
        f.write('\n')
                
# with open(file2, 'r') as f2:
#     input = f2.readlines()
#     for i in range(75209):
#         change = input[i].split(';')
#         change[1] = change[1].replace('\n', '')
#         for j in range(700):
#             mat[j][int(change[0])], mat[j][int(change[1])] = mat[j][int(change[1])], mat[j][int(change[0])]  # noqa: E501
#             mat[j][int(change[0])+1], mat[j][int(change[1])+1] = mat[j][int(change[1])+1], mat[j][int(change[0])+1]  # noqa: E501
#             mat[j][int(change[0])+2], mat[j][int(change[1])+2] = mat[j][int(change[1])+2], mat[j][int(change[0])+2]  # noqa: E501

# with open("res.txt", 'w') as f:
#     for i in mat:
#         for j in i:
#             f.write(str(j) + ' ')
#         f.write('\n')