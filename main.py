# My Full Name [MAHMOUD HAMDY]
# My First Name [MAHMOUD]
for i in range(1, 7):
    # The Letter M
    if i <= 6:
        print(" ", end="")
    for j in range(1, 16):
        if j <= 6 - i or j >= 10 - i and (j <= 6 + i) or j >= 10 + i:
            print(" ", end="")
        else:
            print("*", end="")
    for j in range(16, 32):
        if j <= 21 - i or j >= 25 - i and (j <= 21 + i) or j >= 25 + i:
            print(" ", end="")
        else:
            print("*", end="")
    print(" ", end="")
    # The Letter A
    for j in range(1, 16):
        if (j <= 6 - i) or (j >= 10 - i and (3 >= i or i == 6)) and (j <= 6 + i) or (j >= 10 + i):
            print(" ", end="")
        else:
            print("*", end="")
    print(" ", end="")
    # The Letter H
    for j in range(1, 13):
        if (5 > i > 2) and (j >= 1) or (j >= 10) or (j <= 3):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end="")

    # The Letter M
    if i <= 6:
        print(" ", end="")
    for j in range(1, 16):
        if j <= 6 - i or j >= 10 - i and (j <= 6 + i) or j >= 10 + i:
            print(" ", end="")
        else:
            print("*", end="")
    for j in range(16, 32):
        if j <= 21 - i or j >= 25 - i and (j <= 21 + i) or j >= 25 + i:
            print(" ", end="")
        else:
            print("*", end="")
    print(" ", end="")
    # The Letter O
    if i <= 3:
        for j in range(1, 10):
            if j <= 3 - i or j >= 7 - i and (j <= 3 + i) or j >= 7 + i:
                print(" ", end="")
            else:
                print("*", end="")
    if i > 3:
        for j in range(1, 10):
            if j <= i - 4 or j >= i and (j <= 10 - i) or j >= 14 - i:
                print(" ", end="")
            else:
                print("*", end="")
    print("  ", end="")

    # The Letter U
    for j in range(1, 13):
        if i > 4 and j >= 1 or j >= 10 or j <= 3:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end="")
    # The Letter D

    for j in range(1, 10):
        if i > 5 or i < 2 or j <= 3 or j >= 10:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(10, 13):
        if 6 > i > 1 and j > 9:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print(" ")

# My Last Name [HAMDY]
for i in range(1, 7):
    # The Letter H
    for j in range(1, 13):
        if (5 > i > 2) and (j >= 1) or (j >= 10) or (j <= 3):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end="")
    # The Letter A
    for j in range(1, 16):
        if (j <= 6 - i) or (j >= 10 - i and (3 >= i or i == 6)) and (j <= 6 + i) or (j >= 10 + i):
            print(" ", end="")
        else:
            print("*", end="")
    print(" ", end="")
    # The Letter M
    if i <= 6:
        print(" ", end="")
    for j in range(1, 16):
        if j <= 6 - i or j >= 10 - i and (j <= 6 + i) or j >= 10 + i:
            print(" ", end="")
        else:
            print("*", end="")
    for j in range(16, 32):
        if j <= 21 - i or j >= 25 - i and (j <= 21 + i) or j >= 25 + i:
            print(" ", end="")
        else:
            print("*", end="")
    print(" ", end="")

    # The Letter D
    for j in range(1, 10):
        if i > 5 or i < 2 or j <= 3 or j >= 10:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(10, 13):
        if 6 > i > 1 and j > 9:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")
    if 4 > i > 0:
        for j in range(1, 10):
            if j <= i - 1 or j > i + 2 and (j <= 7 - i) or j >= 11 - i:
                print(" ", end="")
            else:
                print("*", end="")
    if i > 3:
        for j in range(1, 10):
            if j < 4 or j > 6:
                print(" ", end="")
            else:
                print("*", end="")
    print()