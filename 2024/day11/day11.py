import random, math

def load():
	with open('day11/day11Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()
def part1(inpt):
	return inpt

def part2(inpt):
	return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')