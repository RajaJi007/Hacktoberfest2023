n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*', end='')
    if i > 1:
        print(' ' * (2 * i - 3) + '*')
    else:
        print()
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*', end='')
    if i > 1:
        print(' ' * (2 * i - 3) + '*')
    else:
        print()
