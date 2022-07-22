numbers = [(float(i) if "." in list(i) else int(i)) for i in input().split()]
print(min(numbers))
print(max(numbers))