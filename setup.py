# import tkinter as tk
# from tkinter import messagebox, scrolledtext
# import subprocess
#
#
# def install_requirements():
#     """Install the required dependencies and show real-time logs in the GUI."""
#     # List of dependencies
#     dependencies = [
#         "browser-use==0.1.19",
#         "langchain-google-genai==2.0.8",
#         "pyperclip==1.9.0",
#         "gradio==5.9.1",
#         "langchain-ollama==0.2.2",
#         "langchain-openai==0.2.14",
#     ]
#
#     # Disable the Install button during installation
#     install_button.config(state="disabled")
#     log_text.insert(tk.END, "Starting installation of dependencies...\n")
#     log_text.see(tk.END)
#
#     success = True
#
#     # Install each dependency and update the logs
#     for dep in dependencies:
#         log_text.insert(tk.END, f"Installing {dep}...\n")
#         log_text.see(tk.END)
#         root.update_idletasks()  # Update the GUI in real-time
#
#         try:
#             result = subprocess.run(
#                 ["pip", "install", dep],
#                 capture_output=True,
#                 text=True,
#                 check=True,
#             )
#             log_text.insert(tk.END, result.stdout + "\n")  # Show success message
#         except subprocess.CalledProcessError as e:
#             success = False
#             log_text.insert(tk.END, f"Failed to install {dep}:\n{e.stderr}\n")
#             log_text.see(tk.END)
#
#     if success:
#         log_text.insert(tk.END, "All dependencies installed successfully!\n")
#         messagebox.showinfo("Success", "All dependencies installed successfully!")
#     else:
#         log_text.insert(tk.END, "Some dependencies failed to install. Check logs for details.\n")
#         messagebox.showerror("Error", "Some dependencies failed to install. Check logs for details.")
#
#     log_text.see(tk.END)
#     # Re-enable the Install button
#     install_button.config(state="normal")
#
#
#
#
# # Create the Tkinter GUI
# root = tk.Tk()
# root.title("Web-UI Setup Tool")
# root.geometry("600x400")
#
# # Title Label
# tk.Label(root, text="Web-UI Setup Tool", font=("Arial", 16)).pack(pady=10)
#
# # Instruction Label
# tk.Label(
#     root,
#     text="Click the button below to install all required dependencies.",
#     font=("Arial", 12),
#     wraplength=500,
#     justify="center",
# ).pack(pady=10)
#
# # ScrolledText widget for logs
# log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=70, font=("Courier", 10))
# log_text.pack(pady=10)
#
# # Install Button
# install_button = tk.Button(
#     root,
#     text="Install Dependencies",
#     font=("Arial", 12),
#     bg="green",
#     fg="white",
#     command=install_requirements,
# )
# install_button.pack(pady=10)
#
# # Exit Button
# exit_button = tk.Button(
#     root,
#     text="Exit",
#     font=("Arial", 12),
#     bg="red",
#     fg="white",
#     command=root.destroy,
# )
# exit_button.pack(pady=5)
#
# # Run the Tkinter event loop
# root.mainloop()


import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import os


def install_requirements():
    """Install the required dependencies and show real-time logs in the GUI."""
    # List of dependencies
    dependencies = [
        "browser-use==0.1.18",
        "langchain-google-genai==2.0.8",
        "pyperclip==1.9.0",
        "gradio==5.12.0",
        "langchain-ollama==0.2.2",
        "langchain-openai==0.3.0",
        "playwright==1.49.1"
    ]

    # Disable the Install button during installation
    install_button.config(state="disabled")
    log_text.insert(tk.END, "Starting installation of dependencies...\n")
    log_text.see(tk.END)

    success = True

    # Install each dependency and update the logs
    for dep in dependencies:
        log_text.insert(tk.END, f"Installing {dep}...\n")
        log_text.see(tk.END)
        root.update_idletasks()  # Update the GUI in real-time

        try:
            result = subprocess.run(
                ["pip", "install", dep],
                capture_output=True,
                text=True,
                check=True,
            )
            log_text.insert(tk.END, result.stdout + "\n")  # Show success message
        except subprocess.CalledProcessError as e:
            success = False
            log_text.insert(tk.END, f"Failed to install {dep}:\n{e.stderr}\n")
            log_text.see(tk.END)

    if success:
        log_text.insert(tk.END, "All dependencies installed successfully!\n")
        messagebox.showinfo("Success", "All dependencies installed successfully!")
        create_bat_file()  # Call the function to create the .bat file
    else:
        log_text.insert(tk.END, "Some dependencies failed to install. Check logs for details.\n")
        messagebox.showerror("Error", "Some dependencies failed to install. Check logs for details.")

    log_text.see(tk.END)
    # Re-enable the Install button
    install_button.config(state="normal")


def create_bat_file():
    """Create a .bat file to run the Web-UI."""
    project_dir = os.getcwd()
    bat_content = """@echo off
REM navigate to the project directory
cd  "{project_dir}"

REM Open the WebUI in the default browser
start "" "http://127.0.0.1:7788"

REM Start the WebUI server
python webui.py --ip 127.0.0.1 --port 7788

REM Open the WebUI in the default browser
start "" "http://127.0.0.1:7788"
"""
    try:
        bat_file_path = "start_webui.bat"
        with open(bat_file_path, "w") as bat_file:
            bat_file.write(bat_content)
        log_text.insert(tk.END, f".bat file created: {bat_file_path}\n")
        messagebox.showinfo("Success", "The .bat file was created successfully!")
    except Exception as e:
        log_text.insert(tk.END, f"Error creating .bat file: {e}\n")
        messagebox.showerror("Error", f"Failed to create the .bat file: {e}")


# Create the Tkinter GUI
root = tk.Tk()
root.title("Web-UI Setup Tool")
root.geometry("600x500")

# Title Label
tk.Label(root, text="Web-UI Setup Tool", font=("Arial", 16)).pack(pady=10)

# Instruction Label
tk.Label(
    root,
    text="Click the button below to install all required dependencies.",
    font=("Arial", 12),
    wraplength=500,
    justify="center",
).pack(pady=10)

# ScrolledText widget for logs
log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=70, font=("Courier", 10))
log_text.pack(pady=10)

# Install Button
install_button = tk.Button(
    root,
    text="Install Dependencies",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=install_requirements,
)
install_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    bg="red",
    fg="white",
    command=root.destroy,
)
exit_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
