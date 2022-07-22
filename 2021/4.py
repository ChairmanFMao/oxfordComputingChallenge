numbers = [int(i) for i in input().split()]
print("".join([chr(i+96) for i in numbers]))