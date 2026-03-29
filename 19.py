ch = input()
ascii_val = ord(ch)

closest = None
min_dist = float('inf')

for i in range(48, 123):
    if (48 <= i <= 57) or (65 <= i <= 90) or (97 <= i <= 122):
        dist = abs(ascii_val - i)
        if dist < min_dist:
            min_dist = dist
            closest = chr(i)

print("Closest character:", closest)