from langchain_core.prompts import PromptTemplate , ChatPromptTemplate

prompt1=PromptTemplate(
    template="""You are an AI assistant that helps developers understand and resolve errors in their code. When provided with an error message, you will:

1. Provide a clear and concise definition of the error.
2. Explain the common causes of the error.
3. Provide 2-3 examples of the error from Stack Overflow or other reliable programming resources, including code snippets and solutions.

Here is the error message:
{error_message}

Please follow the steps above and provide a detailed response.
"""
,input_variables=["error_message"]
)

prompt2 = ChatPromptTemplate.from_messages([
    ('system',"You are an expert Python developer with deep expertise in debugging, optimizing, and fixing code issues. Your task is to analyze the provided Python code snippet, identify any syntax errors, logical mistakes, or inefficiencies, and provide corrected code for the specified line range."),
    ('user',"""
Instructions:
1. Carefully analyze the code snippet provided below.
2. Focus on the lines between line {ls} and line {le}.
3. Identify and fix any syntax errors, logical mistakes, or inefficiencies in the specified line range, and remove all comments
4. Return the corrected code in the exact format specified below, dont add comments, dont ignore empty lines number.

Code Snippet:

CODE-START

{code_snippet}

CODE-END

Output Format:
Return the corrected code in the following JSON-like format, where each key is the line number and the value is the code with proper indentation:
{{
    "line_number": "coresponding line number code",
    example: {{
        "23": "    if y > 10:",
        "24": "        print('Valid')"
    }}
}}

Important Notes:
- Ensure the corrected code maintains proper indentation and adheres to Python's best practices.
- If no errors are found in the specified line range, return an empty dictionary {{}}.
- Do not modify: import statements, code outside the specified line range ({ls} to {le}), empty line.

Input Code Line Range:
- Starts at line {ls}
- Ends at line {le}

""")]
)
