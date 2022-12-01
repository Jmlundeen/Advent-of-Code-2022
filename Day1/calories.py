elves = open('./Day1/input.txt','r').read().split('\n\n')
top3 = sorted([sum([int(x) for x in elf.split('\n') if x != '']) for elf in elves])[-3:]
print(sum(top3))