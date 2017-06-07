from problem import Proxy, QueensProblem
from heuristics import heuristic_none, heuristic_random, heuristic_attacked_cells, heuristic_free_cells


def main():
    """
    Run a deep-first search algorithm with different heuristics to solve the n-queens problem.
    The program will try different problems dimensions. The output is a table with the results
    of each heuristics for each dimension. The first number represents the number of recursive
    steps that the algorithm performed to get a solution, the second number is the number of
    invocations of the heuristic function during the search.
    """

    # separator to format the output
    separator = ', '

    # list of heuristics to try
    heuristics = [
        ('Constant', heuristic_none),
        ('Random', heuristic_random),
        ('Free_Cells', heuristic_free_cells),
        ('Attacked_Cells', heuristic_attacked_cells)
    ]

    # print header
    print('n%s%s' % (separator, separator.join(list(zip(*heuristics))[0])))

    # try different problem dimensions
    for n in range(3, 16):

        # print the current problem dimension
        print(n, end='')

        # try different heuristics
        for (name, heuristic) in heuristics:
            proxy = Proxy(heuristic)
            queens = QueensProblem(proxy.heuristic, n)
            queens.solve()
            print(separator, end='')
            print(queens.get_recursive_calls_number(), end='')
            print('|', end='')
            print(proxy.count(), end='')

        # terminate the line
        print('')


# entry point
if __name__ == '__main__':
    main()
