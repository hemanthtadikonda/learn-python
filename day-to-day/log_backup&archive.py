#!/usr/bin/env python3

import os
import tarfile
import time

# Directories
log_dir = "."
backup_dir = "backup"

# Ensure backup directory exists
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Generate a weekly timestamp (Year-WeekNumber)
timestamp = time.strftime("%Y_Week%U")
archive_name = f"logs_backup_{timestamp}.tar.gz"
archive_path = os.path.join(backup_dir, archive_name)

# Find log files
log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]

if log_files:

    with tarfile.open(archive_path, "w:gz") as tar:
        for log_file in log_files:
            tar.add(log_file)  # Add each log file to archive

    # Remove original log files after archiving
    for log_file in log_files:
        os.remove(log_file)


    print(f"Archived {len(log_files)} log files to {archive_path}")
else:
    print("No log files found for archiving.")



# #!/usr/bin/env python3
#
# import os
# import shutil
# import time
#
# # Directories
# log_dir = "."
# backup_dir = "backup"
#
# # Ensure backup directory exists
# if not os.path.exists(backup_dir):
#     os.makedirs(backup_dir)
#
# # Generate a weekly timestamp (Year-WeekNumber)
# timestamp = time.strftime("%Y_Week%U")
# archive_name = f"logs_backup_{timestamp}.tar.gz"
# archive_path = os.path.join(backup_dir, archive_name)
#
# # Find log files
# log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
#
# if log_files:
#     shutil.make_archive(archive_path.replace('.tar.gz', ''), 'gztar', log_dir)
#
#     # Remove original log files after archiving
#     for log_file in log_files:
#         os.remove(os.path.join(log_dir, log_file))
#
#     print(f"Archived {len(log_files)} log files to {archive_path}")
# else:
#     print("No log files found for archiving.")
#
#
#

# chmod +x log_backup.py
# crontab -e
# 0 0 * * 0 ./log_backup&archive.py

