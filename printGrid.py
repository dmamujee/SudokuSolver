NULL_OUTPUT = "."


def printable_grid(grid):
    """
    :type grid: 2-D array of numbers
    """
    output = ""
    for row in grid:
        row_output = ""
        for item in row:
            if item is None:
                item = NULL_OUTPUT
            if row_output == "":
                row_output = str(item)
            else:
                row_output += " " + str(item)
        output += row_output + "\n"
    return output
