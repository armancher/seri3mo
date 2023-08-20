x=int(input("enter a number:"))
if x<=1:print("enter a number greater than 1")

else:
    prime=True
    for i in range(2,x):
        if x % i==0:
            prime=False
            break
    if prime:
        print(f"{x} is a prime number")
    else:
        print(f"{x} not prime number")
    