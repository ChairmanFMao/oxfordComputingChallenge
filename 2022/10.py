n = int(input())
gems = [[int(i) for i in input().split()] for j in range(n)]

s = 0
for i in range(n):
    if i & 1:
        best = 0; index = 0
        for j in range(len(gems)):
            if gems[j][1] > best:
                best = gems[j][1]
                index = j
        s += best
        gems.pop(index)
    else:
        best = 0; index = 0
        for j in range(len(gems)):
            if gems[j][0] > best:
                best = gems[j][0]
                index = j
        gems.pop(index)

print(s)