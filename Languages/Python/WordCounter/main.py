"""
Simple script to practice spcripting in python.
Take a plain text file in input and return the number of words.
"""
import sys


def words_count(file_content: str) -> int:
    """
    Utility function to encapsulate the counting logic.
    If later you want more complex method it's easier to have it here.
    """
    return len(file_content.split())


def main(input_file: str):
    """
    Here my main script logic to process input file
    """
    try:
        filename = my_input
        # Try to open and read the file

        with open(input_file, 'r') as f:
            content = f.read()
            # test -> OK
            # print(content)
            counts = words_count(content)
            print(f"You file have: {counts} words\n")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")

    except PermissionError:
        print("Error: You do not have permission to read this file.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':

    my_input = ""
    if len(sys.argv) == 2:  # TODO: check input is valid
        # Here input is given from terminal
        my_input = sys.argv[1]
    else:
        my_input = input("Insert file path here:")

    main(my_input)  # Here launching the main function
