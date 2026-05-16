try:
    n=int(input("enter a no"))
except Exception as e:
    print(e)
else:
    if n<0:
        print("Negative number")
    elif n>=90 and n<=100:
        print("A")
    elif n>=80 and n<=89:
        print("B")
    elif n>=70 and n<=79:
        print("C")
    elif n>=60 and n<=69:
        print("D")
    elif n<=59:
        print("F")
    else:
        print("Number is not in range")
