def create_square_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        for j in range(n):
            matrix[j][i] = num
            num += 1

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Въведете размер на матрицата
n = int(input("Въведете размер на матрицата (n x n): "))

if n < 1:
    print("Невалиден размер на матрицата.")
else:
    square_matrix = create_square_matrix(n)
    print_matrix(square_matrix)


# * # Създаваме празна матрица с размер n x n, където всички стойности са 0.
def create_square_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):  # * # Запълваме матрицата с числата 1, 2, 3,... ( цикъл I определя колоните )
        if i % 2 == 0:
            for j in range(n):
                matrix[j][i] = num
                num += 1
        else:
            # * Запълваме матрицата с числата 5, 6, 7, ...( цикъл J определя редовете )
            for j in range(n - 1, -1, -1):
                matrix[j][i] = num
                num += 1

    return matrix


# ~ Извеждаме матрицата на конзолата, форматирана като таблица.
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# ~ Въведете размер на матрицата
n = int(input("Въведете размер на матрицата (n x n): "))

if n < 1:
    print("Невалиден размер на матрицата.")
else:
    square_matrix = create_square_matrix(n)
    print_matrix(square_matrix)
