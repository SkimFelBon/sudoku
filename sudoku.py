import copy
from helpers import filled, nicelyRow, nicelyColumn
"""
puzzle =[[5,0,7],
         [6,0,1],
         [0,9,8]]
"""
quadrant = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
            [3, 4, 5, 12, 13, 14, 21, 22, 23],
            [6, 7, 8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]]
"""
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
"""
puzzle = [[0,8,0,0,0,0,0,9,0],
          [0,0,7,5,0,2,8,0,0],
          [6,0,0,8,0,7,0,0,5],
          [3,7,0,0,8,0,0,5,1],
          [2,0,0,0,0,0,0,0,8],
          [9,5,0,0,4,0,0,3,2],
          [8,0,0,1,0,4,0,0,9],
          [0,0,1,9,0,3,6,0,0],
          [0,4,0,0,0,0,0,2,0]]


def findQuadrant(i,j):
    """ This function finds(detects) to which quadrant our zero belongs """
    for h in range(len(quadrant)):
        for k in range(len(quadrant[h])):
            index_h = quadrant[h][k] // 9
            index_k = quadrant[h][k] % 9
            if (i, j) == (index_h, index_k):
                return quadrant[h]

def nicelyQuadrant(pyzzle, n, i, j):
    """ This function check's if we can use n in this quadrant """
    box = findQuadrant(i, j)
    for v in box:
        index_i = v // 9
        index_j = v % 9
        if pyzzle[index_i][index_j] == n:
            return False
    return True

def nicelyInPuzzle(pyzzle, n, i, j):
    if nicelyQuadrant(pyzzle, n, i, j) == False:
        return False
    if nicelyRow(pyzzle, n, i, j) == False:
        return False
    if nicelyColumn(pyzzle, n, j) == False:
        return False
    return True

def filltable(table):
    if filled(table) is True:
        return table
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != 0:
                continue
            ## for every zero in table create new table if it fits puzzle
            for n in range(1,10):
                # create new list with new item n
                if nicelyInPuzzle(table, n, i, j) == True:
                    newTable = copy.deepcopy(table)
                    newTable[i][j] = n
                    return filltable(newTable)
                else:
                    continue
    return None

result = filltable(puzzle)
if type(result) is list:
    for j in range(len(result)):
        print(result[j])
else:
    print("Failed to find solution")

""" Print Result
print()
for j in range(len(newTable)):
    print(newTable[j])
print()
"""
