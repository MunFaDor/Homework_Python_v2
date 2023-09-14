
# $ Homework Lesson_7

import random

#! Задача №1:

# . Напишете програма, която чете цели числа въведени от потребителя и ги съхранява в списък. Програма трябва да продължи да чете стойности, докато потребителят не въведе 0. След това тя трябва да покаже всички стойности, въведени от потребителя (с изключение на 0), подредени от най-малката до най-голямата стойност, като на всеки ред се появява по една стойност. Използвайте или метода за сортиране, или функцията за сортиране на списъци.


numbers = []

while True:
    num = int(input("Въведете цяло число: (за да излезете въведете 0)"))
    if num != 0:
        numbers.append(num)
    else:
        print("Успешно затворихте програмата.")
        break

    numbers.sort()

    print("Сортирани числа: ")
    for num in numbers:
        print(num)

#! Задача №2

# . При анализиране на данни, събрани като част от научен експеримент, може да се наложи да се премахнат най-крайните (големите) стойности, преди да се извършват някакви други изчисления. Да се създаде списък от стойностите само с n на брой положителни числа. Трябва да се създаде ново копие на създаденият списък с премахнатите n най-големи елемента и n най-малките елементи. Редът на елементите във върнатия списък не трябва да съвпада с реда на елементите в първоначалния списък. Напишете програма, която  да чете списък от числа въведени от потребителя и да премахва двете най-големи и двете най-малки стойности. Да се принтира новият списък, както и оригиналният. Програма трябва да генерира подходящо съобщение за грешка, ако потребителят въведе по-малко от 4 стойности.

# ~ Четем списък от числа от потребителя
numbers = input(
    "Въведете списък от числа, разделени със запетайки: ").split(",")

# ~ Проверяваме дали има поне 4 числа въведени
if len(numbers) < 4:
    print("Грешка: Въведете поне 4 числа.")
else:
    # ~ Преобразуваме въведените стойности в цели числа
    numbers = [int(num) for num in numbers]

    # ~ Сортираме списъка
    sorted_numbers = sorted(numbers)

    # ~ Премахваме двата най-големи и двата най-малки елемента
    trimmed_numbers = sorted_numbers[2:-2]

    # ~ Извеждаме новият списък и оригиналният списък
    print("Оригинален списък:", numbers)
    print("Нов списък след премахване на двата най-големи и двата най-малки елемента:", trimmed_numbers)

#! Задача №3

# . Да се създаде програма, която чете думи като вход от клавиатурата, докато потребителят не въведе празен ред. След като потребителят въведе празен ред, програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж. Думите трябва да се показват в същия ред, в който са били въведени. Например, ако потребителят въведе:  first second first third second  тогава програмата трябва да принтира само:  first second third

# ~ Създаваме празен списък, в който ще съхраняваме въведените думи
word_list = []

# ~ Вход в безкраен цикъл
while True:
    word = input(
        "Въведете дума (или натиснете Enter, за да приключите въвеждането): ")
    if word == "":
        break  # ~ Излизаме от цикъла при празен вход

    word_list.append(word)  # Добавяме въведената дума към списъка

# ~ Използваме множество, за да премахнем дубликатите
unique_words = set(word_list)

# ~ Извеждаме уникалните думи
print("Уникални думи, въведени от потребителя:")
for word in unique_words:
    print(word)

#! Задача №4

# . Да се създаде програма, която да чете цели числа въведени от потребителя, докато не бъде въведен празен ред. След като всичките числа са прочетени, програмата трябва да показва всички отрицателни числа, последвани от нули, последвани от всички положителни числа. Във всяка група номерата трябва да се показват в същия ред, в който са въведени от потребителя. Например, ако потребителят въведе стойностите 3, 4, 1, 0, -1, 0 и -2, вашата програма трябва да изведе стойностите -4, -1, -2, 0, 0, 3 и 1 . Вашата програма трябва да показва всяка стойност на нов ред.

# ~ Създаваме три празни списъка за отрицателни, нулеви и положителни числа
negative_numbers = []
zeroes = []
positive_numbers = []

# ~ Вход в безкраен цикъл
while True:
    user_input = input(
        "Въведете цяло число (или натиснете Enter, за да приключите въвеждането): ")

    if user_input == "":
        break  # ~ Излизаме от цикъла при празен вход

    number = int(user_input)

    if number < 0:
        negative_numbers.append(number)
    elif number == 0:
        zeroes.append(number)
    else:
        positive_numbers.append(number)

# ~ Извеждаме отрицателните числа, следвани от нули, последвани от положителните числа
for num in negative_numbers + zeroes + positive_numbers:
    print(num)

#! Задача №5

# . За да спечели най-голямата награда в определена лотария, човек трябва да съпостави всичките 6 числа от билета си с 6-те числа между 1 и 49, които са изтеглени от организатора на лотарията. Напишете програма, която генерира произволен избор от 6 числа за лотариен билет. Уверете се, че избраните 6 числа не се повтарят. Покажете числата във възходящ ред.

# ~ Генерираме празен списък за лотарийните числа
lottery_numbers = []

# ~ Генерираме 6 уникални числа в интервала [1, 49] и ги добавяме към списъка
while len(lottery_numbers) < 6:
    number = random.randint(1, 49)
    if number not in lottery_numbers:
        lottery_numbers.append(number)

# ~ Сортираме числата във възходящ ред
lottery_numbers.sort()

# ~ Извеждаме генерираните числа
print("Вашите лотарийни числа са:")
for number in lottery_numbers:
    print(number)

#! Задача №6

# . Да се напише програма, която генерира всички подсписъци на даден списък. Например, списъците на [1, 2, 3] са [], [1], [2], [3], [1, 2], [2, 3], [1, 3] и [1, 2, 3]


def generate_sublists(lst):
    sublists = [[]]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            sublists.append(sublist)
    return sublists


# ~ Въвеждане на списък от потребителя
user_input = input("Въведете списък, разделен със запетаи (например, 1,2,3): ")
user_list = [int(item) for item in user_input.split(',')]

sublists = generate_sublists(user_list)

for sublist in sublists:
    print(sublist)

#! Задача №7

# . Напишете програма, която намира максимална редица от последователни еднакви елементи в списък.  Пример: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}.  ‘2’ * counter


def find_max_sequence(lst):
    max_sequence = []
    current_sequence = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_sequence.append(lst[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence.copy()
            current_sequence = [lst[i]]

    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence

    return max_sequence


# ~ Пример
input_list = [2, 1, 1, 2, 3, 3, 2, 2, 2, 1]
result = find_max_sequence(input_list)
print(result)

#! Задача №8

# . Напишете програма, която намира максималната редица от последователни нарастващи елементи в списък.  Пример: {3, 2, 3, 4, 2, 2, 4} -> {2, 3, 4}.


def find_max_increasing_sequence(lst):
    max_sequence = []
    current_sequence = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            current_sequence.append(lst[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence.copy()
            current_sequence = [lst[i]]

    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence

    return max_sequence


# ~ Пример
input_list = [3, 2, 3, 4, 2, 2, 4]
result = find_max_increasing_sequence(input_list)
print(result)

#! Задача №9

# .Напишете програма, която създава следните квадратни матрици и ги извежда на конзолата във форматиран вид. Размерът на матриците се въвежда от конзолата.

# $ VARIANT A:


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


# ~ Въведете размер на матрицата
n = int(input("Въведете размер на матрицата (n x n): "))

if n < 1:
    print("Невалиден размер на матрицата.")
else:
    square_matrix = create_square_matrix(n)
    print_matrix(square_matrix)

# $ VARIANT B:

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
