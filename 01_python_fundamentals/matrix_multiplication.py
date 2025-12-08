"""
Problem
-------
Multiply two matrices M1 (A x B) and M2 (B x C) and produce M3 (A x C).

Concepts Practiced
------------------
- Nested loops
- Working with 2D lists
- Fundamental algorithm often asked in interviews
"""


def matmul(M1: list[list[int]], M2: list[list[int]]) -> list[list[int]]:
    rows_M1 = len(M1)
    cols_M1 = len(M1[0])
    rows_M2 = len(M2)
    cols_M2 = len(M2[0])

    if cols_M1 != rows_M2:
        raise ValueError("Incompatible dimensions for matrix multiplication")

    # Initialise result with zeros
    M3 = [[0 for _ in range(cols_M2)] for _ in range(rows_M1)]

    for i in range(rows_M1):
        for j in range(cols_M2):
            for k in range(cols_M1):
                M3[i][j] += M1[i][k] * M2[k][j]
    return M3


if __name__ == "__main__":
    M1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    M2 = [
        [10, 20],
        [30, 40],
        [50, 60],
        [70, 80],
    ]
    for row in matmul(M1, M2):
        print(row)

