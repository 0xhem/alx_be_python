def perfrom_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Please enter a valid second number"
            else:
                return num1 / num2
        case _:
            return "Error: Invalid operation"
perfrom_operation(2,3,"add")
