file=open("C:/Users/evanb/AOC-2024/day13/input.txt").read().split("\n\n")
count=0
for machine in file:
    trucx=machine.split("X")
    x_a=int(trucx[1].split(",")[0][1:])
    x_b=int(trucx[2].split(",")[0][1:])
    x_p=int(trucx[3].split(",")[0][1:])
    trucy=machine.split("Y")
    y_a=int(trucy[1].split("\n")[0][1:])
    y_b=int(trucy[2].split("\n")[0][1:])
    y_p=int(trucy[3].split("\n")[0][1:])
    A=(x_p*y_b-y_p*x_b)/(x_a*y_b-y_a*x_b)
    B=(y_p-A*y_a)/y_b
    print(machine+"\n {}*{}+{}*{}={}\n{}*{}+{}*{}={}\n".format(A,x_a,B,x_b,x_p,A,y_a,B,y_b,y_p))
    if A>=0 and B>=0 and abs(A-round(A))<0.001 and abs(B-round(B))<0.001:
        count+=3*round(A)+round(B)
print(count)

count=0
for machine in file:
    trucx=machine.split("X")
    x_a=int(trucx[1].split(",")[0][1:])
    x_b=int(trucx[2].split(",")[0][1:])
    x_p=int(trucx[3].split(",")[0][1:])+10000000000000
    trucy=machine.split("Y")
    y_a=int(trucy[1].split("\n")[0][1:])
    y_b=int(trucy[2].split("\n")[0][1:])
    y_p=int(trucy[3].split("\n")[0][1:])+10000000000000
    A=(x_p*y_b-y_p*x_b)/(x_a*y_b-y_a*x_b)
    B=(y_p-A*y_a)/y_b
    print(machine+"\n {}*{}+{}*{}={}\n{}*{}+{}*{}={}\n".format(A,x_a,B,x_b,x_p,A,y_a,B,y_b,y_p))
    if A>=0 and B>=0 and abs(A-round(A))<0.001 and abs(B-round(B))<0.001:
        count+=3*round(A)+round(B)
print(count)