n = int(input("Enter terms: "))

a, b = 0, 1
result = []
for i in range(n):
    result.append(a)
    a, b = b, a + b
print(result)
