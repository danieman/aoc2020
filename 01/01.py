with open("input.txt", "r") as f:
    numbers = [int(n.strip()) for n in f.readlines()]

# Part a)
found = False
for i, n in enumerate(numbers):
    for j in numbers[i:]:
        if n + j == 2020:
            print(n * j)
            found = True
            break
    if found:
        break

# Part b)
found = False
for i, x in enumerate(numbers):
    for j, y in enumerate(numbers[i:]):
        for z in numbers[i+j:]:
            if x + y + z == 2020:
                print(x * y * z)
                found = True
                break
        if found:
            break
    if found:
        break