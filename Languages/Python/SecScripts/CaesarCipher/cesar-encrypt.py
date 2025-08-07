"""
Trying to implement in Python a version of Caesar Cipher a little more compliacted than the basic one.
This script it's done just for fun and studying not a serious encryption tool.
"""

# Variable to test while coding
# key: int = 20
# key_encrypt: int = 16
# key_decrypt: int = -16

# Support full Unicode range up to 0x10FFFF as read in python docs
UNICODE_UPPER_LIMIT = 0x10FFFF

def caesar_file(file_name: str, key: int) -> str:
    """
    Read a UTF-8 text file, apply a position-dependent Caesar shift
    (subtract at even char indices, add at odd indices), and write out
    the result to a new file.

    Args:
        input_path: Path of the UTF-8 file to transform.
        key: Number of code points to shift (positive or negative).

    Returns:
        The filename of the newly written file.
    """


    # Read the input file and read it with readlines
    with open(file_name) as f:
        my_input: list[str] = f.readlines()

    # Here will be stored the encrypted version of each line    
    encrypted_lines: list[str] = list()

    # Read each original line, transform it and append to the encrypted_lines list
    for l in my_input:
        new_l = change_char(l, key)
        encrypted_lines.append(new_l)
        
    # Construct the output filename by prefixing “encrypted_” to the original name
    encrypted_lines_name: str = f"encrypted_{file_name}"

    # Wtire on the destination file the new transformed version og the input file
    with open(encrypted_lines_name, "w") as enc:
        enc.writelines(encrypted_lines)

    # The name of the new file is returned to user
    return encrypted_lines_name


def change_char(file_line:str, key: int) -> str:
    """
    Function used to modify a line using a key value.
    Should convert character alvernatively
    Use their unicode number to do the calculations
    """
 """
    Shift each character in `line` by +key or –key depending on its index:
      on even index -> subtract key
      on odd index -> add key

    Control characters (newline, carriage return) are left unchanged,
    so that line breaks survive encryption/decryption.

    Args:
        line: One line of text (may include trailing newline).
        key: Shift amount (positive to encrypt, negative to decrypt).

    Returns:
        The transformed line as a new string.
    """
    
    # var used to return the transformed line
    res: list[str] = list()
    # this values is used as modulo to ensure converting char <--> int
    # is always supported for each unicode value and not out of supported range 
    my_mod = UNICODE_UPPER_LIMIT + 1
        
    for index, c  in enumerate(file_line):
        shift_amount: int = key
        
        # If it’s a newline or carriage‐return, let it as is and append:
        if c in ("\n", "\r"):
            res.append(c)
            continue

        # This if add a little more complexity to the algorithm
        # by checking if index is odd or even
        # if even use opposite shift_amount
        if index % 2 == 0:
            shift_amount = -shift_amount

        # input char converted to int
        orig_code: int = ord(c) 
        # getting the new value for the char to transsform 
        new_code: int = (orig_code + shift_amount) % my_mod 
        res.append(chr(new_code)) # appending to the result var

    # returning the string by combining all transformed char
    return "".join(res)
                       

# Tests while coding
# test_change = "test"
# new_test_change = change_char(test_change, 6)       
# test = my_encrypt("input-file.txt", key_encrypt)
# test_decrypt = my_encrypt(test, key_encrypt)


if __name__ == "__main__":

    # Tests working
    # # test with hardoced file paths
    # # 1) encrypt
    # encrypted_file = caesar_file("test-lorem-ipsum-20par.txt", key)
    # # 2) decrypt (same function, same key)
    # decrypted_file = caesar_file(encrypted_file, -key)

    # print("Encrypted to:", encrypted_file)
    # print("Decrypted to:", decrypted_file)
        
    my_input_file = inpu(""
