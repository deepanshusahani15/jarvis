
def sum_of_digit(n):
    sum =0
    while n>0:
        digit=n%10
        sum = sum + digit
        n=n//10
    return sum
n=int(input("enter a no"))
result = sum_of_digit(n)
print(result)
