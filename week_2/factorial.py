num = int(input("Enter a number to find the factorial: "))

count = 1
for i in range(1,num+1):
    count *= i

print(count)
