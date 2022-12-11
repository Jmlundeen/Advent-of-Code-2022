# Tree is visible if its height is greater than any edge in the row or the column
from functools import reduce


rows = [[int(x) for x in line.strip('\n')] for line in open("./Day8/input.txt").readlines()]
cols = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows))]
gridSize = len(rows)
def part1():
    dp = []
    visible = 0
    for row in range(0,gridSize):
        if row == 0 or row == gridSize - 1:
            visible += gridSize
            continue
        lst = []
        for col in range(0,gridSize):
            if col == 0 or col == gridSize - 1:
                visible += 1
                continue
            num = rows[row][col]
            left = max(rows[row][:col])
            right = max(rows[row][col+1:])
            top = max(cols[col][:row])
            bottom = max(cols[col][row+1:])
            if num > left or num > right or num > top or num > bottom:
                visible +=1
                lst.append('visible')
            else:
                lst.append('invisible')
        dp.append(lst)
    print(f'Part 1: {visible}')

def part2():
    treeScores = []
    for row in range(0,gridSize):
        if row == 0 or row == gridSize - 1:
            continue
        for col in range(0,gridSize):
            if col == 0 or col == gridSize - 1:
                continue
            num = rows[row][col]
            left = rows[row][:col][::-1]
            right = rows[row][col+1:]
            top = cols[col][:row][::-1]
            bottom = cols[col][row+1:]
            sceneScore = 1
            for list in [(left),right,top,bottom]:
                for i,int in enumerate(list):
                    if int >= num or i == len(list) - 1:
                        sceneScore *= (i+1)
                        break
            treeScores.append(sceneScore)
    print(f'Part 2: {max(treeScores)}')
part1()
part2()