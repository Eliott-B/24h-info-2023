
seq = 1113122113

seq = [int(i) for i in str(seq)]
print(seq)

def tourliste(entree : list) -> list:
    res = []
    charcourant = entree[0]
    tmp = [charcourant, 0]
    for i in entree:
        # print(i)
        if i == charcourant:
            tmp[1] += 1
        else:
            # print(tmp)
            res.append(tmp[1])
            res.append(tmp[0])
            tmp = [i, 1]
            charcourant = i
            # print(tmp)
    
    res.append(tmp[1])
    res.append(tmp[0])

    return res

def tour(entree : int) -> int:
    res = ""
    charcourant = str(entree)[0]
    tmp = [charcourant, 0]
    for i in str(entree):
        # print(i)
        if i == charcourant:
            tmp[1] += 1
        else:
            # print(tmp)
            res += str(tmp[1]) + str(tmp[0])
            tmp = [i, 1]
            charcourant = i
            # print(tmp)
    res += str(tmp[1]) + str(tmp[0])
    return int(res)
        
        
# print(tour(1113122113))

# 111 3 1 22 11 3

# 31 13 11 22 21

for i in range(50):
    seq = tourliste(seq)

reslen = len(seq)

print(len(seq), len(seq) == 360154)
# seq=list(filter(lambda i:(i),str(seq)))
# newSeq = ""
# i = 0
# while i != 50:
#     tmp = 0
#     for j in range(3):
#         if int(seq[i+j]) != int(seq[i+j-1]) and j != 0:
#             i = j
#             break
#         tmp += 1
#     newSeq += str(tmp) + seq[i-1]
# print(newSeq)
        
print("CODE :", (11+1)*reslen)