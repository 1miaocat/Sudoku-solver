# This is the sudoku puzzle
grid = [
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 3, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 1, 8],
    [0, 0, 0, 0, 8, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [0, 4, 0, 0, 0, 0, 3, 0, 0]
]


def find_empty(bo):  # find an empty grid
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # returns the position of the empty space
    return None, None  # return none if there is no empty spaces


def insert_number(bo, row, col, n):  # test and imput a number to the grid
    row_values = bo[row]
    if n in row_values:  # check if there is number n on the row
        return False
    col_values = []
    for i in range(9):  # check if there is number n on the column
        col_values.append(bo[i][col])
    if n in col_values:
        return False

    r0 = (row // 3) * 3  # create row for 3x3 grid
    c0 = (col // 3) * 3  # create column for 3x3 grid

    for i in range(0, 3):
        for j in range(0, 3):
            # accessing all the tiles in 3x3 grid + check
            if bo[r0 + i][c0 + j] == n and (i, j) != (row, col):
                return False
    return True


def solver(bo):  # sudoku solver function
    row, col = find_empty(bo)
    if row is None:  # find returns None
        return True  # there is no blank space, puzzle solved
    else:
        for n in range(1, 10):  # inserting number from 1-9 to the blank space
            if insert_number(bo, row, col, n):
                bo[row][col] = n

                if solver(bo):
                    return True  # recursion

            bo[row][col] = 0  # backtracking
        return False


def print_board(bo):
    for row in range(len(bo)):  # iterating rows
        if row % 3 == 0 and row != 0:
            # print seperator between rows every 3 row
            print("- - - - - - - - - -")
        for column in range(len(bo[0])):  # range(number of digits in a row)
            if column % 3 == 0 and column != 0:
                print('|', end='')

            if column == 8:  # on the last column, print without space at the end
                print(bo[row][column])
            else:
                print(str(bo[row][column]) + ' ', end='')  # print the numbers


print_board(grid)
solver(grid)
print('----------------')
print_board(grid)
