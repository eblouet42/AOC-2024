file=open("C:/Users/evanb/AOC-2024/day12/input.txt").read().split("\n")[:-1]

def zone(c,i,j,visitetot):
    ZoneVisiteHashSet=set()
    ZoneVisiteList=[]
    ZoneAVisite=[]
    ZoneAVisite.append((i,j))
    while len(ZoneAVisite)!=0:
        parcelle=ZoneAVisite.pop()
        if file[parcelle[1]][parcelle[0]]==c:
                ZoneVisiteHashSet.add(str(parcelle))
                ZoneVisiteList.append((parcelle[0],parcelle[1]))
                visitetot.add(str(parcelle))
                voisins=[]
                voisins.append((parcelle[0]-1,parcelle[1]))
                voisins.append((parcelle[0]+1,parcelle[1]))
                voisins.append((parcelle[0],parcelle[1]-1))
                voisins.append((parcelle[0],parcelle[1]+1))
                for voisin in voisins:
                    if voisin[0]>=0 and voisin[0]<len(file[0]) and voisin[1]>=0 and voisin[1]<len(file) and str(voisin) not in ZoneVisiteHashSet and voisin not in ZoneAVisite:
                        ZoneAVisite.append(voisin)
    return (ZoneVisiteHashSet,ZoneVisiteList,visitetot)

Visite=set()
ZonesHashSets=[]
ZonesLists=[]
for j in range(len(file)):
    for i in range(len(file[0])):
        if str((i,j)) not in Visite:
            car=file[j][i]
            (ZoneHashSet,ZoneList,Visite)=zone(car,i,j,Visite)
            ZonesHashSets.append(ZoneHashSet)
            ZonesLists.append(ZoneList)

prix=0
for k in range(len(ZonesLists)):
    zone=ZonesLists[k]
    zonebis=ZonesHashSets[k]
    area=len(zone)
    perimeter=0
    for (i,j) in zone:
        perimeter+=(str((i+1,j)) not in zonebis)+(str((i-1,j)) not in zonebis)+(str((i,j+1)) not in zonebis)+(str((i,j-1)) not in zonebis)
    prix+=area*perimeter
print(prix)

prix=0
directions=[(1,0),(0,-1),(-1,0),(0,1)]
for k in range(len(ZonesLists)):
    zone=ZonesLists[k]
    zonebis=ZonesHashSets[k]
    area=len(zone)
    side=0
    voyagefait=set()
    for (i,j) in zone:
        if str((i,j-1)) not in voyagefait and str((i,j-1)) not in zonebis:
            tourne=0
            depart=(i,j-1)
            direction_depart=(1,0)
            position=depart
            assert(depart not in zonebis)
            if str((position[0]+directions[(tourne-1)%4][0],position[1]+directions[(tourne-1)%4][1])) not in zonebis:
                position=(position[0]+directions[(tourne-1)%4][0],position[1]+directions[(tourne-1)%4][1])
                voyagefait.add(str(position))
                tourne-=1
                side+=1
            elif str((position[0]+directions[tourne%4][0],position[1]+directions[tourne%4][1])) not in zonebis:
                position=(position[0]+directions[tourne%4][0],position[1]+directions[tourne%4][1])
                voyagefait.add(str(position))
            else:
                tourne+=1
                side+=1
            while position!=depart or directions[tourne%4]!=direction_depart:
                if str((position[0]+directions[(tourne-1)%4][0],position[1]+directions[(tourne-1)%4][1])) not in zonebis:
                    position=(position[0]+directions[(tourne-1)%4][0],position[1]+directions[(tourne-1)%4][1])
                    voyagefait.add(str(position))
                    tourne-=1
                    side+=1
                elif str((position[0]+directions[tourne%4][0],position[1]+directions[tourne%4][1])) not in zonebis:
                    position=(position[0]+directions[tourne%4][0],position[1]+directions[tourne%4][1])
                    voyagefait.add(str(position))
                else:
                    tourne+=1
                    side+=1
    prix+=area*side
print(prix)