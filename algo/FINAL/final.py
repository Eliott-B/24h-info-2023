
# dictionnaire avec comme clés les couples coordonnées et comme valeurs les valeurs de la case



# 10;4;9;5;2;6;3;1;8;7
# 5;3;10;2;7;9;1;4;6;8
# 7;6;3;4;2;9;8;10;1;5
# 9;6;3;5;1;7;4;10;8;2
# 8;7;2;3;10;9;6;1;4;5
# 6;8;2;5;4;10;1;9;7;3
# 6;5;3;2;7;9;4;8;10;1
# 9;5;1;2;8;10;6;4;7;3
# 9;2;5;10;3;4;6;7;8;1
# 1;2;8;9;4;10;3;6;5;7

with open("FINAL/affectations1.txt", "r") as f:
    dict = {}
    f = f.split("\n")
    for i in range(len(f)):
        f[i] = f[i].split(";")
    print(f)

    i=1
    j=0
    for line in f:
        
        dict[i, j+1] = line[j]
        j+=1
        i+=1
        


print(dict)
choix = {()}
