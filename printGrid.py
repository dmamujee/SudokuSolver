NULL_OUTPUT = "."


def print_grid(grid):
    """
    :type grid: 2-D array of numbers
    """
    for row in grid:
        output = ""
        for item in row:
            if item is None:
                item = NULL_OUTPUT
            if output == "":
                output = str(item)
            else:
                output += " " + str(item)
        print(output)
