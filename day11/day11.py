file=open("C:/Users/evanb/AOC-2024/day11/input.txt").read().split("\n")[:-1]
L=file[0].split(" ")
for i in range(25):
    Li=[]
    for nb in L:
        n=len(nb)
        if nb=="0":
            Li.append("1")
        elif n%2==0:
            Li.append(str(int(nb[:(n//2)])))
            Li.append(str(int(nb[(n//2):])))
        else:
            Li.append(str(int(nb)*2024))
    L=Li
print(len(L))

M=[]
for i in range(10):
    Mi=[]
    for j in range(76):
        Mi.append(0)
    M.append(Mi)

def boom(c,k):
    if M[int(c)][k]!=0:
        return M[int(c)][k]
    elif k==0 or k==1:
        M[int(c)][k]=1
    elif c=="0":
        M[int(c)][k]=boom("1",k-1)
    elif k<6:
        if k==2:
            if c<"5":
                M[int(c)][k]=2
            else:
                M[int(c)][k]=1
        elif k==3:
            if c<"5":
                M[int(c)][k]=4
            else:
                M[int(c)][k]=2
        elif k==4:
            M[int(c)][k]=4
        elif k==5:
            if c=="4":
                M[int(c)][k]=4
            elif c=="3":
                M[int(c)][k]=5
            elif c=="2":
                M[int(c)][k]=6
            elif c=="1" or c=="8":
                M[int(c)][k]=7
            else:
                M[int(c)][k]=8
    else:
        somme=0
        if c<"5":
            nombre=str(2024*int(c))
            for chiffre in nombre:
                somme+=boom(chiffre,k-3)
        elif c!="8":
            nombre=str(2024*2024*int(c))
            for chiffre in nombre:
                somme+=boom(chiffre,k-5)
        else:
            nombre=str(2024*2024*int(c))
            for i in range(len(nombre)):
                if i!=6:
                    if i==7:
                        somme+=boom(nombre[i],k-4)
                    else:
                        somme+=boom(nombre[i],k-5)
        M[int(c)][k]=somme
    return boom(c,k)
            
L2=file[0].split(" ")
count=0
for i in range(75):
    Li=[]
    for nb in L2:
        n=len(nb)
        if n==1:
            count+=boom(nb,75-i)
        elif n%2==0:
            Li.append(str(int(nb[0:(n//2)])))
            Li.append(str(int(nb[(n//2):])))
        else:
            Li.append(str(int(nb)*2024))
    L2=Li
count+=len(L2)
print(count)

