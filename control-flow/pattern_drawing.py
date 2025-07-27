size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for i in range(size):
        print("*", end="")# print asterisk without a new line
    print()# print a new line after every row
    row += 1