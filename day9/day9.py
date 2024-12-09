diskmap=open("C:/Users/evanb/AOC-2024/day9/input.txt").read().split("\n")[:-1][0]
L=[]
i=0
while i<len(diskmap):
    if i%2==0:
        for j in range(int(diskmap[i])):
            L.append(str(i//2))
    else:
        for j in range(int(diskmap[i])):
            L.append(".")
    i+=1

i=0
j=len(L)-1
while i<j:
     if L[i]=="." and L[j]!=".":
         L[i]=L[j]
         L[j]="."    
         j-=1
     elif L[i]==".":
        j+=-1
     else:
        i+=1

count=0
for i in range(len(L)):
    if L[i]!=".":
        count+=i*int(L[i])
print(count)

L=[]
i=0
while i<len(diskmap):
    if i%2==0:
        L.append((str(i//2),int(diskmap[i])))
    else:
        L.append((".",int(diskmap[i])))
    i+=1
    
j=len(L)-1
while j>0:
    if L[j][0]==".":
        j-=1
    else:
        i=1
        bouge=False
        while i<j and not(bouge):
            if L[i][0]=="." and L[i][1]>=L[j][1]:
                if L[i][1]==L[j][1]:
                    L[i]=L[j]
                else:
                    L[i]=(".",L[i][1]-L[j][1])
                    L.insert(i,L[j])
                    j+=1
                L[j]=(".",L[j][1])
                bouge=True
            else:
                i+=1
        if not(bouge):
            j-=1
L2=[]
for (a,b) in L:
    for i in range(b):
        L2.append(a)
count=0
for i in range(len(L2)):
    if L2[i]!=".":
        count+=i*int(L2[i])
print(count)
                    
                
        
