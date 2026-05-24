#Reverse String Using Recursion
def reverse(s):

    if len(s) == 0:
        return s

    return s[-1] + reverse(s[:-1])


text = input("Enter string: ")

print("Reverse =", reverse(text))
