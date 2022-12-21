def fold_y(b,max_x,max_y,table):
    for y in range(b+1,max_y):
        for x in range(max_x):
            if table[y][x]=="#":
                roznica=y-b
                if b-roznica>=0:
                    table[b-roznica][x]="#"
def fold_x(b,max_x,max_y,table):
    for y in range(max_y):
        for x in range(b+1,max_x):
            if table[y][x]=="#":
                roznica=x-b
                if b-roznica>=0:
                    table[y][b-roznica]="#"
lines=open("input13", "r")
cords=[]
instructions=[]
for x in lines:
    if x=="\n":
        pass
    elif "="in x:
        instructions.append(x)
    else:
        a,b=x.split(",")
        cords.append([int(a),int(b.replace("\n",""))])
max_x=0
max_y=0
for x in cords:
    if x[0]>max_x:
        max_x=x[0]
    if x[1]>max_y:
        max_y=x[1]
max_x+=1
max_y+=1
table=[]
for _ in range(max_y):
    tab=[]
    for y in range(max_x):
        tab.append(".")
    table.append(tab)
for x in cords:
    table[x[1]][x[0]]="#"
for instr in instructions:
    if "y"in instr:
        a,b=instr.split("=")
        fold_y(int(b),max_x,max_y,table)
        max_y=int(b)
    elif "x" in instr:
        a, b = instr.split("=")
        fold_x(int(b), max_x, max_y, table)
        max_x = int(b)
sum=0
for x in range(max_y):
    print("".join(table[x][0:max_x-1]))
