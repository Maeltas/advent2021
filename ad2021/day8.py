def stringin(str1,str2):
    for i in str1:
        if i not in str2:
            return False
    return True


f=open("input8", "r")
sum=0
for x in f:
    a,b=x.split("|")
    zero=""
    one=""
    one2=""
    two=""
    three=""
    four=""
    five=""
    six=""
    seven=""
    eight="abcdefg"
    nine=""
    unmatched=[]
    for j in sorted(a.split(),key=len):
        if len(j) == 2:
            one="".join(sorted(j))
            one2=j
        elif len(j) == 3:
            seven="".join(sorted(j))
        elif len(j) == 4:
            four="".join(sorted(j))
        elif len(j) == 5:
            if stringin(one,j):
                three="".join(sorted(j))
            else:
                unmatched.append("".join(sorted(j)))
        elif len(j)==6:
            if not stringin(four,j) and not stringin(seven,j):
                six="".join(sorted(j))
            elif stringin(four,j):
                nine="".join(sorted(j))
            else:
                zero="".join(sorted(j))
    for i in unmatched:
        helper=nine
        helper=helper.replace(one[0],"")
        helper=helper.replace(one[1], "")
        if stringin(helper,i):
            five=i
        else:
            two=i
    sum2=0
    for j in b.split():
        j="".join(sorted(j))
        if j==zero:
            if sum2>0:
                sum2*=10
        elif j==one:
            if sum2>0:
                sum2*=10
            sum2+=1
        elif j==two:
            if sum2>0:
                sum2*=10
            sum2+=2
        elif j==three:
            if sum2>0:
                sum2*=10
            sum2+=3
        elif j==four:
            if sum2>0:
                sum2*=10
            sum2+=4
        elif j==five:
            if sum2>0:
                sum2*=10
            sum2+=5
        elif j==six:
            if sum2>0:
                sum2*=10
            sum2+=6
        elif j==seven:
            if sum2>0:
                sum2*=10
            sum2+=7
        elif j==eight:
            if sum2>0:
                sum2*=10
            sum2+=8
        elif j==nine:
            if sum2>0:
                sum2*=10
            sum2+=9
    print(sum2)
    sum+=sum2
print(sum)