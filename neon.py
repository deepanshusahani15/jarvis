
def neon(n):
    sum_of_digit =0
    neon_no = n**2
    while neon_no>0:
        digit=neon_no%10
        sum_of_digit = sum_of_digit + digit
        neon_no=neon_no//10
    return "is neon" if n == sum_of_digit else "is not neon"
n=int(input("enter a no"))
result = neon(n)
print(n, result)
