from copy import deepcopy

class Pair:
    def __init__(self,numbers):
        self.first = numbers[0]
        self.second = numbers[1]

def compare(one):
    return one.first + one.second

n = int(input())
pairs = [Pair([int(i) for i in input().split()]) for j in range(n)]
done = deepcopy(pairs)
done.sort(key = compare)

flag = 0

for i in range(n):
    if pairs[i].first != done[i].first or pairs[i].second != done[i].second:
        flag = 1
        break

if flag:
    for i in done:
        print(i.first,i.second)
else:
    print("sorted")