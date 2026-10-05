a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a<b:
    min=a
else:
    min=b
gcd=1
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        gcd=i
print(f"The GCD of {a} and {b} is {gcd}")
