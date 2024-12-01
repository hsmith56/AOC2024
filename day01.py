import random, math

def load(example=False):
    if example is True:
        with open('day01Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day01Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(example=True)

def part1(data, *args, **kwargs):
    data = [(int(y),int(z)) for y,z in (" ".join(x.split()).split(" ") for x in data)]
    l = sorted([x[0] for x in data])
    r = sorted([x[1] for x in data])

    total = 0

    for i in range(len(data)):
        total += abs(l[i]-r[i])
        
    return total


def part2(data, *args, **kwargs):
    data = [(int(y),int(z)) for y,z in (" ".join(x.split()).split(" ") for x in data)]
    l = sorted([x[0] for x in data])
    r = sorted([x[1] for x in data])

    total = 0

    for i in range(len(data)):
        total += l[i] * r.count(l[i])
        
    return total

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')