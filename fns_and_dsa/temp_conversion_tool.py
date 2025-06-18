FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32




temperature = float(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if degree == "C":
    f = convert_to_celsius(temperature)
    print(f"{temperature}°C is {f}°F ")
elif degree == "F":
    c = convert_to_fahrenheit(temperature)
    print(f"{temperature}°F is {c}°C")
else:
    print("Invalid temperature. Please enter a numeric value")
