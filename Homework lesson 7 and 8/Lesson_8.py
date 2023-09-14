
# $ Homework Lesson 8

#! Задача №1:

# . Да се преработи следната задача, така че да използва речник. Напишете програма, която преобразува дадено число в интервала [0..999] в текст, съответстващ на българското произношение. Примери: -0 -> “Нула” -273 -> ”Двеста седемдесет и три” -400 -> ”Четиристотин” -501 -> “Петстотин и едно” -711 -> “Седемстотин и единадесет”

import random


def number_to_words(n):
    # ~ Речник с числата и техните текстови представяния
    num_to_words = {
        0: "Нула",
        1: "Едно",
        2: "Две",
        3: "Три",
        4: "Четири",
        5: "Пет",
        6: "Шест",
        7: "Седем",
        8: "Осем",
        9: "Девет",
        10: "Десет",
        11: "Единадесет",
        12: "Дванадесет",
        13: "Тринадесет",
        14: "Четиринадесет",
        15: "Петнадесет",
        16: "Шестнадесет",
        17: "Седемнадесет",
        18: "Осемнадесет",
        19: "Деветнадесет",
        20: "Двадесет",
        30: "Тридесет",
        40: "Четиридесет",
        50: "Петдесет",
        60: "Шестдесет",
        70: "Седемдесет",
        80: "Осемдесет",
        90: "Деветдесет"
    }

    if n in num_to_words:
        return num_to_words[n]

    if 20 < n <= 99:
        tens = n // 10 * 10
        ones = n % 10
        return f"{num_to_words[tens]} и {num_to_words[ones]}"

    if 100 <= n <= 999:
        hundreds = n // 100
        remainder = n % 100
        if remainder == 0:
            return f"{num_to_words[hundreds]}стотин"
        else:
            return f"{num_to_words[hundreds]}стотин {number_to_words(remainder)}"

    return "Числото не е в интервала [0..999]"


number = int(input("Въведете число от 0 до 999: "))

if 0 <= number <= 999:
    words = number_to_words(number)
    print(words)
else:
    print("Числото не е в интервала [0..999]")

#! Задача №2:

# ~ Речник с множители за ниво на активност
activity_levels = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9,
    6: 2.0
}

# ~ Функция за изчисление на BMR спрямо пола


def calculate_bmr(age, gender, height, weight):
    if gender == 'm':
        bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif gender == 'f':
        bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        bmr = None
    return bmr


# ~ Въвеждане на данните от потребителя
age = int(input("Въведете възраст: "))
gender = input("Въведете пол ('m' или 'f'): ")
height = float(input("Въведете височина в см: "))
weight = float(input("Въведете тегло в кг: "))
activity_level = int(input("Въведете ниво на активност (1-6): "))

# ~ Изчисляване на BMR
bmr = calculate_bmr(age, gender, height, weight)

if bmr is not None:
    # ~ Изчисляване на калорийния прием за различни цели
    calorie_intake_maintenance = bmr * activity_levels[activity_level]
    calorie_intake_lose_half_kg = calorie_intake_maintenance - 500
    calorie_intake_lose_1_kg = calorie_intake_maintenance - 1000
    calorie_intake_gain_half_kg = calorie_intake_maintenance + 500
    calorie_intake_gain_1_kg = calorie_intake_maintenance + 1000

    # ~ Извеждане на резултатите
    print(
        f"Имате нужда от {calorie_intake_maintenance} Калории на ден за да поддържате теглото си")
    print(
        f"Имате нужда от {calorie_intake_lose_half_kg} Калории на ден за да сваляте по 0.5 кг на седмица")
    print(
        f"Имате нужда от {calorie_intake_lose_1_kg} Калории на ден за да сваляте по 1 кг на седмица")
    print(
        f"Имате нужда от {calorie_intake_gain_half_kg} Калории на ден за да качвате по 0.5 кг на седмица")
    print(
        f"Имате нужда от {calorie_intake_gain_1_kg} Калории на ден за да качвате по 1 кг на седмица")
else:
    print("Грешка: Невалиден пол. Въведете 'm' за мъж или 'f' за жена.")

#! Задача №3:

# Дефиниране на менюто като речник
menu = {
    "sandwich": 10,
    "tea": 7,
    "soup": 5,
    "salad": 8,
    "pizza": 12
}

# Инициализация на променливата за общата цена
total_price = 0

# Цикъл за поръчване
while True:
    order = input("Order: ")

    # Проверка дали поръчаното ястие се намира в менюто
    if order in menu:
        price = menu[order]
        total_price += price
        print(f"{order} costs {price}, total is {total_price}")
    elif order == "":
        # Потребителят въведе празен стринг, край на поръчката
        print(f"Your total is {total_price}")
        break
    else:
        # Потребителят въведе несъществуващо ястие
        print("Sorry, we are fresh out of that today.")
        print(f"Your total is {total_price}")
        break

#! Задача №4:

# Инициализация на речник за валежите
rainfall_data = {}

while True:
    city = input("Въведете име на град (Enter за изход): ")

    if not city:
        # Ако потребителят натисне Enter (празен ред), приключваме
        break

    try:
        rainfall = float(input(f"Въведете количество дъжд за {city}: "))

        if city in rainfall_data:
            rainfall_data[city] += rainfall
        else:
            rainfall_data[city] = rainfall
    except ValueError:
        print("Невалидно количество дъжд. Моля, въведете число.")

# Извеждане на отчета
for city, total_rainfall in rainfall_data.items():
    print(f"{city}: {total_rainfall}")

#! Задача №5:


def find_difference(dict1, dict2):
    result = {}

    for key in dict1.keys():
        if key in dict2 and dict1[key] != dict2[key]:
            result[key] = [dict1[key], dict2[key]]
        elif key not in dict2:
            result[key] = [dict1[key], None]

    for key in dict2.keys():
        if key not in dict1:
            result[key] = [None, dict2[key]]

    return result


# Примери:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'd': 3}
d3 = {'a': 1, 'b': 2, 'c': 4}
d4 = {'a': 1, 'b': 2, 'c': 4}
d5 = {'a': 1, 'b': 2, 'd': 4}

result1 = find_difference(d1, d2)
result2 = find_difference(d1, d3)
result3 = find_difference(d4, d5)

print(result1)  # {'c': [3, None], 'd': [None, 3]}
print(result2)  # {'c': [3, 4]}
print(result3)  # {'c': [4, None], 'd': [None, 4]}

#! Задача №6:

# Създаване на тълковен речник (френско-английски)
dictionary = {
    'cat': ['chat'],
    'dog': ['chien'],
    'house': ['maison'],
    'car': ['voiture'],
    'flower': ['fleur'],
    'tree': ['arbre'],
    'book': ['livre'],
    'apple': ['pomme'],
    'sun': ['soleil']
}


def search_word(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return []


while True:
    search_input = input("Въведете английска дума (или 'exit' за изход): ")

    if search_input == 'exit':
        break

    translations = search_word(search_input, dictionary)

    if translations:
        print(f"Френски еквиваленти: {', '.join(translations)}")
    else:
        print("Няма съответствие в речника.")

#! Задача №7:


# Инициализираме речник за очакваните вероятности
expected_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Инициализираме речник за броя на паднали комбинации
dice_rolls = {i: 0 for i in range(2, 13)}

# Симулираме 1000 завъртания на два зара
for _ in range(1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    dice_rolls[total] += 1

# Принтираме резултата
print("Резултати след 1000 завъртания:")
for total, count in dice_rolls.items():
    expected_probability = expected_probabilities[total]
    print(
        f"Сума {total}: Очаквана вероятност {expected_probability:.3f}, Брой падания {count}")

#! Задача №8:

# Въвеждане на низ от потребителя
input_string = input("Въведете низ: ")

# Инициализиране на речник за броя на символите
unique_chars = {}

# Прохождане през всеки символ в низа
for char in input_string:
    # Ако символът не е в речника, добавяме го като ключ със стойност 1
    if char not in unique_chars:
        unique_chars[char] = 1
    else:
        # Ако символът вече съществува, увеличаваме броя на срещанията му
        unique_chars[char] += 1

# Броят на уникалните символи е равен на броя на ключовете в речника
count_unique = len(unique_chars)

# Принтираме резултата
print(f"Брой на уникалните символи в низа: {count_unique}")

#! Задача №9:

# Въвеждане на двата низа от потребителя
str1 = input("Въведете първия низ: ").lower()
str2 = input("Въведете втория низ: ").lower()

# Създаване на речници за броя на срещанията на символите в низовете
char_count1 = {}
char_count2 = {}

# Попълване на речника за първия низ
for char in str1:
    if char.isalpha():  # Игнорираме интервали и знаци
        char_count1[char] = char_count1.get(char, 0) + 1

# Попълване на речника за втория низ
for char in str2:
    if char.isalpha():
        char_count2[char] = char_count2.get(char, 0) + 1

# Сравнение на речниците
if char_count1 == char_count2:
    print("Двата низа са анаграми.")
else:
    print("Двата низа не са анаграми.")

#! Задача №10:

# Създаване на речник с буквите и техните точки
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Въвеждане на думата от потребителя и преобразуване на всички букви в главни
word = input("Въведете дума: ").upper()

# Изчисляване на резултата за думата
score = 0
for letter in word:
    if letter in letter_scores:
        score += letter_scores[letter]

# Извеждане на резултата
print(f"Резултат за думата '{word}': {score} точки")
