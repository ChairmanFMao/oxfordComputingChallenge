numbers = [int(i) for i in input().split()]
print(numbers[1]*numbers[2])
print(f"%.4f" % (numbers[0]/pow(2,numbers[2])))