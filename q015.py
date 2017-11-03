"""Problem 15 - Lattice paths."""
LIMIT = 3
counter = 0

def move(pos):
    global counter # LUL
    if pos == [LIMIT, LIMIT]:
        counter += 1
        return
    elif pos[0] > LIMIT or pos[1] > LIMIT:
        return
    else:
        move([pos[0], pos[1]+1])
        move([pos[0]+1, pos[1]])

move([0, 0])
print(counter)
