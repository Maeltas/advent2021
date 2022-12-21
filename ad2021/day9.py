def basin(input,a,b,basin_set):
    size=1
    if (a - 1) >= 0 and input[a - 1][b] > input[a][b] and int(input[a - 1][b])!=9 and str(a-1)+":"+str(b) not in basin_set:
        basin_set.append(str(a-1)+":"+str(b))
        size+=basin(input,a-1,b,basin_set)
    if (a + 1) < len(input) and input[a + 1][b] > input[a][b] and int(input[a + 1][b])!=9 and str(a+1)+":"+str(b) not in basin_set:
        basin_set.append(str(a + 1) + ":" + str(b))
        size+=basin(input,a+1,b,basin_set)
    if (b + 1) < len(input[0]) and input[a][b + 1] > input[a][b] and int(input[a][b+1])!=9 and str(a)+":"+str(b+1) not in basin_set:
        basin_set.append(str(a) + ":" + str(b+1))
        size+=basin(input,a,b+1,basin_set)
    if (b - 1) >= 0 and input[a][b - 1] > input[a][b] and int(input[a][b-1])!=9 and str(a)+":"+str(b-1) not in basin_set:
        basin_set.append(str(a) + ":" + str(b - 1))
        size+=basin(input,a,b-1,basin_set)
    return size

lines=open("input9", "r")
low_numbers=[]
basins=[]
input=[]
for x in lines:
    for a in x.split():
        input.append(a)
is_lower=True
for a in range(0,len(input)):
    for b in range(0,len(input[0])):
        is_lower=True
        if (a-1) >=0 and input[a-1][b]<=input[a][b]:
            is_lower=False
        if (a+1) <len(input) and input[a+1][b]<=input[a][b]:
            is_lower=False
        if (b+1) <len(input[0]) and input[a][b+1]<=input[a][b]:
            is_lower=False
        if (b-1) >=0 and input[a][b-1]<=input[a][b]:
            is_lower=False
        if is_lower==True:
            low_numbers.append(input[a][b])
            basin_set=[str(a)+":"+str(b)]
            basins.append(basin(input,a,b,basin_set))
sum=0
for a in low_numbers:
    sum+=1+int(a)
print(sum)
basins = sorted(basins, reverse=True)
print(basins)