def znajdz_drogi(val,connections,droga,drogi2,Twice):
    droga+=","+val
    print(droga)
    if val=="end":
        if droga not in drogi2:
            drogi2.append(droga)
        return
    for x in connections:
        if x[0]==val:
            if x[1].upper()==x[1]:
                znajdz_drogi(x[1], connections, droga, drogi2,Twice)
            elif x[1] not in droga:
                znajdz_drogi(x[1], connections, droga, drogi2,Twice)
            elif Twice==False and x[1] not in ["start","end"]:
                znajdz_drogi(x[1], connections, droga, drogi2,True)
        elif x[1]==val:
            if x[0].upper() == x[0]:
                znajdz_drogi(x[0],connections,droga,drogi2,Twice)
            elif x[0] not in droga:
                znajdz_drogi(x[0], connections, droga, drogi2, Twice)
            elif Twice == False and x[0] not in ["start","end"]:
                znajdz_drogi(x[0], connections, droga, drogi2, True)


lines=open("input12", "r")
connections=[]
for x in lines:
    a=x.split("-")
    connections.append([a[0],a[1].replace("\n","")])
print(connections)
drogi=[]
for x in connections:
    if x[0]=="start":
        droga="start"
        Twice=False
        znajdz_drogi(x[1],connections,droga,drogi,Twice)
    elif x[1]=="start":
        droga = "start"
        Twice = False
        znajdz_drogi(x[0], connections, droga, drogi, Twice)
print(drogi)
print(len(drogi))