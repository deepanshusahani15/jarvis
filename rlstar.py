
for i in range(5):

    for space in range(i):
        print(" ", end=' ')

    for j in range(5-i,0,-1):
        print("*", end=' ')

    print()
