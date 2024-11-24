#Zadanie 1 (Mnożenie macierzy)

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Incopeteble size of Matrixes")

    res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):  # Iteracja po wierszach A
        for j in range(len(B[0])):  # Iteracja po kolumnach B
            for k in range(len(B)):  # Iteracja po elementach wiersza/kolumny
                res[i][j] += A[i][k] * B[k][j]

    return res

A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]

result = matrix_multiply(A, B)

# Wyświetlenie
for row in result:
    print(row)