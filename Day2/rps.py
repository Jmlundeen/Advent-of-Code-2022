games = [x.split(' ') for x in open('./Day2/input.txt').read().split('\n')]
rps = {
    1:3,
    2:1,
    3:2
}
scores = [[1 if x == 'A' or x == 'X' else 2 if x == 'B' or x == 'Y' else 3 for x in y] for y in games]
ans = sum([y + 3 if x == y else y if rps[x] == y else y+6 if rps[y] == x else -1 for x,y in scores])
print(ans)