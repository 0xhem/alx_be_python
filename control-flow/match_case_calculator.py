#Requesting number input from users
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Selected operations
add = num1+num2
sub = num1-num2
multi = num1*num2

#Asking the user for operation they'd like to perform
input_prompt = input("Choose the operation (+, -, *, /): " )
if  input_prompt == "+":
    operation = "addition"
elif input_prompt == "-":
    operation = "substraction"
elif input_prompt == "*":
    operation = "multiplication"
elif input_prompt == "/":
    operation = "division"

match operation:
    case "addition":
        print("The result is " + str(add) + ".")
    case "substraction":
        print("The result is " + str(sub) + ".")
    case "multiplication":
        print("The result is " + str(multi) + ".")
    case "division":
        if num2 == 0: #In a case if the user wants to divide by zero; to prevent runtime error
            print("Can't divide by zero.")
        else:
            print("The result is " + str(num1/num2) + ".")
