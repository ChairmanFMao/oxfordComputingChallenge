money = int(input())
towns = [int(i) for i in input().split()]
for i in towns:
    fee = int(money/2)
    if fee < i:
        money -= fee
        money += i

print(money)