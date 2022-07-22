n = int(input())
numbers = {}
for i in range(10):
    numbers[i] = 0

for i in range(n):
    for j in input():
        numbers[int(j)] += 1

popular = 0; score = 0
for i in range(10):
    if numbers[i] > score:
        popular = i
        score = numbers[i]

print(popular)