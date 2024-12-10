def trailhead(i,j,k,S):
    if k==9:
        S.add(str((i,j)))
    else:
        Voisins=[]
        if (i+1)<len(file[0]) and int(file[j][i+1])==k+1:
            Voisins.append((i+1,j))
        if (i-1)>=0 and int(file[j][i-1])==k+1:
            Voisins.append((i-1,j))
        if (j+1)<len(file) and int(file[j+1][i])==k+1:
            Voisins.append((i,j+1))
        if (j-1)>=0 and int(file[j-1][i])==k+1:
            Voisins.append((i,j-1))
        for voisin in Voisins:
            trailhead(voisin[0],voisin[1],k+1,S)
            
def trailheadrating(i,j,k):
    if int(file[j][i])!=k:
        return 0
    if k==9:
        return 1
    else:
        Voisins=[]
        if (i+1)<len(file[0]) and int(file[j][i+1])==k+1:
            Voisins.append((i+1,j))
        if (i-1)>=0 and int(file[j][i-1])==k+1:
            Voisins.append((i-1,j))
        if (j+1)<len(file) and int(file[j+1][i])==k+1:
            Voisins.append((i,j+1))
        if (j-1)>=0 and int(file[j-1][i])==k+1:
            Voisins.append((i,j-1))
        countinterne=0
        for voisin in Voisins:
            countinterne+=trailheadrating(voisin[0],voisin[1],k+1)    
        return countinterne

file=open("C:/Users/evanb/AOC-2024/day10/input.txt").read().split("\n")[:-1]
count=0
for j in range(len(file)):
    for i in range(len(file[0])):
        if file[j][i]=="0":
            S=set()
            trailhead(i,j,0,S)
            count+=len(S)
print(count)

count=0
for j in range(len(file)):
    for i in range(len(file[0])):
        if file[j][i]=="0":
            count+=trailheadrating(i,j,0)
print(count)