text = input()
text += " "
out = ""
ptr = 1
current = text[0]
streak = 1
while (ptr < len(text)):
    if text[ptr] == current:
        streak += 1
    if text[ptr] != current:
        out += current + str(streak)
        streak = 1
        current = text[ptr]
    ptr += 1

print(out)
