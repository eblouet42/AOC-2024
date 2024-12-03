file=open("C:/Users/evanb/AOC-2024/day3/input.txt").read()
count=0
do=True
for i in range(len(file)-8):
    if file[i:i+4]=="do()":
        do=True
    elif file[i:i+7]=="don't()":
        do=False
    elif (file[i:i+4]=="mul(" and do):
        chiffre1=0
        chiffre2=0
        j=0
        virgule=False
        while (i+4+j<len(file)-1) and (file[i+4+j]!=','):
            j+=1
            if (file[i+4+j]==','):
                virgule=True
        if virgule:
            nombre=True
            for n in range(i+4,i+4+j):
                if file[n] not in ["0","1","2","3","4","5","6","7","8","9"]:
                    nombre=False
            if nombre:
                chiffre1=int(file[i+4:i+4+j])
        j2=0
        parenthese=False
        while (i+5+j+j2<len(file)-1) and (file[i+5+j+j2]!=")"):
            j2+=1
            if (file[i+5+j+j2]==")"):
                parenthese=True
        if parenthese:
            nombre=True
            for n in range(i+5+j,i+5+j+j2):
                if file[n] not in ["0","1","2","3","4","5","6","7","8","9"]:
                    nombre=False
            if nombre:
                chiffre2=int(file[i+5+j:i+5+j+j2])
        count+=chiffre1*chiffre2
print(count)
        
            
            
        
        