num = int(input("Enter a number: "))

div_sum = 0
for i in range(1, num):
    if num % i == 0:
        div_sum += i

if div_sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
