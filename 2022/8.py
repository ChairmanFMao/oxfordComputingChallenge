m = int(input())
numbers = [int(input()) for i in range(m)]
out = 0
for i in range(len(numbers)-1):
    if numbers[i+1] > numbers[i]:
        out += 100

print(out)