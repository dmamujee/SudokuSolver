from printGrid import printable_grid


# From http://www.websudoku.com/?level=1&set_id=2146138832

def is_grid_valid(grid):
    for temp_row in grid:
        if is_row_valid(temp_row) is False:
            return False

    for row in range(3):
        row = row*3
        for column in range(3):
            column = column*3
            temp_row = []
            for i in range(3):
                for j in range(3):
                    temp_row.append(grid[row + i][column + j])
            if is_row_valid(temp_row) is False:
                return False

    return True


def is_row_valid(row):
    new_row = list(filter(lambda a: a is not None, row))
    if len(new_row) > len(set(new_row)):
        return False
    else:
        return True
