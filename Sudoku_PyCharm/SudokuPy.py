# naieve algorithm Sudoko
# back tracking

# 9x9 81


import numpy as np
import random

# import your grid here
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 0, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(np.matrix(grid))


def possible(row, column, number):
    global grid  # going to look at grid oustide of the function
    # is the nubmer apparing in the row
    for i in range(0, 9):
        if grid[row][i] == number:  # checking rows horizontally. If a number appears we give FALSE
            return False
    # is the number appearing in the column
    for i in range(0, 9):
        if grid[i][column] == number:  # we're checking the column verically. If it appears we give FALSE
            return False
    # is the number appearing in a given spot
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True


# backtracking
def solve():
    global grid  # allows us mod the grid outside of the function
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print(np.matrix(grid))
    input('more possible options')


solve()
print()