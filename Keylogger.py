import os
from datetime import datetime

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# Usage
clear_screen()


def key_logger(text):
    # Specify the file path (use raw string to handle backslashes)
    file_path = r"C:/keylogger"

    # Ensure the directory exists before attempting to write
    if not os.path.exists(file_path):
        os.makedirs(file_path)  # Create the directory if it doesn't exist

    # Get the current date and time
    formatted_date = datetime.now().strftime("%Y-%m-%d")

    # Specify the full file name with path
    filename = os.path.join(file_path, f"{formatted_date}.txt")

    # Get the current time (for each text entry)
    current_time = datetime.now().strftime("%H:%M:%S")
    
    #searching if there is a file that contains the text entry of today's date:
    files = os.listdir(file_path)
    search_term = f"{formatted_date}.txt"

    # adding a condition to append a text on an existing file, or creating a new one:
    if search_term in files:
        # Open the file in append mode ('a'):
        with open(filename, 'a') as file:
            # Write the time, and the text:
            file.write("\n")
            file.write(f"{current_time} - {text}\n\n\n\n\n\n")
            file.write(f"{formatted_date}\n")
            file.write(text)

    else:
        # Open the file in writing mode ('w'):
        with open(filename, 'w') as file:
            # Write the time, and the text:
            file.write("\n")
            file.write(f"{current_time} - {text}\n\n\n\n\n\n")
            file.write(f"{formatted_date}\n")
            file.write(text)

#instructions:
print("Wecome, This is a simple Keylogger that saves every input text in a file named as the insertion's day date.\n")
print("All what you have to do is inserting the text and look for the file in a directory named \"Keylogger\".\n")

# Get the text input and use the function:
text = input("Enter the text you want to save: ")
key_logger(text)