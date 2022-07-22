numbers = [int(i) for i in input().split()]
changes = 1
seat = numbers[0]
for i in range(1,len(numbers)):
    if numbers[i] < seat:
        seat = numbers[i]
        changes += 1

print(changes)