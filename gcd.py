num1 = int(input("Enter the first number: "))#8
num2 = int(input("Enter the second number: "))#12

while num1:
    num2,num1=num1,num2%num1

gcd=num2
print("GCD of", num1, "and", num2, "is:", gcd)