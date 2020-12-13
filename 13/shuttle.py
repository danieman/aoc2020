with open("input.txt") as f:
    t0 = int(f.readline().strip())
    buses = f.readline().strip().split(",")

# Task a)
t = t0
bn = [int(b) for b in buses if b != "x"]
while True:
    found = False
    for b in bn:
        if t % b == 0:
            found = True
            print((t - t0) * b)
            break
    if found:
        break
    t += 1

# Task b)
t = t0
bn = [(i, int(b)) for i, b in enumerate(buses) if b != "x"]
p = 1
for i, b in bn:
    while True:
        if (t + i) % b == 0:
            p *= b
            break
        t += p

print(t)