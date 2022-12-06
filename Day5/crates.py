import re
assignments = [[int(x) for x in sub] for sub in [re.findall(r'\d+',x) for x in [x.split('\n') for x in open('./Day5/input.txt').read().split('\n\n')][1]]]


def part1():
    crates = [[re.findall(r'[A-Z]',item)[0] for item in list(i)[::-1] if not item.isspace()] for i in zip(*[re.findall(r"(.{3})\s?", x) for x in [x.split('\n') for x in open('./Day5/input.txt').read().split('\n\n')][0]][:-1])]
    for num, col1, col2 in assignments:
        for x in range(num):
            crates[col2 - 1].append(crates[col1 - 1].pop())
    return("".join([lst.pop() for lst in crates]))


def part2():
    crates = [[re.findall(r'[A-Z]',item)[0] for item in list(i)[::-1] if not item.isspace()] for i in zip(*[re.findall(r"(.{3})\s?", x) for x in [x.split('\n') for x in open('./Day5/input.txt').read().split('\n\n')][0]][:-1])]
    for num, col1, col2 in assignments:
        if num > 1:
            crates[col2 - 1] = crates[col2 - 1] + crates[col1 - 1][-num:]
            del crates[col1 - 1][-num:]
        else:
            crates[col2 - 1].append(crates[col1 - 1].pop())
    return("".join([lst.pop() for lst in crates]))


print(f'Part 1 - {part1()}')
print(f'Part 2 - {part2()}')