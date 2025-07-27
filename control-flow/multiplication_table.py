number = int(input("Enter a number to see its multiplication table: "))
for i in range(1,11):
    product = i * number
    print(str(number) + " * " + str(i) + " = " + str(product))