# Program Name: Lab11.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab11
# Due Date: 24/11/24
# Purpose: This program manages a text file called users.txt. It provides functionality to create the file,
#          add usernames, update usernames, and remove usernames.
# Resources: IT1114 course materials

import os

def create_file():
    """Creates an empty file named users.txt in the current directory."""
    with open("users.txt", "w") as file:
        pass  # File is created empty

def add_user(username):
    """Appends a username to the users.txt file."""
    with open("users.txt", "a") as file:
        file.write(username + "\n")

def update_user(old_username, new_username):
    """
    Replaces any instance of old_username with new_username in the users.txt file.
    """
    if not os.path.exists("users.txt"):
        print("File does not exist. Use create_file() first.")
        return
    with open("users.txt", "r") as file:
        lines = file.readlines()
    with open("users.txt", "w") as file:
        for line in lines:
            # Replace matching username
            if line.strip() == old_username:
                file.write(new_username + "\n")
            else:
                file.write(line)

def remove_user(username):
    """
    Removes the specified username from the users.txt file.
    """
    if not os.path.exists("users.txt"):
        print("File does not exist. Use create_file() first.")
        return
    with open("users.txt", "r") as file:
        lines = file.readlines()
    with open("users.txt", "w") as file:
        for line in lines:
            if line.strip() != username:  # Write only lines not matching the username
                file.write(line)
