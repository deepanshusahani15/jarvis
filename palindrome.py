
def palindrome(n):
    reverse_no = reverse(n)
    print("reverse no", reverse_no)
    if reverse_no == n:
        return True
    else:
        return False
n=int(input("enter a no"))
result = palindrome(n)
print(n, "palindrome status", result)
