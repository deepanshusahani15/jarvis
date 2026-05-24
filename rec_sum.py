#Sum of Natural Numbers Using Recursion
def total(n):

    if n == 1:
        return 1

    return n + total(n-1)


n = int(input("Enter number: "))

print("Sum =", total(n))
