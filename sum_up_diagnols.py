def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    diagonal1 = 0
    diagonal2 = 0

    for i in range(len(matrix)):
        diagonal1 = diagonal1 + matrix[i][i]
        diagonal2 = diagonal2 + matrix[i][-1-i]
    
    return diagonal1 + diagonal2

m1 = [
    [1,   2],
    [30, 40],
]

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]

# *** OR:

    # total = 0

    # for i in range(len(matrix)):
    #     total += matrix[i][i]
    #     total += matrix[i][-1 - i]

    # return total

# *** OR:

   # return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))])
