f=open("ad2021d2", "r")
hp=0
d=0
a=0
for x in f:
    y=x.split()
    if y[0]== "forward":
        hp+=int(y[1])
        d+=a*int(y[1])
    elif y[0]=="down":
        a+=int(y[1])
    else:
        a-=int(y[1])
print(hp*d)