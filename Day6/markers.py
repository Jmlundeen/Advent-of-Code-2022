# Part 1 swap 14 with 4
print(next(filter(lambda list:len(set(list[1])) == 14,zip(range(len(string := open('./Day6/input.txt','r').readline())),("".join(string[i-14:i]) for i in range(len(string))))))[0])
