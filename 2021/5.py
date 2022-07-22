first = [int(i) for i in input().split()]
second = [int(i) for i in input().split()]
first.sort()
second.sort()
if len(first) != len(second):
    print("False")
else:
    flag = 1
    for i in range(len(first)):
        if first[i] != second[i]:
            flag = 0
            break
    print("True" if flag else "False")