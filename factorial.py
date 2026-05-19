
n=int(input("enter a positive no"))
fact = 1
if n>0:
    for i in range(1,n+1):
        fact = fact*i
    print(f"Factorial of {n} is {fact}")
else:
    print("Plz enter positive no")
