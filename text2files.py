# Kenny G Scott - 2023
# https://github.com/soodohcool

# Standard library imports
import os
import sys

# This function creates a directory structure based on the provided text structure
def create_structure(structure_text):
    # Split the text structure into separate lines
    lines = structure_text.splitlines()

    # Create an empty list to act as a stack
    stack = []

    # Loop through each line in the text structure
    for line in lines:
        # Remove any whitespace at the end of the line
        line = line.rstrip()

        # If the line is empty, skip to the next line
        if not line:
            continue

        # Determine the amount of indentation on the line
        indent = len(line) - len(line.lstrip())

        # Remove any whitespace at the beginning and end of the line
        line = line.strip()

        # Remove any elements from the stack that have a greater or equal indentation
        while stack and stack[-1][1] >= indent:
            stack.pop()

        # If the line contains a dot (.) character, it represents a file
        if '.' in line:
            # Construct the file path by joining the directory names in the stack with the file name
            file_path = os.path.join(*(dir_name for dir_name, _ in stack), line)

            # Get the parent directory of the file path
            parent_dir = os.path.dirname(file_path)

            # If the parent directory exists, create it. Otherwise, do nothing
            if parent_dir:
                os.makedirs(parent_dir, exist_ok=True)

            # Create the file and leave it empty
            with open(file_path, 'w') as f:
                pass
        else:
            # If the line does not contain a dot (.) character, it represents a directory

            # Append the directory name and its indentation level to the stack
            stack.append((line, indent))

            # Construct the directory path by joining the directory names in the stack
            dir_path = os.path.join(*(dir_name for dir_name, _ in stack))

            # Create the directory if it does not exist
            os.makedirs(dir_path, exist_ok=True)

# This function reads in the contents of a file and returns them as a string
def read_structure_from_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

# If this script is run directly (not imported as a module)
if __name__ == '__main__':
    # If the script is not provided with a file name argument, print usage instructions and exit
    if len(sys.argv) < 2:
        print('Usage: python text2files.py <structure_file>')
        sys.exit(1)

    # Get the file name from the script argument
    file_name = sys.argv[1]

    # Read the contents of the file
    structure_text = read_structure_from_file(file_name)

    # Create the directory structure based on the contents of the file
    create_structure(structure_text)
