bags = open('./Day3/input.txt','r').read().split('\n')
bags = [sum([ord(char) - 38 if char.isupper() else ord(char) - 96 for char in sets]) for sets in [set( x[:len(x)//2]).intersection(set(x[len(x)//2:])) for x in bags]]
print(sum(bags))