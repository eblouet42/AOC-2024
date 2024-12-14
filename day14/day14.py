file=open("C:/Users/evanb/AOC-2024/day14/input.txt").read().split("\n")[:-1]
X=101
Y=103
robots=[]
for machin in file:
    robot=[]
    truc=machin.split("=")
    trucp=truc[1].split(",")
    x=int(trucp[0])
    y=int(trucp[1].split(" ")[0])
    robot.append((x,y))
    trucv=truc[2].split(",")
    vx=int(trucv[0])
    vy=int(trucv[1])
    robot.append((vx,vy))
    robots.append(robot)

cycle=[]
for robot in robots:
    (i,j)=robot[0]
    (vx,vy)=robot[1]
    count=0
    depart=(i,j)
    (i,j)=((i+vx)%101,(j+vy)%103)
    count+=1
    while (i,j)!=depart:
        (i,j)=((i+vx)%101,(j+vy)%103)
        count+=1
    cycle.append(count)

pos_finale=[]
for j in range(103):
    line=[]
    for i in range(101):
        line.append(0)
    pos_finale.append(line)
    
for m in range(len(robots)):
    (i,j)=robots[m][0]
    (vx,vy)=robots[m][1]
    for k in range(100%cycle[m]):
        (i,j)=((i+vx)%101,(j+vy)%103)
    pos_finale[j][i]+=1

quadrant_count=[0,0,0,0]
for j in range(103):
    for i in range(101):
        if j<51 and i<50:
            quadrant_count[0]+=pos_finale[j][i]
        elif j<51 and i>50:
            quadrant_count[1]+=pos_finale[j][i]
        elif j>51 and i<50:
            quadrant_count[2]+=pos_finale[j][i]
        elif j>51 and i>50:
            quadrant_count[3]+=pos_finale[j][i]
print(quadrant_count[0]*quadrant_count[1]*quadrant_count[2]*quadrant_count[3])

pos=[]
for j in range(103):
    line=[]
    for i in range(101):
        line.append(0)
    pos.append(line)
    
wheresapin1=open("C:/Users/evanb/AOC-2024/day14/wheresapin1.txt","w")
wheresapin2=open("C:/Users/evanb/AOC-2024/day14/wheresapin2.txt","w")
wheresapin3=open("C:/Users/evanb/AOC-2024/day14/wheresapin3.txt","w")
wheresapin4=open("C:/Users/evanb/AOC-2024/day14/wheresapin4.txt","w")

for k in range(10000):
    for m in range(len(robots)):
        (i,j)=robots[m][0]
        pos[j][i]-=1
        (vx,vy)=robots[m][1]
        (i,j)=((i+vx)%101,(j+vy)%103)
        pos[j][i]+=1
        robots[m][0]=(i,j)
    dastring=""
    for j in range(103):
        for i in range(101):
            if pos[j][i]>0:
                dastring+="#"
            else:
                dastring+="."
        dastring+="\n"
    dastring+="\n"
    if k>6500 and k<7500:
        if k>=7250:
            wheresapin4.write(str(k)+"\n"+dastring)
        elif k>=7000:
            wheresapin3.write(str(k)+"\n"+dastring) 
        elif k>=6750:
            wheresapin2.write(str(k)+"\n"+dastring)
        else:
            wheresapin1.write(str(k)+"\n"+dastring)