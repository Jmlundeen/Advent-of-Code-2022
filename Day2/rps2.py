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