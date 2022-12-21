f=open("input5", "r")
value={}
for x in f:
    x1, x2, y1, y2=0, 0, 0, 0
    x=x.split(" -> ")
    i=0
    for z in x:
        z=z.split(",")
        if i==0:
            x1=int(z[0])
            y1=int(z[1])
        else:
            x2 = int(z[0])
            y2 = int(z[1].replace("\n",""))
        i+=1
    if x1==x2:
        for a in range(min(y1,y2),max(y1,y2)+1):
            if str(x1) + ":" + str(a) in value.keys():
                b = value[str(x1) + ":" + str(a)]
                b += 1
                value[str(x1) + ":" + str(a)] = b
            else:
                value[str(x1) + ":" + str(a)] = 1
    elif y1==y2:
        for a in range(min(x1,x2), max(x1,x2)+1):
            if str(a) + ":" + str(y1) in value.keys():
                b = value[str(a) + ":" + str(y1)]
                b += 1
                value[str(a) + ":" + str(y1)] = b
            else:
                value[str(a) + ":" + str(y1)] = 1
    elif abs(x1-x2) == abs(y1-y2):
        b=0
        b_change=0
        if min(x1, x2) == x1:
            b = y1
        else:
            b=y2
        if(y2>y1) and b==y1:
            b_change=1
        elif y1>y2 and b==y1:
            b_change=-1
        elif y2>y1 and b==y2:
            b_change=-1
        elif y2<y1 and b==y2:
            b_change=1
        for a in range(min(x1,x2),max(x1,x2)+1):
                if str(a) + ":" + str(b) in value.keys():
                    c = value[str(a) + ":" + str(b)]
                    c += 1
                    value[str(a) + ":" + str(b)] = c
                else:
                    value[str(a) + ":" + str(b)] = 1
                b+=b_change
sum=0
for key,v in value.items():
    if v>1:
        sum+=1
print(sum)