import random


# noinspection PyUnusedLocal
def heuristic_none(queens, n):
    """
    No heuristic, use the original search order.
    This returns a constant number for every possible placement of queens.
    :param queens: Ignored.
    :param n: Ignored.

    :return: A constant number.
    """
    return 0


# noinspection PyUnusedLocal
def heuristic_random(queens, n):
    """
    No heuristic, just shuffle the possible moves in a random order.
    :param queens: List of pairs of coordinates (x, y).
    :param queens: Ignored.
    :param n: Ignored.
    """
    random.seed(0)
    return random.uniform(0, 1)


def heuristic_free_cells(queens, n):
    """
    Compute the number of cells not attacked by any queen.
    :param queens: List of pairs of coordinates (x, y).
    :param n: Problem dimension.
    :return: Number of not-attacked cells.
    """

    # put the queens on the chessboard
    chessboard = compute_chessboard(queens, n)

    # mark cells attacked
    for (x, y) in queens:

        # set row
        for i in range(n):
            chessboard[i][y] = 0

        # set column
        for j in range(n):
            chessboard[x][j] = 0

        # diagonal, top left sector
        for k in range(min(x, n - y)):
            chessboard[x - k][y + k] = 0

        # diagonal, bottom right sector
        for k in range(min(n - x, y)):
            chessboard[x + k][y - k] = 0

        # diagonal, top right
        for k in range(min(n - x, n - y)):
            chessboard[x + k][y + k] = 0

        # diagonal, bottom left
        for k in range(min(n + x, n + y)):
            chessboard[x - k][y - k] = 0

    return sum(map(sum, chessboard))


def heuristic_attacked_cells(queens, n):
    """
    Compute the number of cells attacked by at least one queen.
    :param queens: List of pairs of coordinates (x, y).
    :param n: Problem dimension.
    :return: Number of attacked cells, including the cells occupied by the queens.
    """
    return n * n - heuristic_free_cells(queens, n)


def compute_chessboard(queens, n):
    """
    Put the queens on chessboard.
    :param queens: Queens list.
    :param n: Problem dimension.
    :return: Chessboard matrix.
    """

    # initialize an empty chessboard
    chessboard = [[1 for _ in range(n)] for _ in range(n)]

    # check each cell
    for (x, y) in queens:
        # set all cells occupied by a queen
        chessboard[x][y] = 0

    # return the computed chessboard
    return chessboard
