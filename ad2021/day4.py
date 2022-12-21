def checkBingo(bingo,table,x,y,winning_board):
    m=int(len(table)/x/y)
    isBingo=True
    isBingo2 = True
    for f in range(0,m):
        for o in range(0,x):
            isBingo = True
            isBingo2 = True
            for u in range(0,y):
                if table[f*x*y+o+y*u] not in bingo:
                    isBingo=False
                if table[f*x*y+o*x+u] not in bingo:
                    isBingo2=False
            if isBingo==True or isBingo2==True:
                if f not in winning_board:
                    winning_board.append(f)
                    if len(winning_board)==100:
                        sum=0
                        for o in range(0, x):
                            for u in range(0, y):
                                if table[f * x * y + o * x + u] not in bingo:
                                    sum+=int(table[f * x * y + o * x + u])
                        print(int(bingo[len(bingo)-1])*sum)
    return -1


f=open("input4", "r")
table=[]
input=[]
bingo=[]
x=0
y=0
i=0
isSet=False
for a in f:
    if a=="\n" and y>0 and isSet==False:
        isSet=True
    elif i>1 and a!="\n":
        a=a.split()
        x=len(a)
        for b in a:
            table.append(b.replace("\n",""))
        if isSet==False:
            y+=1
    elif i<=1:
        a=a.split(",")
        for b in a:
            input.append(b.replace("\n",""))
    i+=1
i=0
m=-1
sum=0
winning_boards=[]
for a in input:
    bingo.append(a)
    if i<4:
        pass
    else:
        m=checkBingo(bingo,table,x,y,winning_boards)
    if m!=-1:
        if m not in winning_boards:
            winning_boards.append(m)
        print(m)
        break
    i+=1
