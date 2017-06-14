from printGrid import print_grid

# From http://www.websudoku.com/?level=1&set_id=2146138832
fake_grid = [
    [None, None, 7, None, None, None, None, "6", None],
    [2, 3, None, None, 5, 6, None, 9, None],
    [9, None, 1, 8, None, None, 3, None, 5],
    [1, 4, None, None, None, None, None, None, None],
    [8, 9, None, 1, 2, 4, None, 5, 6],
    [None, None, None, None, None, None, None, 8, 1],
    [3, None, 8, None, None, 5, 6, None, 9],
    [None, 5, None, 9, 1, None, None, 2, 7],
    [None, 1, None, None, None, None, 5, None, None]
]

print_grid(fake_grid)
