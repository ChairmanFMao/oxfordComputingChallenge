n, m = [int(i) for i in input().split()]
grid = [input() for i in range(m)]
used = [[0 for i in range(n)] for j in range(m)]

# There is a working version in 11pt2.py, it was much more simple than I thought.

clues = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] != "X":
            used[i][j] = 1
            done = 0
            if j < n-1:
                temp = j+1
                if not used[i][temp] and grid[i][temp] != "X":
                    while temp < n and not used[i][temp] and grid[i][temp] != "X":
                        used[i][temp] = 1
                        temp += 1
                    done = 1
            if i < m-1:
                temp = i+1
                if not used[temp][j] and grid[temp][j] != "X":
                    while temp < m and not used[temp][j] and grid[temp][j] != "X":
                        used[temp][j] = 1
                        temp += 1
                    done = 1
            clues += done

print(clues)

"""
10 10
X2911X341X
5X3X178XX1
2X144X1300
120X7XX6X7
X6XX6X8064
1634X1XX1X
2X7XX1X801
2871X802X2
4XX641X0X0
X341X7080X
"""