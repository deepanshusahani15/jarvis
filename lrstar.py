for i in range(1,6):

    for space in range(5-i):
        print(" ", end=' ')

    for j in range(i,0,-1):
        print("*", end=' ')

    print()
