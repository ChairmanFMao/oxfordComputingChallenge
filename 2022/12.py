s = input()
best = []
times = 0
occurs = {}
for i in range(26):
    occurs[chr(i+97)] = 0
for i in s:
    occurs[i] += 1

for i in range(26):
    if occurs[chr(i+97)] > times:
        best = [chr(i+97)]
        times = occurs[chr(i+97)]
    elif occurs[chr(i+97)] == times:
        best.append(chr(i+97))

print(" ".join(best))
    