import os

def extract_new_errors(logfile_path, last_position_file='last_pos.txt'):
    """
    Extracts new errors from the log file since the last position.
    :param logfile_path: Path to the log file.
    :param last_position_file: File to store the last position read.
    :return: New error lines.
    """
    # Ensure the log file exists
    if not os.path.exists(logfile_path):
        print("Log file does not exist.")
        return []

    # Read the last position from the file (default to 0 if the file does not exist)
    if os.path.exists(last_position_file):
        with open(last_position_file, 'r') as f:
            last_position = int(f.read().strip())
    else:
        last_position = 0

    # Open the log file and move to the last known position
    with open(logfile_path, 'r') as log_file:
        # Move to the position where we last read
        log_file.seek(last_position)
        
        # Read all new lines after the last position
        new_errors = []
        for line in log_file:
            # Here you can add more sophisticated error detection
            if 'ERROR' in line or 'Exception' in line:
                new_errors.append(line.strip())
        
        # Update the position for the next time
        new_position = log_file.tell()
        with open(last_position_file, 'w') as f:
            f.write(str(new_position))

    return new_errors

# Example usage
logfile_path = 'logs\global_errors.log'  # Path to your log file
'''
new_errors = extract_new_errors(logfile_path)

# Print out the new errors
if new_errors:
    print("New Errors Found:")
    for error in new_errors:
        print(error)
else:
    print("No new errors found.")
'''