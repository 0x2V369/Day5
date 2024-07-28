# Password Generator Project
import random

# List of letters to be used in password generation (both uppercase and lowercase)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numbers to be used in password generation
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of symbols to be used in password generation
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '-', ',', '.', '[', ']']

# Welcome message to the user
print("Welcome to the PyPassword Generator!")

# Get the number of letters the user wants in their password
nr_letters = int(input("How many letters would you like in your password?\n"))

# Get the number of numbers the user wants in their password
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Get the number of symbols the user wants in their password
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Initialize the password string
password_list = []

# Add random letters to password char list
for i in range(nr_letters):
    password_list += random.choice(letters)

# Add random numbers to password char list
for i in range(nr_numbers):
    password_list += random.choice(numbers)

# Add random symbols to password char list
for i in range(nr_symbols):
    password_list += random.choice(symbols)

# Shuffle the order in password_list to break the order
random.shuffle(password_list)

# Converting list to string
password = ''.join(password_list)

# Display the generated password
print(f"Generated password is: {password}")
