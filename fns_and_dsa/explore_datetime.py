from datetime import datetime, timedelta

# Printing the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

display_current_datetime()


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.now()
    future_date = today + timedelta(days=number_of_days)
    futur_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {futur_date}")

calculate_future_date()