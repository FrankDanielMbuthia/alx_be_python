from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)

def calculate_future_date():
    days = int(input("Enter a number of days (as an integer): "))
    future_date = datetime.now() + timedelta(days)
    print(future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()