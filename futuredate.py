from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Add 2 months to the current date
future_date = current_date + timedelta(days=2*30)
future_date_date = future_date.date()
print(future_date_date)