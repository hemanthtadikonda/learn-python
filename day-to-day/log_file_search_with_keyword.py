import os
import re

# Get multiple log files from user input
log_files = input("Enter a list of log files separated by spaces: ").split()

# Get multiple keywords to search for
keywords = input("Enter your keywords separated by spaces: ").split()
keyword_pattern = re.compile(r"|".join(keywords), re.IGNORECASE)  # Regex pattern for all keywords

# Scan each log file
for file in log_files:
    if os.path.exists(file):  # Check if file exists
        with open(file, "r", errors="ignore") as f:
            for line in f:
                if keyword_pattern.search(line):  # Search for any keyword
                    print(f"[{file}] {line.strip()}")

    else:
        print(f"⚠ Warning: File '{file}' not found!")

