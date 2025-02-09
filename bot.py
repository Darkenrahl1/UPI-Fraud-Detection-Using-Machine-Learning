import os
import time

# List of files with desired dates
files_with_dates = [
    {'file':'app.py','date':'2024-03-12 22:15:50'},
    {'file':'model.ipynb','date':'2024-03-14 22:15:50'},
    {'file':'README.md','date':'2024-03-15 22:15:50'},
    {'file':'static','date':'2024-03-16 22:15:50'},
    {'file':'templates','date':'2024-03-19 22:15:50'},

]

for entry in files_with_dates:
    file_path = entry["file"]
    date_str = entry["date"]

    # Convert date string to timestamp
    timestamp = time.mktime(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))

    # Set last modified time
    os.utime(file_path, (timestamp, timestamp))
    print(f"Updated {file_path} to {date_str}")
