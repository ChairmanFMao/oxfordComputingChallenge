s = input().strip()
layer = 0
down = 1
out = ["","",""]
for i in range(len(s)):
    out[layer] += s[i]
    if layer == 0:
        layer += 1
        down = 1
    elif layer == 1:
        layer += down
    elif layer == 2:
        layer -= 1
        down = -1
print("".join(out))