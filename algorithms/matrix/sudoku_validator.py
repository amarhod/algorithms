"""
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

(More info at: http://en.wikipedia.org/wiki/Sudoku)

"""
#import numpy as np


testing = [0]*20;
for i in range(20):
    testing[i] = False

# Using dict/hash-table
from collections import defaultdict
def valid_solution_hashtable(board):
    for i in range(len(board)):
        dict_row = defaultdict(int)
        dict_col = defaultdict(int)
        for j in range(len(board[0])):
            value_row = board[i][j]
            value_col = board[j][i]
            if not value_row or value_col == 0:
                return False
            if value_row in dict_row:
                return False
            else:
                dict_row[value_row] += 1

            if value_col in dict_col:
                return False
            else:
                dict_col[value_col] += 1

    for i in range(3):
        for j in range(3):
            grid_add = 0
            for k in range(3):
                for l in range(3):
                    grid_add += board[i*3+k][j*3+l]
            if grid_add != 45:
                return False
    return True


# Without hash-table/dict
def valid_solution(board):
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False

    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return False

    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]

            if sorted(region) != correct:
                return False

    # if everything correct
    return True


# Using set
def valid_solution_set (board):

    valid = set(range(1, 10))

    for row in board:
        testing[0] = True
        #If 1
        if set(row) != valid:
            testing[2] = True
            return False
        else:
            testing[3] = True;
    if row not in board:
        testing[1] = True
    for col in [[row[i] for row in board] for i in range(9)]:
        testing[4] = True
        #If 2
        if set(col) != valid:
            testing[6] = True
            return False
        else:
            testing[7] = True
    if col not in [[row[i] for row in board] for i in range(9)]:
        testing[5] = True
    for x in range(3):
        testing[8] = True
        for y in range(3):
            testing[10] = True
            #If 3
            if set(sum([row[x*3:(x+1)*3] for row in board[y*3:(y+1)*3]], [])) != valid:
                testing[12] = True
                return False
            else: 
                testing[13] = True
        if y not in range(3):
            testing[11] = True
    if x not in range(3):
        testing[9] = True
    return True

def return_thingy(i):
    return testing[i] 

# bread = np.array([
#                     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                     [3, 4, 5, 2, 8, 6, 1, 7, 9]
#                 ])

breads = [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]

#test = valid_solution_set(breads)
#print(test)

#for x in breads:
#    print(x)

#print(bread[:,2])

#for i in range(9):
    #print(bread[:,i])
