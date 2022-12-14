inputs = [[l,int(r)]for l,r in [x.split() for x in open('./Day9/input.txt').readlines()]]
def moveTail(rope,index):
    if index == -1:
        return rope
    head = rope[index + 1]
    tail = rope[index]
    xDiff = head[0] - tail[0]
    yDiff = head[1] - tail[1]

    if abs(xDiff) > 1:
        if xDiff < 0:
            tail[0] -= 1
        else:
            tail[0] += 1
        if yDiff < 0:
            tail[1] -= 1
        elif yDiff > 0:
            tail[1] += 1
        return moveTail(rope, index - 1)
    elif abs(yDiff) > 1:
        if yDiff < 0:
            tail[1] -= 1
        else:
            tail[1] += 1
        if xDiff < 0:
            tail[0] -= 1
        elif xDiff > 0:
            tail[0] += 1
        return moveTail(rope, index - 1)
    return rope

def solution(size):
    rope = [[0,0] for _ in range(size)]
    unique = set([tuple(rope[0])])

    for move in inputs:
            match move[0]:
                case 'R':
                    for _ in range(move[1]):
                        rope[size - 1][0] += 1
                        rope = moveTail(rope,size - 2)
                        unique.add(tuple(rope[0]))
                case 'U':
                    for _ in range(move[1]):
                        rope[size - 1][1] += 1
                        rope = moveTail(rope,size - 2)
                        unique.add(tuple(rope[0]))
                case 'L':
                    for _ in range(move[1]):
                        rope[size - 1][0] -= 1
                        rope = moveTail(rope,size - 2)
                        unique.add(tuple(rope[0]))
                case 'D':
                    for _ in range(move[1]):
                        rope[size - 1][1] -= 1
                        rope = moveTail(rope,size - 2)
                        unique.add(tuple(rope[0]))
    return len(unique)

print(f'Part 1: {solution(2)}')
print(f'Part 2: {solution(10)}')