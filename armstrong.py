
def armstrong(n):
    temp = n
    armstrong_no = 0
    while n>0:
        digit=n%10
        #print("digit", digit)
        armstrong_no = armstrong_no + digit**3
        #print("armstrong no", armstrong_no)
        n=n//10
        #print(n)
    #print("arm strong no", armstrong_no)
    return "is armstrong" if armstrong_no == temp else "is not armstrong"
n=int(input("enter a no"))
result = armstrong(n)
print(n, result)
