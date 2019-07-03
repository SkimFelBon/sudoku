# helpers.py

quadrant = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
            [3, 4, 5, 12, 13, 14, 21, 22, 23],
            [6, 7, 8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]]

## DONE: write function to check if table filled
def filled(pyzzle):
    for i in range(len(pyzzle)):
        for j in range(len(pyzzle)):
            if pyzzle[i][j] == 0:
                return False
    return True

def findQuadrant(i,j, quadrant):
    """ This function finds(detects) to which quadrant our zero belongs """
    for h in range(len(quadrant)):
        for k in range(len(quadrant[h])):
            index_h = quadrant[h][k] // 9
            index_k = quadrant[h][k] % 9
            if (i, j) == (index_h, index_k):
                return quadrant[h]

def nicelyQuadrant(pyzzle, n, i, j):
    """ This function check's if we can use n in this quadrant """
    box = findQuadrant(i, j, quadrant)
    for v in box:
        index_i = v // 9
        index_j = v % 9
        if pyzzle[index_i][index_j] == n:
            return False
    return True

def nicelyColumn(pyzzle, n, j):
    for k in range(len(pyzzle)):
        if pyzzle[k][j] == n:
            return False
    return True

def nicelyRow(pyzzle, n, i, j):
    for j in range(len(pyzzle[i])):
        if pyzzle[i][j] == n:
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
