n = int(input())
if n > 200:
    n *= 0.8
elif n > 100:
    n *= 0.85
elif n > 50:
    n *= 0.9

print(int(n))