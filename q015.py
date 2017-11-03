
LIMIT = 2

def move(pos, counter):
    if pos == [LIMIT, LIMIT]:
        counter += 1
        return
    elif pos[0] > LIMIT or pos[1] > LIMIT:
        return
    else:
        move([pos[0], pos[1]+1], counter)
        move([pos[0]+1, pos[1]], counter)

counter=0
move([0,0], counter)
print(counter)