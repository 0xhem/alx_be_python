#Requesting number input from users
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
add = num1+num2
sub = num1-num2
multi = num1*num2

#Asking the user for operation they'd like to perform
operation = input("Choose the operation (+, -, *, /): " )
if operation == "+":
    result = "addition"
elif operation == "-":
    result = "substraction"
elif operation == "*":
    result = "multiplication"
elif operation == "/":
    result = "division"
else:
    print("Cannot divide by zero")
match result:
    case "addition":
        print("The result is " + str(add) + ".")
    case "substraction":
        print("The result is " + str(sub) + ".")
    case "multiplication":
        print("The result is " + str(multi) + ".")
    case "division":
        if num2 == 0:
            print("Can't divide by zero.")
        else:
            print("The result is " + str(num1/num2) + ".")
