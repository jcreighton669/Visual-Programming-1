num = 0
sum = 0
print("Enter positive numbers to be added together to stop adding, enter a negative number.")
while num >= 0:
    sum += num
    num = int(input())

print(sum)
