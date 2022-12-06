import re
from functools import reduce
def assignments_test():
    return [[int(x) for x in sub] for sub in [re.findall(r'\d+',x) for x in [x.split('\n') for x in open('./Day5/input.txt').read().split('\n\n')][1]]]
def crates_test():
    return [[re.findall(r'[A-Z]',item)[0] for item in list(i)[::-1] if not item.isspace()] for i in zip(*[re.findall(r"(.{3})\s?", x) for x in [x.split('\n') for x in open('./Day5/input.txt').read().split('\n\n')][0]][:-1])]

def part1():
    print("".join([stack[-1] for stack in [reduce( lambda ans, assignment:[ stack + ans[assignment[1] - 1][-assignment[0]:] if assignment[2]-1 == i else stack[:-assignment[0]] if assignment[1] - 1 == i else stack for i,stack in enumerate(ans)],assignments, crates) for crates,assignments in [([[re.findall(r'[A-Z]',item)[0] for item in list(i)[::-1] if not item.isspace()] for i in zip(*[re.findall(r"(.{3})\s?", x) for x in crateInput[:-1]])],[[int(num) for num in assignment] for assignment in [re.findall(r'\d+',assignmentStrings) for assignmentStrings in assInput]]) for crateInput,assInput in [tuple(line.split('\n') for line in open('./Day5/input.txt').read().split('\n\n'))]]].pop()]))
def part2():
    print("".join([stack[-1] for stack in [reduce( lambda ans, assignment:[ stack + ans[assignment[1] - 1][-assignment[0]:][::-1] if assignment[2]-1 == i else stack[:-assignment[0]] if assignment[1] - 1 == i else stack for i,stack in enumerate(ans)],assignments, crates) for crates,assignments in [([[re.findall(r'[A-Z]',item)[0] for item in list(i)[::-1] if not item.isspace()] for i in zip(*[re.findall(r"(.{3})\s?", x) for x in crateInput[:-1]])],[[int(num) for num in assignment] for assignment in [re.findall(r'\d+',assignmentStrings) for assignmentStrings in assInput]]) for crateInput,assInput in [tuple(line.split('\n') for line in open('./Day5/input.txt').read().split('\n\n'))]]].pop()]))
part2()
part1()