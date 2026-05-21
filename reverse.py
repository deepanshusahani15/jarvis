
def reverse(n):
    reverse_no = 0
    while n>0:
        last_digit=n%10
        #print(last_digit)
        reverse_no=reverse_no*10+last_digit
        #print(reverse_no)
        n=n//10
        #print(n)
    return reverse_no
n=int(input("enter a no"))
print("original no is",n)
result = reverse(n)
print("reverse no is", result)
