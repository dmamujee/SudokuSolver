from printGrid import printable_grid


# From http://www.websudoku.com/?level=1&set_id=2146138832

def solve(grid):
    if is_solved(grid):
        return grid
    for row in range(0, 9):
        for item in range(0, 9):
            if grid[row][item] is not None:
                continue
            for i in range(1, 10):
                grid[row][item] = i
                if is_grid_valid(grid) is True:
                    result = solve(grid)
                    if result is False:
                        continue
                    else:
                        return grid
                else:
                    continue
            return False


def is_grid_valid(grid):
    for temp_row in grid:
        if is_row_valid(temp_row) is False:
            return False

    for row in range(0, 6, 3):
        for column in range(0, 6, 3):
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


def is_solved(grid):
    for row in grid:
        for cell in row:
            if cell is None:
                return False
    return True


grid = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]
        ]
output = solve(grid)
print(output)
