from random import *
import string
import sys

def main():
    length = input("enter password length: ")
    try:
        password = generate_password(int(length))
        print(f"your password is: {password}")
    except:
        sys.exit("please enter an intiger number")

def generate_password(l):

    characters = string.ascii_letters + string.punctuation + string.digits
    characters_list = []
    for c in characters:
        characters_list.append(c)

    password = []

    for i in range(l):
        char = choice(characters_list)
        password.append(char)
    
    return "".join(password)

if __name__ == "__main__":
    main()
