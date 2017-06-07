import operator


class Proxy:
    """
    Proxy for a heuristic function for the QueensProblem.
    Keep track of the number of calls to the underlying heuristic function.
    """

    def __init__(self, heuristic):
        """
        Create a new Proxy.
        :param heuristic: Heuristic to proxy.
        """
        self._counter = 0
        self._heuristic = heuristic

    def heuristic(self, queens, n):
        """
        Compute the heuristic.
        :param queens: List of queens.
        :param n: Dimension of the problem.
        :return: Cost.
        """
        self._counter += 1
        return self._heuristic(queens, n)

    def count(self):
        """
        Get the count of calls to the heuristic.
        :return: Number of calls.
        """
        return self._counter


class QueensProblem:
    """
    Solve the problem of the n queens on a chessboard.
    """

    def __init__(self, heuristic, n=8):
        self._heuristic = heuristic
        self._n = n
        self._recursive_calls = 0

    def get_recursive_calls_number(self):
        """
        Get the number of recursive calls done to solve the problem.
        :return: Number of recursive calls.
        """
        return self._recursive_calls

    def is_legal_placement(self, queens):
        """
        Check if the queens in the list attack each other on the chessboard.
        :param queens: List of pairs of coordinates (x, y).
        :return: True if the queens does not attack each other.
        """
        return self._is_legal_placement(queens[:])

    def _is_legal_placement(self, queens):
        """
        Check if the queens in the list attack each other on the chessboard.
        NB: this procedure will destroy the list of queens.
        :param queens: List of pairs of coordinates (x, y).
        :return: True if the queens does not attack each other.
        """

        # base case, no queen to place is left... this is a valid solution
        if len(queens) == 0:
            return True

        # remove the first queen
        current = queens.pop()

        # check the current queen against each other
        checks = map(lambda q: self.attack(current, q), queens)

        # if the new queen placed attacks one of the other, discard the placement
        if any(checks):
            return False

        # if the placement is legal til now, try to add the next queens
        else:
            return self._is_legal_placement(queens)

    def solve(self):
        """
        Solve the queen problem using a deep-first search with heuristic and backtrack.
        :return: Pair (solved, placement).
        """
        self._recursive_calls = 0
        return self._solve([])

    def _solve(self, queens):
        """
        Solve the queen problem using a deep-first search with heuristic and backtrack.
        :param queens: List of queens successfully placed until now.
        :return: Pair (solved, placement).
        """

        # track the number of recursive calls so far
        self._recursive_calls += 1

        # check how many queens are already placed
        i = len(queens)

        # base case!
        if i == self._n:
            return True, queens

        # select a queen for line i
        possible = list(map(lambda j: (i, j), range(self._n)))

        # compute the combinations
        positions = list(map(lambda pos: [pos] + queens, possible))

        # compute the scores
        scores = list(map(lambda pos: self._heuristic(pos, self._n), positions))
        possible_next_moves = list(zip(scores, positions))
        possible_next_moves.sort(reverse=True)

        # backtrack
        for (_, q) in possible_next_moves:
            if self.is_legal_placement(q):
                result, placement = self._solve(q)
                if result:
                    return result, placement

        # if here, no solution was found for the problem
        return False, None

    @staticmethod
    def attack(q1, q2):
        """
        Check if 2 queens on the chessboard attack each other.
        :param q1: First queen.
        :param q2: Second queen.
        :return: True if the 2 queens attack each other.
        """
        x1, y1 = q1
        x2, y2 = q2
        # check, in order, columns, rows and diagonals
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

    @staticmethod
    def argmin(l):
        """
        Compute the minimum element of a list.
        :param l: List of elements.
        :return: Minimum element.
        """
        return min(enumerate(l), key=operator.itemgetter(1))
