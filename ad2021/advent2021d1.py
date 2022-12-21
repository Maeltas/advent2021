f=open("advent2021d1i.txt", "r")
prev1=-1
prev2=-1
sum1=0
sum2=0
result=0
i=0
for x in f:
    if i>=2:
        if i%2==0:
            sum1=int(x)+prev1+prev2
        else:
            sum2=int(x)+prev1+prev2
    if i>=3:
        if sum1>sum2 and i%2==0:
            result+=1
        elif sum2>sum1 and i%2==1:
            result+=1
    if prev1==-1 and prev2==-1:
       prev1=int(x)
    elif prev2==-1:
       prev2=prev1
       prev1=int(x)
    else:
       prev2 = prev1
       prev1 = int(x)
    i+=1

print(result)

