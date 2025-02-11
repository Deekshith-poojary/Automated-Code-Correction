# Automated Code Correction Framework

## Overview

The **Automated Code Correction Framework** is an AI-powered debugging tool designed to automate error detection and correction. It streamlines the debugging process by analyzing errors, providing relevant solutions, and applying corrections to faulty code. Implemented in Python, the system leverages **LangChain** for AI-driven automation.

## Features

- **Logger:** Captures and stores errors from executed programs in a log file.
- **AI Agent 1:** Extracts errors, explains their causes, and provides relevant examples from sources like Stack Overflow in a GUI.
- **AI Agent 2:** Extracts faulty code, sends it to a Large Language Model (LLM) for correction, and replaces the erroneous lines with the fixed code.
- **Automated Debugging:** Reduces manual effort and enhances development efficiency.
- **GUI:** Shows the error analysis in a GUI.

## Technologies Used

- **Python**
- **LangChain** (for AI agents)
- **Large Language Model (LLM)** (for code correction)
- **Python Tkinter** (for displaying error analysis and examples)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Deekshith-poojary/Automated-Code-Correction.git
   cd Automated-Code-Correction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your LLM API keys in `agentone.py` and `agenttwo.py`:
   - The project uses **Google Gemini AI API Key** by default.
   - Users can also configure **OpenAI** or **Claude** API keys as alternatives.

## Usage

1. Simply run your error-prone program file by importing the `global_logger` module:
   ```python
   import global_logger
   ```
   Example usage:
   ```python
   import global_logger

   print(3/0)#it will through division by zero error.
   ```
3. The framework will automatically capture errors, analyze them, and provide corrected solutions.
4. View debugging insights and corrected code in the GUI.

## Contribution

Feel free to contribute to the project by submitting pull requests. Ensure your code follows best practices and includes proper documentation.

## License

This project is licensed under the MIT License.

## Contact

For queries or contributions, reach out to [deekshithpoojary122d@gmail.com](mailto\:deekshithpoojary122d@gmail.com).

