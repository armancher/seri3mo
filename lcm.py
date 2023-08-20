
num1 = int(input("Enter the first number: "))#8
num2 = int(input("Enter the second number: "))#12


max_num = max(num1, num2)#12
lcm = max_num#12

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max_num

print("LCM of", num1, "and", num2, "is:", lcm)
