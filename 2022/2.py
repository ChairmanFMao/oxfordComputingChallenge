n = int(input())
digits = [i for i in input().split()]
m = int(input())
codes = []
for i in range(m):
    codes.append(input())

errors = 0
for i in codes:
    if i[0] in digits:
        errors += 1

print(errors)