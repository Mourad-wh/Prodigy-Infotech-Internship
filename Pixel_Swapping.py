import os
import numpy as np
from PIL import Image

#clearing the terminal:
def clear_screen():
    """Clear the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

#checking if the file exists:
def file_exists(filepath):
    """Check if a file exists."""
    return os.path.isfile(filepath)

#function is designed to ensure that a user input is a valid integer 
# and, if specified, meets a minimum value requirement, it will be used to check block size.
def validate_integer_input(prompt, min_value=None):
    """Validate user input to ensure it is an integer and meets the minimum value requirement."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a value greater than or equal to {min_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

#this function is for encryption:
def image_encrypter(image_path, block_size, output_path):
    """Encrypt the image by shuffling its blocks."""
    # Open the image and convert it to a numpy array
    image = Image.open(image_path)
    image_array = np.array(image)

    # Get image dimensions
    height, width, channels = image_array.shape

    # Ensure the image dimensions are divisible by the block size
    height = (height // block_size) * block_size
    width = (width // block_size) * block_size
    image_array = image_array[:height, :width, :]

    # Create a list to hold the blocks
    blocks = []

    # Divide the image into blocks
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = image_array[i:i+block_size, j:j+block_size, :]
            blocks.append(block)

    # Flatten the blocks list into a single array
    flat_blocks = np.array(blocks).reshape(-1, block_size * block_size * channels)

    # Generate or use the encryption key to shuffle the blocks
    encryption_key = input("Please insert the encryption key (0-250): ")
    np.random.seed(int(encryption_key))  # Use the key as a seed for reproducibility
    np.random.shuffle(flat_blocks)

    # Reshape the flat_blocks back to the original block format
    encrypted_blocks = flat_blocks.reshape(-1, block_size, block_size, channels)

    # Create an empty array to hold the encrypted image
    encrypted_image = np.zeros_like(image_array)

    # Reconstruct the image with the shuffled blocks
    block_index = 0
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            encrypted_image[i:i + block_size, j:j + block_size, :] = encrypted_blocks[block_index]
            block_index += 1

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_image)
    encrypted_img.save(output_path)

    print(f"Encrypted image saved as {output_path}")
    return encryption_key


#decrypting the image:
def image_decrypter(image_path, block_size, output_path, encryption_key):
    """Decrypt the image by reversing the block shuffling process."""
    # Open the encrypted image and convert it to a numpy array
    encrypted_image = Image.open(image_path)
    encrypted_image_array = np.array(encrypted_image)

    # Get image dimensions
    height, width, channels = encrypted_image_array.shape

    # Ensure the image dimensions are divisible by the block size
    height = (height // block_size) * block_size
    width = (width // block_size) * block_size
    encrypted_image_array = encrypted_image_array[:height, :width, :]

    # Create a list to hold the blocks
    blocks = []

    # Divide the encrypted image into blocks
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = encrypted_image_array[i:i+block_size, j:j+block_size, :]
            blocks.append(block)

    # Flatten the blocks list into a single array
    flat_blocks = np.array(blocks).reshape(-1, block_size * block_size * channels)

    # Generate the same permutation key using the encryption key
    np.random.seed(int(encryption_key))  # Use the same seed as in the encryption process
    original_indices = np.random.permutation(len(flat_blocks))

    # Initialize an array to hold the decrypted blocks
    decrypted_blocks = np.zeros_like(flat_blocks)

    # Re-arrange the blocks back to their original positions
    for i, original_index in enumerate(original_indices):
        decrypted_blocks[original_index] = flat_blocks[i]

    # Reshape the decrypted blocks back to the original block format
    decrypted_blocks = decrypted_blocks.reshape(-1, block_size, block_size, channels)

    # Create an empty array to hold the decrypted image
    decrypted_image = np.zeros_like(encrypted_image_array)

    # Reconstruct the image with the decrypted blocks
    block_index = 0
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            decrypted_image[i:i + block_size, j:j + block_size, :] = decrypted_blocks[block_index]
            block_index += 1

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_image)
    decrypted_img.save(output_path)

    print(f"Decrypted image saved as {output_path}")


def main():
    print("Welcome, this program is a simple tool to encrypt and decrypt images.\n")
    while True:
        
        choice = input("Insert (1) to encrypt, or (2) to decrypt: ") 
        print("\n")
        if choice in ['1', '2']:
            break
        else:
            print("Please enter a valid option (1 or 2).\n")
            print("\n")

    if choice == '1':
        while True:
            print("To insert the image's path make sure to do a right click on the image then choose the option (copy path)\n")
            print("And please meke sure to delete the \"\" before you validate the path to avoid having problems with the code.\n")
            print("And also make sure to rename your image while inserting the path to save it.\n")
            print("Thank You! And Enjoy (; \n")
            image_path = input("Please enter your image's path: ")
            print("\n")
            if file_exists(image_path):
                break
            else:
                print("File not found. Please enter a valid path.\n")

        output_path = input("Please enter the path where your image will be saved: ")
        print("\n")
        block_size = validate_integer_input(f"Please enter the block size (1-100): ", min_value=1)
        print("\n")
        encryption_key = image_encrypter(image_path, block_size, output_path)
        
        print("Encryption completed successfully!\n")
        print("Save this key to decrypt the image later.\n")
        print(f"Encryption Key (copy this):  {encryption_key}\n")

    elif choice == '2':
        while True:
            print("To insert the image's path make sure to do a right click on the image then choose the option (copy path)\n")
            print("And please make sure to delete the \"\" before you validate the path to avoid having problems with the code.\n")
            print("And also make sure to rename your image while inserting the path to save it.\n")
            image_path = input("Please enter your encrypted image's path: ")
            print("\n")
            if file_exists(image_path):
                break
            else:
                print("File not found. Please enter a valid path.\n")

        output_path = input("Please enter the path where your decrypted image will be saved: ")
        print("\n")
        encryption_key_str = input("Please enter the encryption key: ")
        
        block_size = validate_integer_input("Please enter the block size: ", min_value=1)

        image_decrypter(image_path, block_size, output_path, encryption_key_str)
        print("Decryption completed successfully!")


if __name__ == "__main__":
    main()
