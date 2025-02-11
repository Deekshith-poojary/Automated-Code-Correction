import json,helper

def update_file_with_corrections(file_path, corrections):
    """
    Updates a file with corrected code based on a JSON object.

    Args:
        file_path (str): Path to the file to be updated.
        corrections (dict): A dictionary where keys are line numbers (as strings) and values are corrected code.
    """
    # Step 1: Read the file into a list of lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Step 2: Update the lines based on the corrections
    for line_no, corrected_code in corrections.items():
        # Convert line_no to integer (since JSON keys are strings)
        line_no = int(line_no)
        # Ensure the line number is within the file's range
        if 0 < line_no <= len(lines):
            # Update the line (subtract 1 because list indices start at 0)
            lines[line_no - 1] = corrected_code + '\n'
        else:
            print(f"Warning: Line number {line_no} is out of range for the file.")

    # Step 3: Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

    print(f"File '{file_path}' has been updated with corrections.")
'''
corrections =""" {
    "5": "            return n * done(n - 1)",
    "7": "            return n * done(n - 1)"

}"""
json_data=json.loads(corrections)

update_file_with_corrections(helper.file_path,json_data)
'''