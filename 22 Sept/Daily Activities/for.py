def multiplication_table(num):
    print (f"Multiplication_table of {num}")
    for i in range (1,11):
        result = num * i
        print (f"{num} x {i} = {num * i}")

#eg
number = int(input("Enter a number: "))
multiplication_table(number)
