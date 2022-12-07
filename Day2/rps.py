def originalPart1():
    games = [x.split(' ') for x in open('./Day2/input.txt').read().split('\n')]
    # x beats y
    rps = {
        1:3,
        2:1,
        3:2
    }
    # 1 == lose (0), 2 == draw (3), 3 == win (6)
    scores = [[1 if x == 'A' or x == 'X' else 2 if x == 'B' or x == 'Y' else 3 for x in y] for y in games]
    ans = sum([y + 3 if x == y else y if rps[x] == y else y+6 if rps[y] == x else -1 for x,y in scores])
    print(ans)

def originalPart2():
    games = [x.split(' ') for x in open('./Day2/input.txt').read().split('\n')]
    rps = {
        # x beats y
        1:3,
        2:1,
        3:2
    }
    # 1 == lose (0), 2 == draw (3), 3 == win (6)
    scores = [[1 if x == 'A' or x == 'X' else 2 if x == 'B' or x == 'Y' else 3 for x in y] for y in games]
    ans = [rps[x] if y == 1 else x + 3 if y == 2 else list(rps.keys())[list(rps.values()).index(x)] + 6 if y == 3 else -1 for x,y in scores]
    print(sum(ans))

def part1():
    print(sum([3+self if opp == self else self if (opp - self) % 3 == 1 else self + 6 for opp,self in map(lambda game: (ord(game.split()[0]) - 64,ord(game.split()[1]) - 87),open('./Day2/input.txt').read().splitlines())]))

def part2():
    print(sum([(self + opp - 1)% 3 + 1 + self*3 for opp,self in map(lambda game: (ord(game.split()[0]) - 65,ord(game.split()[1]) - 88),open('./Day2/input.txt').read().splitlines())]))

part1()
part2()
