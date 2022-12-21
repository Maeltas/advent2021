f=open("day3", "r")
gamma=""
epsilon=""
input=[]
for x in f:
    input.append(x)
def count1(i,input):
    num1=0
    num0=0
    for y in input:
        if int(y[i])==0:
            num0+=1
        else:
            num1+=1
    if num0> num1:
        return 0
    return 1
def oxygen(i,input):
    num1 = 0
    num0 = 0
    for y in input:
        if int(y[i]) == 0:
            num0 += 1
        else:
            num1 += 1
    delete=[]
    if num0 > num1:
        for y in input:
            if int(y[i]) == 1:
                delete.append(y)
        for nm in delete:
            input.remove(nm)
    else:
        for y in input:
            if int(y[i]) == 0:
                delete.append(y)
        for nm in delete:
            input.remove(nm)
    if len(input)==1:
        return input[0]
    else:
        return oxygen(i+1,input)
def co2sr(i,input):
    num1 = 0
    num0 = 0
    for y in input:
        if int(y[i]) == 0:
            num0 += 1
        else:
            num1 += 1
    delete=[]
    if num0 <= num1:
        for y in input:
            if int(y[i]) == 1:
                delete.append(y)
        for nm in delete:
            input.remove(nm)
    else:
        for y in input:
            if int(y[i]) == 0:
                delete.append(y)
        for nm in delete:
            input.remove(nm)
    if len(input) == 1:
        return input[0]
    else:
        return co2sr(i + 1, input)
for i in range(len(input[0])-1):
    gamma+=str(count1(i,input))
    if gamma[len(gamma)-1]=="0":
        epsilon+="1"
    else:
        epsilon+="0"
multiplier=1
gamma2=0
epsilon2=0
i=len(gamma)-1
while i>=0:
    gamma2+=int(gamma[i])*multiplier
    epsilon2 += int(epsilon[i]) * multiplier
    i-=1
    multiplier*=2
print(gamma2*epsilon2)
ogr=""
co2=""
input2=[]
for i in input:
    input2.append(i)
ogr=oxygen(0,input)
co2=co2sr(0,input2)
multiplier=1
ogr2=0
co22=0
i=len(ogr)-2
while i>=0:
    ogr2+=int(ogr[i])*multiplier
    co22 += int(co2[i]) * multiplier
    i-=1
    multiplier*=2
print(ogr2*co22)
