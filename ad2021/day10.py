lines=open("input10", "r")
brackets={
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
}
s={
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}
s2={
    "(":1,
    "[":2,
    "{":3,
    "<":4,
}
sum=0
score=[]
for x in lines:
    table=[]
    no_error=True
    for a in range(len(x)-1):
        if x[a] in brackets.keys():
            table.append(x[a])
        elif x[a]==brackets[table[-1]]:
            table.pop()
        else:
            sum+=s[x[a]]
            no_error=False
            break
    if no_error==True:
        score2=0
        while table!=[]:
            score2 *= 5
            score2+=s2[table[-1]]
            table.pop()
        score.append(score2)
print(sum)
score=sorted(score)
print(score[int(len(score)/2)])