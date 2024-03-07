def multiplication (numbers):
    x = 1
    for i in numbers:
        x = x * int(i)
    return x

numbers = input("Insert numbers: ").split()

print(multiplication(numbers))