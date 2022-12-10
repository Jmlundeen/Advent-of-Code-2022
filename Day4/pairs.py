def part1():
    print(sum([1 if (int(b) >= int(d) and int(a) <= int(c)) or (int(d) >= int(b) and int(c) <= int(a)) else 0 for a,b,c,d in [nums.split('-') for nums in ['-'.join(sublist) for sublist in [line.split(',') for line in open('./Day4/input.txt').read().split('\n')]]]]))
def part2():
    print(sum([1 if (int(d) >= int(a) and int(b) >= int(c)) else 0 for a,b,c,d in [nums.split('-') for nums in ['-'.join(sublist) for sublist in [line.split(',') for line in open('./Day4/input.txt').read().split('\n')]]]]))
