n, m = [int(i) for i in input().split()]
grid = [input() for i in range(m)]

clues = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] != "X":
            good = 0
            if j < n-1:
                if grid[i][j+1] != "X" and (j == 0 or grid[i][j-1] == "X"):
                    good = 1
            if i < m-1:
                if grid[i+1][j] != "X" and (i == 0 or grid[i-1][j] == "X"):
                    good = 1
            clues += good

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