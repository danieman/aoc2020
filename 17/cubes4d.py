def get_neighbours(x, y, z, w):
    n = set()
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if (i, j, k, l) != (x, y, z, w):
                        n.add((i, j, k, l))
    return n

def get_candidates(active):
    c = set()
    for x, y, z, w in active:
        c |= get_neighbours(x, y, z, w)
    return c

def count_active_neighbours(pos, active):
    return sum([point in active for point in get_neighbours(*pos)])

init = [line.strip() for line in open("input.txt").readlines()]

active = set()
for y in range(len(init)):
    for x in range(len(init[y])):
        if init[y][x] == "#":
            active.add((x, y, 0, 0))

for _ in range(6):
    new = set()
    for point in get_candidates(active):
        if point in active and count_active_neighbours(point, active) in {2, 3}:
            new.add(point)
        elif point not in active and count_active_neighbours(point, active) == 3:
            new.add(point)
    active = new

print(len(active))