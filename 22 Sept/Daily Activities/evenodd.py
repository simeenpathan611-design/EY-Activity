def check_number(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


#eg
number = int(input("Enter a number: "))
result = check_number(number)
print(result)
