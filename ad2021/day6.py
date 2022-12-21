f=open("input6", "r")
table=[0,0,0,0,0,0,0,0,0]
for x in f:
    x = x.split(",")
    for a in x:
        a=a.replace("\n","")
        table[int(a)%8]+=1
for _ in range(0,256):
    ile_zer=0
    for i,e in enumerate(table):
        if i==0:
            ile_zer=e
            table[i]=table[i+1]
        elif i==8:
            table[i]=ile_zer
        elif i==6:
            table[i] = table[i + 1]+ile_zer
        else:
            table[i] = table[i + 1]
sum=0
for i in table:
    sum+=i
print(sum)