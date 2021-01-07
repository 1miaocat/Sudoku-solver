# This is the sudoku puzzle
board = [
    [0, 2, 0, 0, 3, 0, 0, 4, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 8, 0, 6, 0, 0, 0],
    [8, 0, 0, 0, 1, 0, 0, 0, 6],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 6, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 3, 0, 0, 4, 0, 0, 2, 0]
]


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


print_board(board)
