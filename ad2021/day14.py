lines=open("input14", "r")
input=""
pairs={}
instructions=[]
for x in lines:
    if x=="\n":
        pass
    elif "->" in x:
        instructions.append(x.replace("\n",""))
    else:
        input=x.replace("\n","")
for i in range(2,len(input)+1):
    m = input[i - 2:i]
    if m in pairs.keys():
        val=pairs[m]
        pairs[m]=val+1
    else:
        pairs[m]=1
print(pairs)
for _ in range(40):
    pairs2={}
    for key,val in pairs.items():
        zmieniono=False
        for instr in instructions:
            if key in instr:
                zmieniono=True
                a,b=instr.split(" -> ")
                if key[0]+b in pairs2:
                    number=pairs2[key[0]+b]
                    pairs2[key[0] + b]=number+val
                else:
                    pairs2[key[0]+b]=val
                if b+key[1]in pairs2:
                    number=pairs2[b+key[1]]
                    pairs2[b+key[1]]=number+val
                else:
                    pairs2[b+key[1]]=val
        if key not in pairs2.keys() and zmieniono==False:
            pairs2[key]=val
    pairs={}
    for key,val in pairs2.items():
        pairs[key]=val
wystapienia={}
wystapienia[input[len(input)-1]]=1
ile_b=0
ile_h=0
for key,val in pairs.items():
    if key[0] in wystapienia:
        number=wystapienia[key[0]]
        wystapienia[key[0]] = number+val
    else:
        wystapienia[key[0]] = val
min=0
max=0
for key,val in wystapienia.items():
    if min==0:
        min=val
    if min>val:
        min=val
    if max<val:
        max=val
print(max-min)