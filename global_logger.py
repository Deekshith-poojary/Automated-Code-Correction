import logging
import os
import sys
import traceback
import ast

# Ensure logs directory exists
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)

# Configure global logging
logging.basicConfig(
    filename=os.path.join(log_directory, "global_errors.log"),  # Log file
    level=logging.ERROR,  # Capture only errors and above
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s"  # Format with filename
)

def log_exception(exc_type, exc_value, exc_traceback):
    """Global function to log all syntax and runtime errors."""
    if issubclass(exc_type, SyntaxError):
        error_msg = f"Syntax Error: {''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)).replace(chr(10), ' ')}"
    else:
        error_msg = f"Runtime Error: {''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)).replace(chr(10), ' ')}"

    logging.error(error_msg)
    print(error_msg)
    import main
    main.error_msg=error_msg
    main.mains()

# Attach global exception handler for runtime errors
sys.excepthook = log_exception

def check_syntax():
    """Checks for syntax errors in the script that imports this module."""
    if len(sys.argv) > 1:
        script_path = sys.argv[1]  # Get the main script name

        try:
            with open(script_path, "r", encoding="utf-8") as f:
                script_code = f.read()
            
            # Parse the script before execution to catch syntax errors
            ast.parse(script_code, filename=script_path)

        except SyntaxError as e:
            log_exception(SyntaxError, e, None)
            sys.exit(1)  # Stop execution if a syntax error is found

# Run syntax check when imported
#check_syntax()
