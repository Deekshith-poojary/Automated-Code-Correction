import tkinter as tk
import tkinter as tk
from tkinter import ttk
import threading
import time

def long_running_function():
    import agentone  # execute agentone
    return agentone.final_answer

def run_function():
    """Runs the long-running function in a separate thread."""
    threading.Thread(target=execute_and_up, daemon=False).start()

def execute_and_up():
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Processing Code...")
    root.after(0, update_result_ui, "Processing Code...")  

    import agenttwo
    result = "file has been updated successfully!"
    root.after(0, update_result_ui, result)  
    root.after(0, lambda: execute_button.pack_forget()) # Update label with result


def execute_and_update():
    """Executes the function and updates the GUI with the result."""
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "loading...")
    result = long_running_function()
    root.after(0, update_result_ui, result)  

    # Show the button after text update
    root.after(0, lambda: execute_button.pack(pady=10)) # Update label with result

def update_result_ui(output):
    # Clear and insert new content
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, output)
    result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Dynamic Error Resolution Tool GUI")
root.geometry("600x400")  # Bigger window for better text display
root.configure(bg="#121212")  # Dark mode background

# Apply dark theme styles
style = ttk.Style()
style.configure("TButton", background="gray", foreground="black", font=("Arial", 11, "bold"))

# Frame to contain text and scrollbar
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Use a Text widget for better readability
result_text = tk.Text(frame, wrap="word", height=15, width=60, bg="#1E1E1E", fg="white",
                    font=("Consolas", 11), padx=10, pady=10, relief=tk.FLAT)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add scrollbar
scrollbar = ttk.Scrollbar(frame, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

# Button (initially hidden)
execute_button = ttk.Button(root, text="🔄 Auto Correct Code", command=run_function)

threading.Thread(target=execute_and_update, daemon=False).start()
root.mainloop()
