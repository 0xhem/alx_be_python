from datetime import datetime, timedelta

# Printing the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

display_current_datetime()


def calculate_future_date():
    number_of_days = int(input("Enter a number of days: "))
    today = datetime.now()
    futur_date = today + timedelta(days=number_of_days)
    future_date = futur_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

calculate_future_date()