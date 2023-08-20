"""
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
"""
#Find the item type that appears in both compartments of each rucksack.
#What is the sum of the priorities of those item types?
#The string is divided in half, each representing a compartments

with open (file='input03A.txt', mode='r') as file:
    input = file.readlines() #read flrom file
    new_input = [] 
    for i in input: #strip the \n char from each string
        new_input.append(i.rstrip('\n'))

    print(new_input)