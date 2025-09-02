# Read the log file.
# Print logs with line numbers.
# Extract structured info (date, time, level, message).
# Save filtered logs to a new file.
# (Optional) Export parsed logs into JSON or CSV.

# Line example:
# 2025-08-17 09:12:01 INFO User 'alice' logged in

import re

with open("app.log", "r") as infile:
    lines = infile.readlines()
    # Pattern to struct the data
    log_pattern = re.compile(
        r"(?P<date>^\d{4}-\d{2}-\d{2})\s+"
        r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
        r"(?P<level>INFO|WARNING|ERROR)\s+"
        r"(?P<message>.*)$"
    )
    structured_data = []
    info_log = []
    warning_log = []
    error_log = []
    # Printing (only for visual purposes)
    for i, line in enumerate(lines, start=1):
        print(f"{i}- {line.strip()}")
    
    for line in lines:
        # Structuring the data
        match = log_pattern.match(line)
        if match:
            data = match.groupdict()
            structured_data.append(data)
            if data["level"] == "INFO":
                info_log.append(line)
            elif data["level"] == "WARNING":
                warning_log.append(line)
            elif data["level"] == "ERROR":
                error_log.append(line)
                
# Saving to files
    
with open("info.log", "w") as infofile:
    infofile.writelines(info_log)
    
with open("warning.log", "w") as warningfile:
    warningfile.writelines(warning_log)
    
with open("error.log", "w") as errorfile:
    errorfile.writelines(error_log)