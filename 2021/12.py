n = int(input())
original = [int(input()) for i in range(n)]
done = sorted(original)

left = 0; right = n-1
while original[left] == done[left] and left < n-1:
    left += 1
while original[right] == done[right] and right > 0:
    right -= 1

if left < right:
    print(left)
    print(right)
else:
    print("sorted")