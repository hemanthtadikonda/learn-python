import psutil
import time

log_file = "resource_monitor.log"

while True:
    cpu_percent = psutil.cpu_percent(interval=5)
    ram = psutil.virtual_memory().percent

    log_entry = f"CPU Usage: {cpu_percent}% | RAM Usage: {ram}%\n"

    # Log to file
    with open(log_file, "w") as f:
        f.write(log_entry)

    # Print alert if CPU usage exceeds 80%
    if cpu_percent > 90:
        print(f"ALERT: High CPU usage detected! ({cpu_percent}%)")

    time.sleep(5)  # Sleep before the next check

