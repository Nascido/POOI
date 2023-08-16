read = input()

x1, y1, x2, y2 = read.split(" ")
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

movements = []

while x1 != 0:
    
    difx = abs(x1 - x2)
    dify = abs(y1 - y2)

    if difx == dify:
        if difx == 0:
            movements.append(0)
        else:
            movements.append(1)
    elif difx == 0 or dify == 0:
        movements.append(1)
    else:
        movements.append(2)

    read = input()

    x1, y1, x2, y2 = read.split(" ")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)


for move in movements:
    print(move)
