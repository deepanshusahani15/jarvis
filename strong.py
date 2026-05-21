
def factorial(n):
    fact = 1
    if n>0:
        for i in range(1,n+1):
            fact = fact*i
    return fact


def strong(n):
    temp = n
    strong_no = 0
    while temp >0:
        digit = temp %10
        strong_no = strong_no + factorial(digit)
        temp = temp//10
    if strong_no == n:
        print(n,"is a strong no")
    else:
        print(n,"is not a strong no")
n=int(input("enter a positive no"))
strong(n)
