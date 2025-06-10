task = input("Enter your task: ")
priority = input("Priority ( high / medium / low ): ").lower
time_bound = input("Is it time bound? ( yes / no: ) ").lower

while priority not in ("high", "medium", "low"):                # To make sure the right argument is passed
    print("Please enter a valid priority: " )
    priority = input("Priority (high / low / medium): ").lower

while time_bound not in ("yes", "no"):                          # To make sure the right argument is passed
    print("Invalid response. Type yes/no")
    time_bound = input("IS it time bound? ( yes / no): ").lower

match priority:                                                 # Passing match cases
    case "high":
        if time_bound == "yes":
            reminder = (f"{task} is a high priority task that requires immediate attention today!")
        else:
            reminder = (f"{task} is high priority. Manage it accordingly")
    case "medium":
        if time_bound == "yes":
            reminder = (f"{task} is a medium priority, but time bound. Get it to it")
        else:
            reminder = (f"{task} is a medium priority. Get it done when you are available")
    case "low":
        if time_bound == "yes":
            reminder = (f"{task} is low priority, but time bound.")
        else:
            reminder = (f"{task} is low priority. Get it done at your convinience")

print()
print(reminder)