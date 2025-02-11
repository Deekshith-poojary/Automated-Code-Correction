def getcode(file_path: str):
    """fetch the code to be used by the model with starting and ending line number"""
    with open(file_path, 'r') as file:
        content = file.readlines()  # Read all lines into a list
        ls = 1  # Start line is always 1 (first line in the file)
        le = len(content)  # End line is the last line in the file

    
    code_snippet = ''.join(content) 
    return code_snippet,ls,le
    
file_path = 'test_program.py'  # Specify the path to your Python script
#getcode(file_path)
