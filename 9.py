marks = []
for i in range(5):
    marks.append(float(input(f"Enter mark {i+1}: ")))

total = sum(marks)
avg = total / 5

print("Total:", total)
print("Average:", avg)