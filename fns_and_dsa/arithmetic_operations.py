def perfrom_operation(num1, num2, operation = ("add", "substract", "multiply", "divide")):   
    match operation:
        case "add":
            result = num1 + num2
        case "substract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                print("Please enter a valid second number")
            else:
                result = num1 / num2
    print(result)

perfrom_operation(2,4,"multiply")