task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

while priority not in ("high", "medium", "low"):                # To make sure the right argument is passed
    print("Please enter a valid priority: " )
    priority = input("Priority (high / low / medium): ")

while time_bound not in ("yes" "no"):                          # To make sure the right argument is passed
    print("Invalid response. Type yes/no")
    time_bound = input("IS it time bound? ( yes / no): ")

match priority:                                                 # Passing match cases
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is high priority. Manage it accordingly")
    case "medium":
        if time_bound == "yes":
           print(f"Reminder: {task} is a medium priority, but time bound. Get it to it")
        else:
            print(f"Reminder: {task} is a medium priority. Get it done when you are available")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is low priority, but time bound.")
        else:
            print(f"{task} is low priority. Get it done at your convinience")

"""
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
"""
print()
#print(reminder)