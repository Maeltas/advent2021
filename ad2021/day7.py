f=open("input7", "r")
crabs=[]
position=-1
lowest=-1
for x in f:
    x = x.split(",")
    for a in x:
        a = a.replace("\n", "")
        crabs.append(int(a))
for i in range(min(crabs),max(crabs)):
    position=i
    sum=0
    for c in crabs:
        n=abs(c-i)
        a1=1
        an=1+(1*(n-1))
        sum+=int((a1+an)*n/2)
    if sum<lowest or lowest==-1:
        lowest=sum
print(lowest)
