import random, math
import re

def load(example=False):
    if example is True:
        with open('day03Example.txt') as file:
            data = file.readlines()
            d = [line.strip() for line in data]
        return d
        
    with open('day03Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load(example=False)

def part1(inpt):
    pattern = r"mul\(\d*,\d*\)"

    running_total = 0

    for line in inpt:
        matches = re.findall(pattern, line)
        for match in matches:
            match = match.replace("mul(","").replace(")","").split(",")

            match = [int(x) for x in match]
            running_total += match[0] * match[1]

    return running_total

def part2(inpt):
    pattern = r"mul\(\d*,\d*\)"

    running_total = 0

    inpt = "".join(inpt)
    matches = re.finditer(pattern, inpt)
    for match in matches:

        search_upto_index = match.span()[0]

        do_instruction   =  max(inpt[0:search_upto_index+1].rfind('do()'), 0)
        dont_instruction =  inpt[0:search_upto_index+1].rfind("don't()")
        if do_instruction > dont_instruction:
            print("DO STUFF")
        else:
            continue

        match = match.group(0)

        match = match.replace("mul(","").replace(")","").split(",")
        match = [int(x) for x in match]
        running_total += match[0] * match[1]

    return running_total

print(f'Part1 - example: {part1(inpt)}\nPart2 - example: {part2(inpt)}')
