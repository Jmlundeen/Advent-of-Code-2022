def solution():
    return list(map(lambda n: sum(sorted([sum([int(x) for x in calories]) for calories in[elf.split() for elf in open('./Day1/input.txt','r').read().split('\n\n')]])[-n:]),(1,3)))
print(solution())