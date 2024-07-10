# pylint: disable=missing-docstring


def valid_rows(grid):
    for k in range(1,10):
        for i in range(9):
            if (k in grid[i]) is False:
                return False
    return True

def valid_columns(grid):
    for k in range(1,10):
        for j in range(9):
            column = []
            for i in range(9):
                column.append(grid[i][j])
            if (k in column) is False:
                return False
    return True

def valid_boxes(grid):
    for k in range(1,10):
        start_row = 0
        end_row = 3
        while end_row <= 9:
            start_column = 0
            end_column = 3
            while end_column <= 9:
                square = []
                for i in range(start_row,end_row):
                    for j in range(start_column,end_column):
                        square.append(grid[i][j])
                if (k in square) is False:
                    return False
                start_column += 3
                end_column += 3
            start_row += 3
            end_row += 3
    return True

def sudoku_validator(grid):
    return valid_rows(grid) and valid_columns(grid) and valid_boxes(grid)
