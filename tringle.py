a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))
if (a+b)>c or (b+c)>a or (a+c) > b:
    if a==b==c:
        print("equilateral")
    elif a==b or b==c or a==c:
        print("isosceles")
    elif a!=b!=c:
        print("scalene")
else:
    print("Triangle rule failed")
