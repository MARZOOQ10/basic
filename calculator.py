def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "cannot divide by zero"
    
while True:
    print("select operation: ")
    print("1.Add ")
    print("2.Subtract  ")
    print("3.Multiply ")
    print("4.Divide ")
    print("5.Exit ")

    choice = input("Enter your choice from (1,2,3,4,5): ")

    if choice == "5":
        print("Exiting calculator!")
        break
    if choice in ('1','2','3','4'):
        num1 = int(input("enter your first number: "))
        num2 = int(input('enter your second number: '))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Input")
