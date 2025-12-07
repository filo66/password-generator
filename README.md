# Password Generator

A simple Python script that generates a random password using letters, digits, and punctuation.

# Description

This file contains a simple Python program that generates a random password based on a length provided by the user. The script asks the user to enter the password length, checks that the input is an integer, and then creates a password using random characters from letters, digits, and punctuation.

The main function handles user input and error checking. If the input is valid, it calls `generate_password()`, which builds a list of allowed characters and randomly selects from them to form the final password. If the user enters something that isn't an integer, the program exits with an error message.

The file is fully self-contained and requires only Python’s built-in libraries: `random`, `string`, and `sys`.


## Features
- Generates a random secure password.
- Uses uppercase letters, lowercase letters, digits, and symbols.
- Interactive command-line input.

## How to Use
Run the script:

python password_generator.py
Enter the password length when prompted:

enter password length: 12

your password is: A$f9kL@2qP!x

# Description
main() handles user input and displays the generated password.

generate_password(l) creates a password of length l using random characters.

If the user enters a non-integer value, the program exits with an error message.

# Requirements

Python 3.x
No external libraries required.
