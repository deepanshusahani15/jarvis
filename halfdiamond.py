
n = 5

# Upper part
for i in range(1, n + 1):

    # spaces
    for j in range(n - i):
        print("  ", end='')

    # stars
    for k in range(i):
        print("* ", end='')

    print()


# Lower part
for i in range(n - 1, 0, -1):

    # spaces
    for j in range(n - i):
        print("  ", end='')

    # stars
    for k in range(i):
        print("* ", end='')

    print()
