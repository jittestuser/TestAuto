from datetime import datetime

# Get current date and time
now = datetime.now()
print(f"Date: {now.date()}")
print(f"Full datetime: {now}")

# Format the date
print(f"Formatted: {now.strftime('%Y-%m-%d')}")