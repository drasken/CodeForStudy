"""
Trying using DP and iterative approach
//TODO: try in recursive way
"""

#my input
triang = [[75],
          [95, 64],
          [17, 47, 82],
          [18, 35, 87, 10],
          [20, 4, 82, 47, 65],
          [19, 1, 23, 75, 3, 34],
          [88, 2, 77, 73, 7, 63, 67],
          [99, 65, 4, 28, 6, 16, 70, 92],
          [41, 41, 26, 56, 83, 40, 80, 70, 33],
          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
          [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
          [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
          [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
          [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
          [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

#test input
test_tr = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]] # expected --> 23


def max_path_bis(triangle):

    sol = [[0 for n in l] for l in triangle]

    for index, row in enumerate(triangle):
        for index_row, num in enumerate(row):
            if index == 0: #step one
                sol[0][0] = triangle[0][0]
            elif index_row == 0: #edge case left -one possible path
                sol[index][index_row] = num + sol[index - 1][0]
            elif index_row == (len(row) - 1): #edge case rigth -again one path
                sol[index][index_row] = num + sol[index - 1][index_row - 1]
            else:
                sol[index][index_row] = num + max(sol[index - 1][index_row - 1], sol[index - 1][index_row])
    return max(sol[-1])


solution = max_path_bis(triang)
print(solution) #First test = 1074 --> OK! it works 
