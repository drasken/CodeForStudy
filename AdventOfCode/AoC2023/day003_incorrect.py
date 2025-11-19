

class Numero:
    def __init__(self, numero, start, end, riga):
        self.numero = numero
        self.start = start
        self.end = end
        self.riga = riga

    def __repr__(self):
        return (f"Il numero {self.numero} comincia a {self.start} e finisce a {self.end} sulla riga {self.riga}.")

    def has_symbol_near(self, file_input):
        set_near_value = set()

        for row_num, row in enumerate(file_input[(self.riga - 1): (self.riga + 2)]):
            for col_num, num in enumerate(row[(self.start - 1): (self.end + 2)]):
                if not num.isdigit() and num != ".":
                    return True
        return False

        """
        close_symbol = {{x for x in row[(self.start - 1): (self.end + 2)]}
                        for row in file_input if row == (self.riga - 1) or row == (self.riga + 2)}
        
        close_symbol.add(file_input[self.riga][(self.start - 1)])
        if self.riga >= (len(file_input) - 1):
            close_symbol.add(file_input[self.riga][(self.end + 1)])

        for symb in close_symbol:
            if not symb.isdigit() and symb != ".":
                return False
        return True
        """

def add_num(riga: list, start_index: int, num_row:int) -> Numero:
    "Construct the parameters to to creare the Numero to add to list of Numero in input"

    index = 0
    for ch in riga[start_index:]:
        if not ch.isdigit():
            break
        index += 1
    num_string = riga[start_index: (start_index + index)]
    num = Numero(num_string, start_index, (start_index + index), num_row)
    return num


def check_if_can_add(row: list, index: int) -> bool:
    "Inspect the row to find if the elwment in cycle can be added"
    if index == 0 and row[0].isdigit():
        return True

    if row[index].isdigit() and not row[(index - 1)].isdigit():
        return True

    return False


def find_numbers(input_matrix: list[list]) -> list:
    "Inspect the input file to find the numbers corresponding to requisites"

    res: list = list()
    for row_num, row in enumerate(input_matrix):
        for num_column, el in enumerate(row):
            #if num_column != 0 and el.isdigit() and not input_matrix[row_num][(num_column - 1)].isdigit():
            if check_if_can_add(row, num_column):
                found = add_num(row, num_column, row_num)
                res.append(found)
    return res


def sum_aoc(list_numbers: list, matrix:list[list]) -> int:
    """Returns the sum of the numbers in the engine"""

    #result = sum([int(num.numero)  for num in list_numbers if num.has_symbol_near(matrix)])
    result = list(filter(lambda x: x.has_symbol_near(matrix), list_numbers))
    result = sum([int(x.numero) for x in result])
    
    return result

def has_symbol_near(num: Numero, matrix: list[list]) -> bool:

    riga = num.riga
    start_index = num.start
    end_index = num.end

    for row_num, row in enumerate(matrix[(num.riga - 1): (num.riga + 1)]):
        for col_num, el in enumerate(row[(num.start - 1): (num.end + 2)]):
            if not el.isdigit() and el != ".":
                return False
    return True


if __name__ == '__main__':
    """
    test_num = Numero("123", 3, 66, 999)
    print(test_num)
    """

    #"input003_test.txt" expected value -> 925
    with open("input003_test04.txt") as f:
        input_text = f.readlines()

    
    ok_num = find_numbers(input_text)
    #print("len ok_num:  " + str(len(ok_num)))  
    
    

    print(ok_num[0])
    print(ok_num[1].numero)
    #print(ok_num[25])
    #print(ok_num[225])
    #print(ok_num[359])          
    
    """
    for x in ok_num[:40]:
        print(x.numero, end= "    ")
    """
    print(ok_num)
    ok_res = sum_aoc(ok_num, input_text)

    #test_res = list(filter(
    print(ok_res)
    
    num_check01 = Numero("335", 12, 14, 4)
    #assert num_check01.has_symbol_near(input_text) == True, "is not true, strange"
    #assert num_check01.has_symbol_near(input_text) == False "Not False, expected"

    num_check02 = Numero("796", 135, 137, 14)
    #assert num_check02.has_symbol_near(input_text) == True, "is not true, strange"
    #assert num_check02.has_symbol_near(input_text) == False "Not False, expected"

    

    """
    with open("input003.txt") as f:
        input_text = f.readlines()
    
    test_method = Numero("489", 5, 7, 0)

    test_met = test_method.has_symbol_near(input_text)

    assert test_method.has_symbol_near(input_text) == False
    """
