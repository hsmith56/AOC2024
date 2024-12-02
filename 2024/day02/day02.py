import random, math

def load(example=False):
    if example is True:
        with open('day02Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day02Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

def is_valid_sequence(numbers):
    increasing = all(numbers[i] < numbers[i+1] and numbers[i+1] - numbers[i] <= 3 for i in range(len(numbers)-1))
    decreasing = all(numbers[i] > numbers[i+1] and numbers[i] - numbers[i+1] <= 3 for i in range(len(numbers)-1))
    return increasing or decreasing

def part1(inpt):
    safe_count = 0
    for row in inpt:
        numbers = list(map(int, row.split()))
        if is_valid_sequence(numbers):
            safe_count += 1

    return safe_count

def part2(inpt):
    safe_count = 0
    for row in inpt:
        numbers = list(map(int, row.split()))
        
        if is_valid_sequence(numbers):
            safe_count += 1
            continue
        
        for i in range(len(numbers)):
            temp_sequence = numbers[:i] + numbers[i+1:]
            if is_valid_sequence(temp_sequence):
                safe_count += 1
                break
    
    return safe_count

inpt = load(example=False)
print(f'Part1 - example: {part1(inpt)}\nPart2 - example: {part2(inpt)}')
