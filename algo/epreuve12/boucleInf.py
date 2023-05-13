seq = 1113122113

seq=list(filter(lambda i:(i),str(seq)))
newSeq = ""
i = 0
while i != 40:
    tmp = 0
    for j in range(3):
        if int(seq[i+j]) != int(seq[i+j-1]) and j != 0:
            i = j
            break
        tmp += 1
    newSeq += str(tmp) + seq[i-1]
print(len(newSeq))