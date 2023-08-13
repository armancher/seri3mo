import math
a=float(input("enter a: \t"))
b=float(input("enter b: \t"))
c=float(input("enter c: \t"))
print(f"a ={a}")
print(f"b ={b}")
print(f"c ={c}")

delta=(b**2)-(4*a*c)
if delta >0:
    x1=(-b + math.sqrt(delta))/(2*a)
    x2=(-b - math.sqrt(delta))/(2*a)
    print(f"x1 is {x1}",f"x2 is {x2}")

    
elif delta==0:
    x=(-b)/(2*a)
    print(f"x is {x}")
   
else:
    print("error delta is negtive")

