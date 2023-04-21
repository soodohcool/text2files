# text2files
Quickly generates a file and directory structure based on an indented text file

## Notes
- The script is written in Python 3.6.  It has not been tested on other versions of Python.

- Make sure your file structure lists any child directory first (before any files on the same level as the parent). This is important because the script will create the directory before creating the file.  If you list files first, the script could fail. 

- Proper Structure Example:
    ``` 
    home
      user
        file1.txt
        file2.txt
      user2
        file3.txt
        file4.txt
    file5.txt
    ```

- INVALID Structure Example:
    ``` 
    home
    file5.txt
      user
        file1.txt
        file2.txt
      user2
        file3.txt
        file4.txt
    ```

## Usage

1. Create a text file with the desired directory structure.  See the examples above.

2. Run the script with the text file as the first argument.  The second argument is the path to the directory where you want the file structure to be created.  If no second argument is provided, the file structure will be created in the current directory.

**Run command:** `python text2files.py <path_to_structure_file.txt>`

Example: `python text2files.py ./example_structure.txt`