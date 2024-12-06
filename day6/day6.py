file=open("C:/Users/evanb/AOC-2024/day6/input.txt").read().split("\n")[:-1]
depart=(37,43)
hashset={str(depart)}
visite=[depart]
direction=[(0,-1),(1,0),(0,1),(-1,0)]
pos=depart
i=0
while pos[0]>0 and pos[0]<129 and pos[1]>0 and pos[1]<129:
    destination=(pos[0]+(direction[i%4])[0],pos[1]+(direction[i%4])[1])
    while(file[destination[1]][destination[0]]=="#"):
        i+=1
        destination=(pos[0]+(direction[i%4])[0],pos[1]+(direction[i%4])[1])
    pos=destination
    if (str(pos) not in hashset):
        hashset.add(str(pos))
        visite.append(pos)
print(len(visite))

count=0
for (xp,yp) in visite[1:]:
    copie=[]
    for i in range(len(file)):
        s=""
        for j in range(len(file[i])):
            if (j,i)==(xp,yp):
                s+="#"
            else:
                s+=file[i][j]
        copie.append(s)
    loop=False
    obstaclehashset=set()
    pos=depart
    i=0
    while (pos[0]>0 and pos[0]<129 and pos[1]>0 and pos[1]<129 and (not(loop))):
        destination=(pos[0]+(direction[i%4])[0],pos[1]+(direction[i%4])[1])
        while(copie[destination[1]][destination[0]]=="#" and not(loop)):
            if (str(pos)+str(direction[i%4]) in obstaclehashset):
                loop=True
            else:
                obstaclehashset.add(str(pos)+str(direction[i%4]))
                i+=1
                destination=(pos[0]+(direction[i%4])[0],pos[1]+(direction[i%4])[1])
        pos=destination
    count+=loop
print(count)