pattern = input("Enter the size of the pattern: ")
while not pattern.isdigit() or int(pattern) <= 0:
    print("That's not a valid positive number!")
    pattern = input("Please enter a positive integer: ")
size = int(pattern)
for row in range(size):
    for col in range(size):
        print("*", end="")  
    print() 