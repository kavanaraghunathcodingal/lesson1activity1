num = int(input("Enter a number: "))
count = 0
temp = num
while num != 0:
    num = num // 10
    count += 1

print(f"The number {temp} has {count} digits")
