import os

def clear_screen():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')  # Use 'cls' command to clear the screen on Windows
    else:
        os.system('clear')  # Use 'clear' command to clear the screen on Unix/Linux/MacOS

# Example usage
clear_screen()

# Introduction to the code:
print("Welcome, this program is a simple encryption and decryption tool based on a key you can choose. \n")
print("First, do you want the encryption tool or decryption?\n")
print("Press (1) for encryption \n")
print("Press (2) for decryption \n")

# Choice of the tool:
choice = int(input("Please insert your choice: "))

# Encryption tool:
if choice == 1:
    ascii_list = []

    def text_to_ascii(text):  # Define the function to transform the text to ASCII.
        for char in text:
            ascii_list.append(ord(char))
        return ascii_list

    cipher = input("Please enter the text to encrypt: ")  # User inputs the text they want to encrypt

    # Convert input text to ASCII values
    text_to_ascii(cipher)

    def encrypt(text, key):  # Define the encryption function.
        encrypted_text = ""
        for char in text:
            # Correct the logic to set 'm' based on the character itself
            if char.isupper():
                m = 65
            elif char.islower():
                m = 97
            else:
                m = 0

            if m == 0:
                encrypted_char = char  # Keep non-alphabetic characters unchanged
            else:
                encrypted_char = chr((ord(char) - m + key) % 26 + m)
            
            encrypted_text += encrypted_char
        return encrypted_text

    key = int(input("Please enter the encryption key: "))  # Define the encryption key.

    encrypted = encrypt(cipher, key)

    print("Encrypted text is:", encrypted)

if choice == 2:
    ascii_list = []

    def text_to_ascii(text):  # Define the function to transform the text to ASCII.
        for char in text:
            ascii_list.append(ord(char))
        return ascii_list

    cipher = input("Please enter the text to decrypt: ")  # User inputs the text they want to decrypt

    # Convert input text to ASCII values
    text_to_ascii(cipher)

    def decrypt(text, key):  # Define the decryption function.
        decrypted_text = ""
        for char in text:
            # Correct the logic to set 'm' based on the character itself
            if char.isupper():
                m = 65
            elif char.islower():
                m = 97
            else:
                m = 0

            if m == 0:
                decrypted_char = char  # Keep non-alphabetic characters unchanged
            else:
                decrypted_char = chr((ord(char) - m - key) % 26 + m)  # Corrected decryption logic
            
            decrypted_text += decrypted_char
        return decrypted_text

    key = int(input("Please enter the decryption key: "))  # Define the decryption key.

    decrypted = decrypt(cipher, key)

    print("Decrypted text is:", decrypted)
