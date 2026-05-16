weight=int(input("enter weight in kg"))
height=float(input("enter height in cm"))
bmi= weight/height**2
print("bmi:", bmi)
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("normal")
elif bmi>=25 and bmi<=29.9:
    print("overweight")
elif bmi>=30:
    print("obese")
