import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Usage
clear_screen()

#this function is used to check the password complexity:
def check(password):
    length = len(password)  #checking the length
    majuscule = sum(1 for char in password if 'A' <= char <= 'Z')  #checking the uppercase characters
    minuscule = sum(1 for char in password if 'a' <= char <= 'z')  #checking the lowercase characters
    special_characters = sum(1 for char in password if char in '!@#$%^&*_=+[]{}|;:,.<>?/')  #checking the special characters
    numbers = sum(1 for char in password if '0' <= char <= '9')   #checking the numbers

    return length, special_characters, numbers, majuscule, minuscule

# This function is used to count the criteria satisfied by your password:
def counter(length, special_characters, numbers, majuscule, minuscule):
    criteria = 0

    if length >= 8:
        criteria += 1

    if special_characters >= 3:
        criteria += 1

    if numbers >= 3:
        criteria += 1

    if majuscule >= 3:
        criteria += 1

    if minuscule >= 3:
        criteria += 1
    
    return criteria

#This function helps you build a strong password that satisfies our criteria:
def builder():
    print("I will give you a simple tool to make your password complex enough to satisfy our criteria.\n")
    while True:
        name = input("Write your full name with capital letters:  ")
        if name.isupper():
            break
        else:
            print("Your name must be written only with capital letters.")


    print("Good! Now let's replace the vowel letters (A-E-U-O-I) with numbers (1-2-3-4-5-6-7-8-9). \n")
    print("For example: M1R2D3L45T6K\n")
    while True:
        no_vowels = input("Show me what you got, champion: ")
        if all(char not in 'AEIOU' for char in no_vowels):
            break
        else:
            print("Pay attention, we said it shouldn't contain any vowels.")


    print("WELL DONE! Now after every number, add a special character (ex: ! @ # $ % ^ * + = - _)\n")
    print("For example: M1!R2@D3#L4$5%T6^K\n")
    while True:
        special_characters = input("You're almost there: ")
        special_count = sum(1 for char in special_characters if char in '!@#$%^&*_=+[]{}|;:,.<>?/')
        if special_count >= 3:
            break
        else:
            print("You need to add more special characters, champ.")
            

    print("GOOD JOB!!! Now let's add lowercase characters.\n")
    print("Pick 3 of the remaining uppercase characters and write them in lowercase.\n")
    while True:
        lower_case = input("Let's finish this: ")
        minuscule = sum(1 for char in lower_case if 'a' <= char <= 'z')
        if minuscule >= 3:
            break
        else:
            print("Pay attention, you have to add at least 3 lowercase characters.")

    print(f"You made it! Here's your password: {lower_case}")

# Main algorithm
print("Welcome! This algorithm is a password complexity checker. To make sure that your password will satisfy our criteria, please follow the instructions below: \n")
print("Your password must contain at least:\n- 12 characters as mentionned bellow:\n   *3 special characters (!@#$%^&*_+=-:;)\n   *3 numbers\n   *3 uppercase letters\n   *3 lowercase letters.\n")
choice = input('If you understand, please type "ok" to continue, if not, type "no" to display an example, or type "build" to help you build your own secure password: ')

# Correct input validation
while choice not in ['ok', 'no', 'build']:
    choice = input('Come on man, it\'s easy, just type (ok) - (no) - (build): ')

if choice == 'no':
    print('Your password should be similar to this one: "M1!2@r3#D4$l5%6^7&T8*k"\n')
    choice = input('If you want to build your own secure password, type "build": ')
    if choice == 'build':
        builder()

elif choice == 'build':
    builder()
    
elif choice == 'ok':
    password = input("Please insert your password: ")
    criteria = counter(*check(password))

    while criteria < 5:  # Loop until the password is strong enough
        if criteria < 1:
            password = input("Your password is too weak, please try again with a stronger password: ")
        elif 1 <= criteria < 2:
            password = input("Your password is almost there, please try again: ")
        elif 2 <= criteria < 3:
            password = input("You're getting closer, but the password is still not strong enough: ")
        elif 3 <= criteria <= 4:
            password = input("The password is better, but it still needs improvement: ")
        
        criteria = counter(*check(password))

    if criteria >= 5:
        print("Your password is perfect! Your security matters.")
