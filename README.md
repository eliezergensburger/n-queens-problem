# n-queens problem - heuristics comparison
Comparison between some simple heuristics to solve the n-queens problem.
This repository contains a very simple Python implementation of a deep-first search algorithm with heuristics
to solve the [n-queens problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle).


## Heuristics
4 heuristics were implemented and compared.

### No Heuristic
The heuristic function always return the same constant value.

### Random Heuristic
The heuristic function always return a random value.
This makes the search randomized.

### Free Cells Heuristic
The heuristic function computes the number of free cells (not occupied or attacked by any queen).
The algorithm explore first the placement that leave more free cells on the chessboard.

### Attacked Cells Heuristic
The heuristic function computes the number of attacked cells (occupied or attacked by at least one queen).
The algorithm explore first the placement that makes more cells attacked.
This heuristic forces the algorithm to explore the search space in the opposite order of the Free Cells Heuristic.


## Results
The heuristics are compared based on the number of recursive calls needed by the algorithm 
to find a solution and the number of calls to the heuristic function.

### Number of recursive calls
n | Constant | Random | Free_Cells | Attacked_Cells
-|-|-|-|-
3 | 6 | 6 | 6 | 6
4 | 9 | 9 | 5 | 9
5 | 6 | 6 | 6 | 6
6 | 32 | 32 | 20 | 34
7 | 10 | 10 | 10 | 14
8 | 114 | 114 | 55 | 69
9 | 42 | 42 | 54 | 80
10 | 103 | 103 | 112 | 114
11 | 53 | 53 | 32 | 279
12 | 262 | 262 | 767 | 511
13 | 112 | 112 | 24 | 239
14 | 1900 | 1900 | 388 | 1829
15 | 1360 | 1360 | 1131 | 1378

```bash
# command to generate the table
./main.py | sed 's/|[0-9]*//g' | sed 's/, / | /g' | sed '1 a -|-|-|-|-'
```

### Number of calls to the heuristic function
n | Constant | Random | Free_Cells | Attacked_Cells
-|-|-|-|-
3 | 18 | 18 | 18 | 18
4 | 32 | 32 | 16 | 32
5 | 25 | 25 | 25 | 25
6 | 186 | 186 | 114 | 198
7 | 63 | 63 | 63 | 91
8 | 904 | 904 | 432 | 544
9 | 369 | 369 | 477 | 711
10 | 1020 | 1020 | 1110 | 1130
11 | 572 | 572 | 341 | 3058
12 | 3132 | 3132 | 9192 | 6120
13 | 1443 | 1443 | 299 | 3094
14 | 26586 | 26586 | 5418 | 25592
15 | 20385 | 20385 | 16950 | 20655

```bash
# command to generate the table
./main.py | sed 's/[0-9]*|//g' | sed 's/, / | /g' | sed '1 a -|-|-|-|-'
```
