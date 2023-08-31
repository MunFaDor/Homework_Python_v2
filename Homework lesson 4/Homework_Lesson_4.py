""" SUBCHAP - Задача / DEVIDER - условие на задача / INFO - обяснения за всяко нещо направено във файла"""

# chapter-------------------------------Homework Lesson 4--------------------------------

# subchap Задача №1

# devider Да се напише if-конструкция, която проверява стойността на две целочислени променливи и разменя техните стойности, ако стойността на първата променлива е по-голяма от втората.

# important "MATH" е вграден модул в Python, който предоставя функции и константи за математически операции.

import math
print('Задача №1')

print('\n')

# info Въвеждане на стойности за две променливи от потребителя

num1 = float(input("Въведете първото число: "))
num2 = float(input("Въведете второто число: "))

# info Проверка дали стойността на първата променлива е по-голяма от втората

if num1 > num2:
    print("Първото въведено число е по-голямо от второто. Извършва се размяна на стойостите...")

    # info Размяна на стойностите на променливите чрез временна променлива

    temp = num1
    num1 = num2
    num2 = temp

    # info Извеждане на съобщение след размяната на стойностите

    print("Стойност след размяната:")
    print("Първо число:", num1)
    print("Второ число:", num2)
else:
    print("Първото въведено число не е по-голямо от второто. Няма нужда от размяна.")

print('\n')

print('*'*30)

# subchap Задача №2

# devider Напишете програма, която показва знака (+ или -) от частното на две реални числа, без да го пресмята.
print('\n')
print('Задача №2')
print('\n')

# info Въвеждане на две реални числа от потребителя

numerator = float(input("Въведете числителя: "))
denominator = float(input("Въведете знаменателя: "))

# info Проверка на знака на частното без да го пресмята

if numerator * denominator > 0:
    result_sign = "+"
else:
    result_sign = "-"

# info Извеждане на знака на частното използвайки форматиран стринг

print(
    f"Знакъна на резултата от пресмятането {numerator}/{denominator} е: {result_sign}")

print('\n')

print('*'*30)

# subchap Задача №3

# devider Напишете програма, която намира най-голямото по стойност число, измежду три дадени числа.

print('\n')
print('Задача №3')
print('\n')

# info Въвеждане на три числа от потребителя

num1 = float(input("Въведете първото число: "))
num2 = float(input("Въведете второто число: "))
num3 = float(input("Въведете третото число: "))

# Info Проверка на най-голямото число

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

# Info (Допълнително проучване) Проверка за еднакви числа

if num1 == num2 and num2 == num3:
    print("Въведохте три еднакви числа")
elif num1 == num2 or num1 == num3 or num2 == num3:
    if num1 == num2:
        print(
            f"Въведохте две еднакви числа и те са: {num1}, {num2}, а най-голямото е: {largest}")
    elif num1 == num3:
        print(
            f"Въведохте две еднакви числа и те са: {num1}, {num3}, а най-голямото е: {largest}")
    elif num2 == num3:
        print(
            f"Въведохте две еднакви числа и те са: {num2}, {num3}, а най-голямото е: {largest}")
else:
    print(f"Най-голямото от въведените числа е: {largest}")

print('\n')

print('*'*30)

# subchap Задача №4

# devider Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името на цифрата на български език.

print('\n')
print('Задача №4')
print('\n')

# info Въвеждане на цифра от потребителя
digit = int(input("Въведете число (0-9): "))

# info Проверка на въведената цифра и извеждане на нейното име на български ползвайки IF/ELIF структура

if digit == 0:
    name = "Нула"
elif digit == 1:
    name = "Едно"
elif digit == 2:
    name = "Две"
elif digit == 3:
    name = "Три"
elif digit == 4:
    name = "Четири"
elif digit == 5:
    name = "Пет"
elif digit == 6:
    name = "Шест"
elif digit == 7:
    name = "Седем"
elif digit == 8:
    name = "Осем"
elif digit == 9:
    name = "Девет"
else:
    name = "Невалидна цифра"

# info Извеждане на името на цифрата на български

if name == "Невалидна цифра":
    print("Въведохте невалидна цифра")
else:
    print(f"Името на цифрата {digit} на български е: {name}")
print('\n')

print('*'*30)

# subchap Задача №5

# devider Напишете програма, която при въвеждане на коефициентите (a, b и c) на квадратно уравнение ax^2+bx+c изчислява и извежда неговите реални корени.

print('\n')
print('Задача №5')
print('\n')


# info Въвеждане на коефициентите на квадратното уравнение

a = float(input("Въведете коефициент А: "))
b = float(input("Въведете коефициент B: "))
c = float(input("Въведете коефициент C: "))

# info Изчисляване на дискриминантата

discriminant = b**2 - 4*a*c

# info Проверка на дискриминантата и изчисляване на корените

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Квадратното уравнение има 2 реални корена:")
    print(f"Корен 1: {root1}")
    print(f"Корен 2: {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Квадратното уравнение има 1 реален корен:")
    print(f"Корен: {root}")
else:
    print("Квадратното уравнение няма реални корени.")

print('\n')

print('*'*30)

# subchap Задача №6

# devider Дадени са няколко цели числа. Напишете програма, която намира онези подмножества от тях, които имат сума 0. Примери:
# devider- Ако са дадени числата {-2, -1, 1}, сумата на -1 и 1 е 0.
# devider- Ако са дадени числата {3, 1, -7}, няма подмножества със сума 0.

print('\n')
print('Задача №6')
print('\n')


# info Списък за съхранение на подмножествата със сума 0
def find_subsets_with_sum_zero(numbers):

    # important Ключовата дума def се използва за дефиниране на функция в Python. Това позволява да създадете блок от код, който може да бъде използван повторно чрез извикване на името на функцията!
    subsets = []

    # info Обхождане на всички възможни подмножества
    for i in range(1, 2**len(numbers)):
        # important Текущо подмножество (всяко множество със сума 0 се добавя към "subset")
        subset = []

        # info Генериране на подмножество чрез маскиране на битовете на индекса i
        for j in range(len(numbers)):
            if (i >> j) & 1:
                subset.append(numbers[j])

        # info Проверка дали сумата на текущото подмножество е 0
        if sum(subset) == 0:
            subsets.append(subset)

    return subsets


# info Въвеждане на числата от потребителя
# important Методът "".split()"" се използва за разделяне на стринга на подстрингове, като използва определен разделител.
numbers = list(map(int, input("Въведете списък с числа: ").split()))

# info Намиране на подмножествата със сума 0
zero_sum_subsets = find_subsets_with_sum_zero(numbers)

# info Извеждане на намерените подмножества
if len(zero_sum_subsets) > 0:
    print("Множества със сбор=0:")
    for subset in zero_sum_subsets:
        print(subset)
else:
    print("Не бяха намерени множества със сбор=0.")

print('\n')

print('*'*30)

# subchap Задача №7

# devider Напишете програма, която прилага бонус точки към дадени точки в интервала [1..9] чрез прилагане на следните правила:
# devider - Ако точките са между 1 и 3, програмата ги умножава по 10.
# devider - Ако точките са между 4 и 6, ги умножава по 100.
# devider - Ако точките са между 7 и 9, ги умножава по 1000.
# devider - Ако точките са 0 или повече от 9, се отпечатва съобщение за грешка.

print('\n')
print('Задача №7')
print('\n')

# info Въвеждане на точките от потребителя
points = int(input("Въведете брой точки: "))

# info Прилагане на бонус точки според правилата
if 1 <= points <= 3:
    bonus = points * 10
elif 4 <= points <= 6:
    bonus = points * 100
elif 7 <= points <= 9:
    bonus = points * 1000
else:
    # info проверка за валиднос ( точките трябва да са между 1 и 9)
    print("Грешка: Невалидни точки!")

# info Извеждане на резултата
if 'bonus' in locals():
    print(f"Бонус точки: {bonus}")

print('\n')

print('*'*30)

# subchap Задача №8

# devider Напишете програма, която преобразува дадено число в интервала [0..999] в текст, съответстващ на българското произношение.
# Примери:
# devider - 0 -> “Нула”
# devider - 273 -> ”Двеста седемдесет и три”
# devider - 400 -> ”Четиристотин”
# devider - 501 -> “Петстотин и едно”
# devider -711 -> “Седемстотин и единадесет”

print('\n')
print('Задача №8')
print('\n')


# important Списъци с текстовите представяния на числата от 0 до 9, 10 до 19, десетици и стотици
def convert_to_text(number):
    ones = ["", "едно", "две", "три", "четири",
            "пет", "шест", "седем", "осем", "девет"]
    teens = ["", "единадесет", "дванадесет", "тринадесет", "четиринадесет",
             "петнадесет", "шестнадесет", "седемнадесет", "осемнадесет", "деветнадесет"]
    tens = ["", "десет", "двадесет", "тридесет", "четиридесет",
            "петдесет", "шестдесет", "седемдесет", "осемдесет", "деветдесет"]
    hundreds = ["", "сто", "двеста", "триста", "четиристотин", "петстотин",
                "шестстотин", "седемстотин", "осемстотин", "деветстотин"]

    if 0 <= number <= 9:
        # info Връща текстовото представяне на едноцифрените числа
        return ones[number]
    elif 10 <= number <= 19:
        # info Връща текстовото представяне на числа от 10 до 19
        return teens[number - 10]
    elif 20 <= number <= 99:
        return tens[number // 10] + (" и " + ones[number % 10] if number % 10 != 0 else "")
        # info Връща текстовото представяне на десетици, с добавка на единици (ако са различни от 0)
    elif 100 <= number <= 999:
        if number % 100 == 0:
            # info Връща текстовото представяне на стотици
            return hundreds[number // 100]
        else:
            return hundreds[number // 100] + " и " + convert_to_text(number % 100)
            # info Връща текстовото представяне на стотици, с добавка на текстовото представяне на остатъка (двецифрено число)
    else:
        # info изкарва грешкра когато числото не е в зададения от условието интервал.
        return "Числото не е в интервала [0..999]"


# info Въвеждане на число от потребителя
number = int(input("Въведете число: "))
# info Получаване на текстовото представяне
text_representation = convert_to_text(number)
print(text_representation)  # info Извеждане на текстовото представяне

print('\n')

print('*'*30)

# subchap Задача №9

# devider Да се напише програма, която да превръща температура от целзий в фаренхайт. Формулата е следната: c/5 = f – 32/9, където c е температурата в целзий и f температурата в фаренхайт. Примерен изход: 60°C is 140 in Fahrenheit / 45°F is 7 in Celsius

print('\n')
print('Задача №9')
print('\n')


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


# info Въвеждане на избор от потребителя кой блок от програмата да бъде изпълнен
choice = input(
    "Изберете опция (1 за превръщане от Целзий във Фаренхайт, 2 за обратното): ")

if choice == '1':   # important Преобразуване на температура от Целзий във Фаренхайт БЛОК 1
    celsius = float(input("Въведете температура в Целзий: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit:.1f} in Fahrenheit")
elif choice == '2':  # important Преобразуване на температура от Фаренхайт в Целзий БЛОК 2
    fahrenheit = float(input("Въведете температура в Фаренхайт: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius:.1f} in Celsius")
else:
    print("Невалиден избор")

print('\n')

print('*'*30)

# subchap Задача №10

# devider Напишете програма, която да изчислява възрастта на дадено куче в кучешки години. Забележка: За първите две години, една кучешка година е равна на 10.5 човешки. След това всяка следваща кучешка година се равнява на 4-ри човешки години

print('\n')
print('Задача №10')
print('\n')

# info Въвеждане на възрастта на кучето в човешки години
human_age = float(input("Въведете възрастта на кучето в човешки години: "))

# info Ако възрастта на кучето е по-малка или равна на 2 години
if human_age <= 2:
    dog_age = human_age * 10.5
else:
    # info За възрастта след първите две години
    # important първите две години се умножават по 10.5, след което следващите години по 4
    # explain Според условието, първите две години от живота на кучето една кучешка година се равнява на 10.5 човешки години. След този период (след втората година), всяка следваща кучешка година се пресмята като 4 човешки години.
    dog_age = 21 + (human_age - 2) * 4
print(f"Възрастта на кучето в кучешки години е: {dog_age}")

print('\n')

print('*'*30)

# subchap Задача №11

# devider Да се напише програма, която да намира медианата из между три стойности.

print('\n')
print('Задача №11')
print('\n')

# info Въвеждане на три числа от потребителя
num1 = float(input("Въведете първото число: "))
num2 = float(input("Въведете второто число: "))
num3 = float(input("Въведете третото число: "))

# info Сортиране на числата във възходящ ред
if num1 <= num2 <= num3:
    sorted_nums = [num1, num2, num3]
elif num1 <= num3 <= num2:
    sorted_nums = [num1, num3, num2]
elif num2 <= num1 <= num3:
    sorted_nums = [num2, num1, num3]
elif num2 <= num3 <= num1:
    sorted_nums = [num2, num3, num1]
elif num3 <= num1 <= num2:
    sorted_nums = [num3, num1, num2]
else:
    sorted_nums = [num3, num2, num1]

# info Намиране на медианата
median = sorted_nums[1]

# explain Използваме израза "sorted_nums[1], това означава да вземем стойността на елемента в списъка sorted_nums с индекс 1 който се явява средния елемент тъй като списъците се индексират от 0 до n-1

# info Извеждане на резултата
print(f"Медианата е: {median}")

print('\n')

print('*'*30)

# subchap Задача №12

# devider Напишете програма, която да използва следните променливи, възраст – age, пол (M или F), семейно положение (Y или N) за даден служител. Според следните правила, програмата да определя, къде може да работи конкретният служител.Правила:
# devider - Ако служителката е жена, тя може да работи само в градски райони.
# devider - Ако служителят е мъж на възраст между 20 до 40 години, той може да работи навсякъде
# devider - Ако служителят е мъж на възраст между 40 и 60 години, той ще работи само в градските райони. За всяка друга възраст трябва да се отпечатва грешка

# explain ??? Според условията "MARITAL_STATUS" не променя решението на задачата???

print('\n')
print('Задача №12')
print('\n')

# info  Въвеждане на информация за служителя
age = int(input("Въведете възрастта на служителя: "))
gender = input("Въведете пола на служителя (M или F): ")
marital_status = input("Въведете семейното положение на служителя (Y или N): ")


# info Проверка на условията
if gender == "F":
    print("Служителката може да работи само в градски райони.")
elif gender == "M":
    if 20 <= age <= 40:
        print("Служителят може да работи навсякъде.")
    elif 40 <= age <= 60:
        print("Служителят може да работи само в градски райони.")
    else:
        print("Грешка: Не е възможно да се определи работното място за този служител.")
else:
    print("Грешка: Неизвестен пол.")

print('\n')

print('*'*30)

# subchap Задача №13

# devider Да се напише програма, която при дадено четири цифрено число го обръща отдясно наляво.
# Пример:
# Вход: 1234 Вход: 5982
# Изход: 4321 Изход: 2895

print('\n')
print('Задача №13')
print('\n')

# info Въвеждане на четирицифрено число
number = int(input("Въведете четирицифрено число: "))

# info Разделяне на цифрите и обръщане на числото
digit_1 = number % 10
# explain Тази операция взима последната цифра на числото (най-ниската), като я изчислява като остатък при деление на 10.
number = number // 10
# explain Тази операция премахва последната цифра от числото, като изчислява целочисленото деление на числото на 10. Това премахва най-ниската цифра, като оставя останалите цифри.

digit_2 = number % 10
number = number // 10

digit_3 = number % 10
number = number // 10

digit_4 = number

# explain Тази операция задава последната останала цифра на числото като "digit_4"

# info Обединяване на цифрите в обратен ред
reversed_number = digit_1 * 1000 + digit_2 * 100 + digit_3 * 10 + digit_4

# info Извеждане на резултата
print("Обърнатото число е:", reversed_number)

print('\n')

print('*'*30)

# subchap Задача №14

# devider Сортирайте 3 реални числа в намаляващ ред. Използвайте вложени if оператори.

print('\n')
print('Задача №14')
print('\n')

# info Въвеждане на трите числа
num1 = float(input("Въведете първото число: "))
num2 = float(input("Въведете второто число: "))
num3 = float(input("Въведете третото число: "))

# info Сортиране на числата в намаляващ ред
if num1 >= num2:
    if num2 >= num3:
        largest = num1
        middle = num2
        smallest = num3
    elif num1 >= num3:
        largest = num1
        middle = num3
        smallest = num2
    else:
        largest = num3
        middle = num1
        smallest = num2
else:
    if num1 >= num3:
        largest = num2
        middle = num1
        smallest = num3
    elif num2 >= num3:
        largest = num2
        middle = num3
        smallest = num1
    else:
        largest = num3
        middle = num2
        smallest = num1

# info Извеждане на числата в намаляващ ред
print(f"Сортираните числа в намаляващ ред: {largest}, {middle}, {smallest}")

print('\n')

print('*'*30)

# subchap Задача №15

# devider Група запалянковци решили да си закупят билети за Евро 2016. Цената на билета се определя спрямо две категории:
# VIP – 499.99 лева
# Normal – 249.99 лева
# devider Запалянковците имат определен бюджет, a броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспорт:
# От 1 до 4 – 75% от бюджета
# От 5 до 9 – 60% от бюджета
# От 10 до 24 – 50% от бюджета
# От 25 до 49 – 40% от бюджета
# 50 или повече – 25% от бюджета
# да си купят билети за избраната категория, както и колко пари ще им останат или ще са
# им нужни.
# Входни данни
# Входът се чете от конзолата и съдържа точно 3 реда:
# На първия ред е бюджетът – реално число в интервала [1 000.00 … 1 000 000.00.
# На втория ред е категорията – "VIP" или "Normal".
# На третия ред е броят на хората в групата – цяло число в интервала [1 … 200].
# Изходни данни
# Да се отпечата на конзолата един ред:
# Ако бюджетът е достатъчен:
# "Yes! You have {N} leva left." – където N са останалите пари на групата.
# Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {М} leva." – където М е сумата, която не достига.
# Сумите трябва да са форматирани с точност до два символа след десетичния знак.

print('\n')
print('Задача №15')
print('\n')

# info Въвеждане на входни данни
budget = float(
    input("Въведете бюджета на групата ([1 000.00 … 1 000 000.00.]): "))
category = input("Въведете категория (VIP или Normal): ")
group_size = int(input("Въведете броя на хората в групата: "))

# info Цени на билетите
vip_ticket_price = 499.99
normal_ticket_price = 249.99

# info Проценти за транспорт спрямо броя на хората в групата
if 1 <= group_size <= 4:
    transport_percentage = 0.75
elif 5 <= group_size <= 9:
    transport_percentage = 0.60
elif 10 <= group_size <= 24:
    transport_percentage = 0.50
elif 25 <= group_size <= 49:
    transport_percentage = 0.40
else:
    transport_percentage = 0.25

# info Изчисляване на общата цена за билетите
if category == "VIP":
    ticket_price = vip_ticket_price
else:
    ticket_price = normal_ticket_price

total_ticket_price = ticket_price * group_size

# info Изчисляване на цената за транспорт
transport_cost = budget * transport_percentage

# info Изчисляване на общата цена
total_cost = total_ticket_price + transport_cost

# info Проверка дали бюджетът е достатъчен
if total_cost <= budget:
    left_money = budget - total_cost
    print(f"Да! Разполагате с: {left_money:.2f}лв. остатък.")
else:
    needed_money = total_cost - budget
    print(f"Нямате достатъчно средства! Трябват ви още: {needed_money:.2f}лв.")

print('\n')

print('*'*30)

# subchap Задача №16

print('\n')
print('Задача №16')
print('\n')

# info Въвеждане на входни данни
month = input("Въведете избрания месец: ")
nights = int(input("Въведете броят нощувки: "))

# info Цени на студио и апартамент за нощувка
studio_price_may_october = 50
apartment_price_may_october = 60
studio_price_june_september = 75.20
apartment_price_june_september = 68.70
studio_price_july_august = 76
apartment_price_july_august = 77

# info Изчисляване на цена за целия престой
if month in ["May", "October"]:
    total_studio_price = studio_price_may_october * nights
    total_apartment_price = apartment_price_may_october * nights
    if nights > 7 and nights <= 14:
        total_studio_price *= 0.95  # explain 5% отстъпка
    elif nights > 14:
        total_studio_price *= 0.7  # explain 30% отстъпка за повече от 14 нощувки
elif month in ["June", "September"]:
    total_studio_price = studio_price_june_september * nights
    total_apartment_price = apartment_price_june_september * nights
    if nights > 14:
        total_studio_price *= 0.8  # explain 20% отстъпка за повече от 14 нощувки
else:  # info July and August
    total_studio_price = studio_price_july_august * nights
    total_apartment_price = apartment_price_july_august * nights

# explain приложи 10% отстъпка за апартамент за повече от 14 нощувки
if nights > 14:
    total_apartment_price *= 0.9

# info (допълнително проучване) Калкулиране на отстъпката за студио
studio_discount = 0  # info По подразбиране няма отстъпка
studio_discount_amount = 0  # info По подразбиране няма сума на отстъпката
if (month == "May" or month == "October") and nights > 7:
    if nights <= 14:
        studio_discount = 5
    else:
        studio_discount = 30
elif (month == "June" or month == "September") and nights > 14:
    studio_discount = 20

if studio_discount > 0:
    studio_discount_amount = total_studio_price * (studio_discount / 100)

# info (допълнително проучване) Калкулиране на отстъпката за студио
studio_discount = 0  # info По подразбиране няма отстъпка
studio_discount_amount = 0  # info По подразбиране няма сума на отстъпката
if (month == "May" or month == "October") and nights > 7:
    if nights <= 14:
        studio_discount = 5
    else:
        studio_discount = 30
elif (month == "June" or month == "September") and nights > 14:
    studio_discount = 20

if studio_discount > 0:
    studio_discount_amount = total_studio_price * (studio_discount / 100)

# info (допълнително проучване) Калкулиране на отстъпката за апартамент
apartment_discount = 0  # info По подразбиране няма отстъпка
apartment_discount_amount = 0  # info По подразбиране няма сума на отстъпката
if nights > 14:
    apartment_discount = 10

if apartment_discount > 0:
    apartment_discount_amount = total_apartment_price * \
        (apartment_discount / 100)

# info Прилагане на отстъпките
total_studio_price -= studio_discount_amount
total_apartment_price -= apartment_discount_amount

# info Извеждане на резултатите и отстъпките
print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
if studio_discount > 0:
    print(
        f"Studio discount: {studio_discount}% ({studio_discount_amount:.2f} lv.)")
if apartment_discount > 0:
    print(
        f"Apartment discount: {apartment_discount}% ({apartment_discount_amount:.2f} lv.)")

print('\n')

print('*'*30)

# subchap Задача №17

print('\n')
print('Задача №17')
print('\n')

# info Въвеждане на входни данни
N1 = int(input("Въведете първото число: "))
N2 = int(input("Въведете второто число: "))
operator = input("Въведете оператор (+, -, *, /, %): ")

# info Проверка за операцията и изчисление
if operator == "+":
    result = N1 + N2
    parity = "четно" if result % 2 == 0 else "нечетно"
# explain PARITY - технически термин за четност или нечетност
    print(f"{N1} {operator} {N2} = {result} - {parity}")
elif operator == "-":
    result = N1 - N2
    parity = "четно" if result % 2 == 0 else "нечетно"
    print(f"{N1} {operator} {N2} = {result} - {parity}")
elif operator == "*":
    result = N1 * N2
    parity = "четно" if result % 2 == 0 else "нечетно"
    print(f"{N1} {operator} {N2} = {result} - {parity}")
elif operator == "/":
    if N2 == 0:
        print(f"Не може да се дели {N1} на нула")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":
    if N2 == 0:
        print(f"Не може да се дели {N1} на нула")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")

print('\n')

print('*'*30)
