# sudoku.py
from helpers import filled, nicelyInPuzzle


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# Should return
"""
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
"""

def filltable(table):
    if filled(table) is True:
        return True
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != 0:
                continue
            ## for every zero in table create new table if it fits puzzle
            for n in range(1,10):
                # create new list with new item n
                if nicelyInPuzzle(table, n, i, j) == True:
                    table[i][j] = n
                    if filltable(table):
                        return True
                    table[i][j] = 0
            return False

result = filltable(puzzle)
if result:
    for j in range(len(puzzle)):
        print(puzzle[j])
else:
    print("Failed to find solution")
