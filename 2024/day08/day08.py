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

def part1(inpt):
	return inpt

def part2(inpt):
	return 0

print(f'Part1 - example: {part1(inpt)}\nPart2 - example: {part2(inpt)}')
inpt = load(example=False)
print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')
