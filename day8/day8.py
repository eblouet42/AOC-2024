file=open("C:/Users/evanb/AOC-2024/day8/input.txt").read().split("\n")[:-1]
L=[]
Y=len(file)
X=len(file[0])
for i in range(ord("z")+1):
    L.append([])
for j in range(Y):
    for i in range(X):
        char=file[j][i]
        if char!=".":
            L[ord(char)].append((i,j))
antinode=set()
for frequence in L:
    for node1 in frequence:
        for node2 in frequence:
            if node1!=node2:
                ant=(node2[0]+(node2[0]-node1[0]),node2[1]+(node2[1]-node1[1]))
                if ant[0]>=0 and ant[0]<X and ant[1]>=0 and ant[1]<Y:
                    antinode.add(ant)
print(len(antinode))

for frequence in L:
    for node1 in frequence:
        for node2 in frequence:
            if node1!=node2:
                out=False
                i=0
                while not(out):
                    ant=(node2[0]+(node2[0]-node1[0])*i,node2[1]+(node2[1]-node1[1])*i)                    
                    if ant[0]>=0 and ant[0]<X and ant[1]>=0 and ant[1]<Y:
                        antinode.add(ant)
                        i+=1
                    else:
                        out=True
print(len(antinode))