import numpy as np
file=open("C:/Users/evanb/AOC-2024/day 1/input.txt").readlines()
left=[]
right=[]
count=0
for ligne in file:
    truc=ligne.split("   ")
    left.append(int(truc[0]))
    right.append(int(truc[1]))
left.sort()
right.sort()
for i in range(len(left)):
    count+=abs(left[i]-right[i])
print(count)
count=0
for i in range(len(left)):
    mult=0
    for j in range(len(right)):
        if (left[i]==right[j]):
            mult+=1
    count+=left[i]*mult
print(count)