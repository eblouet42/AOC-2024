file=open("C:/Users/evanb/AOC-2024/day5/input.txt").read().split("\n")
rules=file[0:1176]
updates=file[1177:1381]
import numpy as np

rulesmat=np.full((100,100),False)
for rule in rules:
    [x,y]=rule.split("|")
    rulesmat[int(x),int(y)]=True

count=0
for update in updates:
    ok=True
    numbers=update.split(',')
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if rulesmat[int(numbers[j]),int(numbers[i])]:
                ok=False
    if ok:
        count+=int(numbers[len(numbers)//2])
print(count)

count=0
for update in updates:
    ok=True
    numbers=update.split(',')
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if rulesmat[int(numbers[j]),int(numbers[i])]:
                ok=False
    if not ok:
        truc=numbers
        while(not(ok)):
            ok=True
            for i in range(len(truc)):
                for j in range(i+1,len(truc)):
                    if rulesmat[int(truc[j]),int(truc[i])]:
                        ok=False
                        cop=[]
                        for k in range(len(truc)):
                            if k==i:
                                cop.append(truc[j])
                            elif k==j:
                                cop.append(truc[i])
                            else:
                                cop.append(truc[k])
                        truc=cop
        count+=int(truc[len(truc)//2])
print(count)
