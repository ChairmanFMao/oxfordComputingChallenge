scores = [[i for i in input().split()] for j in range(4)]
a = 0; b = 0
for i in scores:
    if i[0] == "A":
        a += int(i[1]) - (int(i[2]) * 3)
    else:
        b += int(i[1]) - (int(i[2]) * 3)

print("A" if a < b else ("B" if b < a else "draw"))