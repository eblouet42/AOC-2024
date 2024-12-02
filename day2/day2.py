def estSafe(sample):
    increasing=False
    decreasing=False
    L=sample.split(" ")
    valide=True
    for i in range(len(L)-1):
        if int(L[i+1])>int(L[i]):
            if decreasing or (abs(int(L[i+1])-int(L[i])) not in [1,2,3]):
                valide=False
            else:
                increasing=True
        else:
            if increasing or (abs(int(L[i+1])-int(L[i])) not in [1,2,3]):
                valide=False
            else:
                decreasing=True
    return(valide)

file=open("C:/Users/evanb/AOC-2024/day2/input.txt").read().split("\n")
count=0
for sample in file:
    count+=estSafe(sample)
print(count)
count=0
for i in range(len(file)-1):
    L=file[i].split(" ")
    l=[]
    for i in range(len(L)):
        li=""
        for j in range(len(L)):
            if j!=i:
                li+=L[j]+" "
        l.append(li[0:(len(li)-1)])
    valide=False
    for sample in l:
        if estSafe(sample):
            valide=True
    count+=valide
print(count)
    
