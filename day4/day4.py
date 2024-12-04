file=open("C:/Users/evanb/AOC-2024/day4/input.txt").read().split("\n")[0:-1]
count=0
directions=[(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
Y=len(file)
X=len(file[0])
for i in range(Y):
    for j in range(X):
        if (file[i][j])=="X":
            for direction in directions:
                (dx,dy)=direction
                if (i+(3*dy)<Y) and (i+(3*dy)>=0) and (j+(3*dx)<X) and (j+(3*dx)>=0) and file[i+dy][j+dx]=='M' and file[i+2*dy][j+2*dx]=='A' and file[i+3*dy][j+3*dx]=='S':
                    count+=1
print(count)
count=0
for i in range(Y):
    for j in range(X):
        if (file[i][j])=="A":
            if (i+1<Y) and (i-1>=0) and (j+1<X) and (j-1>=0) and ((file[i-1][j-1]=='M' and file[i+1][j+1]=='S') or (file[i-1][j-1]=='S' and file[i+1][j+1]=='M')) and ((file[i-1][j+1]=='M' and file[i+1][j-1]=='S') or (file[i-1][j+1]=='S' and file[i+1][j-1]=='M')):
                count+=1
print(count)