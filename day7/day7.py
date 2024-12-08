def rec_eq(tot,nb):
    if len(nb)==1:
        return tot==int(nb[0])
    else:
        return (rec_eq(tot/int(nb[len(nb)-1]),nb[:-1]) or rec_eq(tot-int(nb[len(nb)-1]),nb[:-1]))

def rec_eq2(tot,nb):
    if tot<=0:
        return False
    elif len(nb)==1:
        return tot==int(nb[0])
    else:
        n=len(nb[-1])
        if str(tot)[-n:]==nb[-1] and str(tot)!=nb[-1]:
            if tot/int(nb[len(nb)-1])%1==0:
              return (rec_eq2(tot//int(nb[len(nb)-1]),nb[:-1]) or rec_eq2(tot-int(nb[len(nb)-1]),nb[:-1]) or rec_eq2(int(str(tot)[:-n]),nb[:-1]))
            else:
                return(rec_eq2(tot-int(nb[len(nb)-1]),nb[:-1]) or rec_eq2(int(str(tot)[:-n]),nb[:-1]))  
        else:
            if tot/int(nb[len(nb)-1])%1==0:
              return (rec_eq2(tot//int(nb[len(nb)-1]),nb[:-1]) or rec_eq2(tot-int(nb[len(nb)-1]),nb[:-1]))
            else:
                return(rec_eq2(tot-int(nb[len(nb)-1]),nb[:-1])) 

file=open("C:/Users/evanb/AOC-2024/day7/input.txt").read().split("\n")[:-1]
count=0
for eq in file:
    tot=int(eq.split(":")[0])
    nb=eq.split(" ")[1:]
    if rec_eq(tot,nb):
        count+=tot
print(count)

count=0
for eq in file:
    to=int(eq.split(":")[0])
    nb=eq.split(" ")[1:]
    if rec_eq2(to,nb):
        count+=to
print(count)