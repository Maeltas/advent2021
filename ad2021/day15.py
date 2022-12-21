import heapq
lines=open("input15", "r")
dir = [[0,1],[0,-1],[1,0],[-1,0]]
input=[]
for x in lines:
    tab=[]
    for a in range (len(x.replace("\n",""))):
        tab.append(int(x[a]))
    input.append(tab)
input2=[]
for a in range(0,5):
    for x in range(len(input)):
        tab=[]
        for b in range(0,5):
            for y in range(len(input[0])):
                number=input[x][y]+b+a
                if number>9:
                    number=number%9
                tab.append(number)
        input2.append(tab)
input=input2
print(input)
paths = [(0, 0, 0)]
vis = [[0] * len(row) for row in input]

while True:
    rf, x, y = heapq.heappop(paths)
    if vis[x][y]: continue
    if (x, y) == (len(input) - 1, len(input[x]) - 1):
        print(rf)
        exit(0)
    vis[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(input) > nx >= 0 <= ny < len(input[0]): continue
        if vis[nx][ny]: continue
        heapq.heappush(paths, (rf + input[nx][ny], nx, ny))