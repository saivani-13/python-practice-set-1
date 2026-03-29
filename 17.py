w1 = input()
w2 = input()

total = 0

for i in range(len(w1)):
    d = abs(ord(w1[i]) - ord(w2[i]))
    print(d, end="-")
    total += d

print("\nTotal:", total)