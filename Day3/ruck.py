def part1():
    print(sum([sum([ord(char) - 38 if char.isupper() else ord(char) - 96 for char in sets]) for sets in [set( x[:len(x)//2]).intersection(set(x[len(x)//2:])) for x in open('./Day3/input.txt','r').read().split('\n')]]))

def part2():
    print(sum([sum([ord(char) - 38 if char.isupper() else ord(char) - 96 for char in set]) for set in[(set(sub[0]).intersection(set(sub[1]).intersection(set(sub[2])))) for sub in list(zip(*[iter(open('./Day3/input.txt','r').read().split('\n'))]*3))]]))
    
part1()
part2()

