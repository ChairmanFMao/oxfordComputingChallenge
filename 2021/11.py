n = int(input())
compare = lambda pair: pair[0] * 1000 + pair[1]
data = [[int(i) for i in input().split()] for j in range(n)]
data.sort(key=compare)
users = 0
time = 0
for i in range(n):
    start, duration = data[i]
    if start >= time:
        time = start + duration
        users += 1

print(users)