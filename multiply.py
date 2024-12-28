# Perform a multiplication by using + by the lowest number of iterations possible

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
result = 0

if num1 < num2:
    for i in range(num1):
        result = result + num2
else:
    for i in range(num2):
        result = result + num1

print(result)
