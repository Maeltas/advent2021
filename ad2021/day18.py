

def shorten(result):
    squarenum=0
    explode=""
    for i in range(len(result)):
        if result[i]=="[":
            squarenum+=1
        elif result[i]=="]":
            squarenum-=1
        if squarenum>4:
            explode+=result[i]
        if squarenum==4 and explode:
            explode += result[i]
            break
    if explode:
        print(i)
        print(explode)
        a=0
        b=0
        for z in range(len(explode)):
            if explode[z] =="[" and explode[z+2]=="," and explode[z+4]=="]":
                a=int(explode[z+1])
                b=int(explode[z+3])
                break
        print(a)
        print(b)
        for foo in range(i-len(explode)):
            if result
    return result
lines=open("input18", "r")
sfish=[]
for x in lines:
    sfish.append(x.replace("\n",""))
for x in sfish:
    print(x)
result=""
i=0
sfish2=[]
for x in sfish:
    if i==0:
        result=x
    else:
        result="["+result+","+x+"]"
    i+=1
    print(result)
    result=shorten(result)
print(result)