bags = open('./Day3/input.txt','r').read().split('\n')
# bags = [sum([ord(char) - 38 if char.isupper() else ord(char) - 96 for char in sets]) for sets in [set(triple[0]).intersection(set(triple[1]).intersection(set(triple[2]))) for triple in [bags[i:i+3] for i in range(0,len(bags),3)]]]
# print(sum(bags))

for i,x in enumerate(bags):
    print(i,x)