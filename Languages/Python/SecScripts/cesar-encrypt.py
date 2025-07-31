"""
Trying to implement simple Cesar's Cipher in Python
"""


key_encrypt: int = 16
unicode_upper_limit = 0x10FFFF

def my_encrypt(file_name: str, encrypt_key: int) -> str:
    """
    Using a single Cesar Encryption algorithm
    
    args:
    file_name= path to the input file (plain text) to encrypt
    encrypt_key = used to mutate string charachter 

    return: path to the encrypted new file
    """
    
    with open(file_name) as f:
        my_input: list[str] = f.readlines()

    encrypted_lines: list[str] = list()
    
    for l in my_input:
        new_l = change_char(l, encrypt_key)
        encrypted_lines.append(new_l)

    encrypted_lines_name: str = f"encrypted_{file_name}"
        
    with open(encrypted_lines_name, "w") as enc:
        enc.writelines(encrypted_lines)

    
    return encrypted_lines_name


def change_char(file_line:str, key: int) -> str:
    """
    Function used to modify a line using a key value.
    Should convert character alvernatively
    Use their unicode number to do the calculations
    """

    res:list[str] = list()


    for index, c  in enumerate(file_line):
        shift_char_amount = index % unicode_upper_limit 
        if index % 2 == 0:
            res.append(chr(ord(c) + shift_char_amount))
        else:
            res.append(chr(ord(c) - shift_char_amount))

    return "".join(res)
                       

test_change = "test"
new_test_change = change_char(test_change, 6)
        

test = my_encrypt("input-file.txt", key_encrypt)
        
        

    
