import random
lines=open("input24", "r")
instr=[]
result=[0,0,0,0]
decipher={
    "w":0,
    "x":1,
    "y":2,
    "z":3
}
monad=[]
for x in lines:
    instr.append(x.replace("\n",""))
print(instr)
valid=False
for ins in instr:
    inst= ins.split()
    if "inp" in ins:
        result[decipher[inst[1]]]=1
        monad.append(result[decipher[inst[1]]])
    elif "add" in ins:
        if inst[2] in ["w", "x", "y", "z"]:
            result[decipher[inst[1]]] += result[decipher[inst[2]]]
        else:
            result[decipher[inst[1]]] += int(inst[2])
    elif "mul" in ins:
        if inst[2] in ["w", "x", "y", "z"]:
            result[decipher[inst[1]]] *= result[decipher[inst[2]]]
        else:
            result[decipher[inst[1]]] *= int(inst[2])
    elif "div" in ins:
        if inst[2] in ["w", "x", "y", "z"]:
            if result[decipher[inst[2]]] == 0:
                break
            result[decipher[inst[1]]] /= result[decipher[inst[2]]]
        else:
            if int(inst[2]) == 0:
                break
            result[decipher[inst[1]]] /= int(inst[2])
    elif "mod" in ins:
        if inst[2] in ["w","x","y","z"]:
            if result[decipher[inst[2]]] <= 0 or result[decipher[inst[1]]]<0:
                break
            result[decipher[inst[1]]] = result[decipher[inst[1]]] % result[decipher[inst[2]]]
        else:
            if int(inst[2]) <= 0 or int(inst[2]) < 0:
                break
            result[decipher[inst[1]]] = result[decipher[inst[1]]] % int(inst[2])
    else:
        if inst[2] in ["w","x","y","z"]:
            if result[decipher[inst[1]]] == int(instr[2]):
                result[decipher[inst[1]]] = 1
            else:
                result[decipher[inst[1]]] = 0
        else:
            if result[decipher[inst[1]]] == result[decipher[inst[2]]]:
                result[decipher[inst[1]]] = 1
            else:
                result[decipher[inst[1]]] = 0
if result[3]==0:
    print(result)
    print(monad)