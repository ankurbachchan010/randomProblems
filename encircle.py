def doesCircleExist(commands):
    com = commands * 4
    print(com)
    N = 0
    E = 1
    S = 2
    W = 3

    x = 0
    y = 0
    dir = N
    result = []
    # Traverse the path given for robot
    for i in range(len(commands)):
        move = commands[i]
        print(move)
        for j in move:
            if move == 'R':
                dir = (dir + 1) % 4
            elif move == 'L':
                dir = (4 + dir - 1) % 4
            else:
                if dir == N:
                    y += 1
                elif dir == E:
                    x += 1
                elif dir == S:
                    y -= 1
                else:
                    x -= 1

    if x == 0 and y == 0:
        result.append("YES")
    else:
        result.append("NO")
    print(result)

doesCircleExist('GGGR')
