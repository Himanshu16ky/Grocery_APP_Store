from datetime import datetime, timedelta

def is_past_24_hours(date_and_time):
    # Parse the given date and time string
    given_date = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S.%f")

    # Get the current date and time
    current_date = datetime.now()

    # Calculate the time difference
    time_difference = current_date - given_date

    # Check if the difference is greater than 24 hours
    return time_difference > timedelta(hours=24)

# Example usage
given_date_and_time = "2023-12-11 10:20:37.485436"
if is_past_24_hours(given_date_and_time):
    print("The date and time have passed 24 hours.")
else:
    print("The date and time are within the last 24 hours.")
