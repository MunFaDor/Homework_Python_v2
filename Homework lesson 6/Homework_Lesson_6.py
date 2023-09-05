
# chapter ---------------------- Homework Lesson 6 ----------------------

# subchap Задача №1

# devider Да се напише програма, която да намира тези числа, които се делят на 7 и на 5, между 1500 и 2700.
print("\n")
print("Задача №1")
print("\n")
# explain Итерираме числата в интервала [1500, 2700]
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №2

# devider Да се състави програма, която ще изчисли сумата на 5, въведени от клавиатурата, естествени числа от интервала [10 ..5555]. Вход: 1,2,3,4,5 Изход: 15

print("\n")
print("Задача №2")
print("\n")

numbers = []  # explain Списък, в който ще съхраняваме въведените числа

# explain Въвеждане на 5 числа
for i in range(5):
    while True:
        try:
            num = int(input(f"Въведете число {i+1} от интервала [10..5555]: "))
            if 10 <= num <= 5555:
                numbers.append(num)
                break  # explain Излизаме от цикъла при успешно въвеждане
            else:
                print("Грешка! Въведете валидно число.")
        except ValueError:
            print("Грешка! Въведете числова стойност.")

# explain Изчисляване на сумата на въведените числа
total_sum = sum(numbers)
print(f"Сумата на въведените числа е: {total_sum}")

print("\n")
print("*"*30)
print('\n')

# subchap Задача №3

#devider Да се напише програма, която да създаде следният шаблон: 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

print("\n")
print("Задача №3")
print("\n")

#explain Горна половина на шаблона
for i in range(1, 6):
    print('* ' * i)

#explain Долна половина на шаблона
for i in range(4, 0, -1):
    print('* ' * i)

print('\n'*2)
print("*"*30)
print('\n')
# subchap Задача №4

#devider Да се напише програма, която да обръща буквите на дадена дума на обратно.Думата да бъде въведена от клавиатурата. Като за целта използвате цикъл. Вход: Input a word to reverse: Hello -> Изход: olleH

print("\n")
print("Задача №4")
print("\n")
#explain Въвеждане на дума от потребителя
word = input("Input a word to reverse: ")

#explain Инициализиране на празна променлива за обратната дума
reversed_word = ""

#explain Цикъл, който обхожда всеки символ във въведената дума
for char in word:
    #explain Добавяне на текущия символ преди текущата обратна дума
    reversed_word = char + reversed_word

#explain Извеждане на обратната дума
print("Reversed word:", reversed_word)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №5

#devider Да се напише програма, която да намира броят на четните и нечетните числа от списък от цели числа.

print("\n")
print("Задача №5")
print("\n")

#explain Въвеждане на списък от цели числа
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

#explain Инициализиране на броячи за четни и нечетни числа
even_count = 0
odd_count = 0

#explain Обхождане на всеки елемент от списъка
for num in numbers:
    if num % 2 == 0:  #explain Проверка за четно число
        even_count += 1
    else:
        odd_count += 1

#explain Извеждане на резултатите
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №6

#devider Да се напише програма, която да принтира всички числа от 0 до 6, без да включва 3 и 6.

print("\n")
print("Задача №6")
print("\n")

#explain Използваме цикъл, за да обходим числата от 0 до 6
for num in range(7):
    #explain Проверка дали числото не е 3 или 6
    if num != 3 and num != 6:
        #explain Извеждане на числото, за което условието е изпълнено
        print(num)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №7

#devider Да се напише програма, която принтира редицата на Фибуначи между 0 и 50. Редицата на Фибуначи е: 0, 1, 1, 2, 3, 5, 8, 13, 21, … Всяко следващо число е сумата от предходните две.

print("\n")
print("Задача №7")
print("\n")

#explain Първите две числа на редицата на Фибоначи
num1 = 0
num2 = 1

#explain Използвайте цикъл, за да генерирате редицата на Фибоначи до 50
while num1 <= 50:
    print(num1)
    next_num = num1 + num2  #explain Изчисляване на следващото число
    num1 = num2
    num2 = next_num

print("\n")
print("*"*30)
print('\n')

# subchap Задача №8

#devider Да се принтира буквата A на екрана както е дадено по-долу:
                #  ***
                # *   *
                # *   *
                # *****
                # *   *
                # *   *
                # *   *

print("\n")
print("Задача №8")
print("\n")

#Explain Височина на буквата A
height = 7

#explain Генериране на буквата A
for i in range(height):
    if i == height // 2:
        print('*' * (i * 2 + 1))
    elif i < height // 2:
        print(' ' * (height // 2 - i) + '*' + ' ' * (i * 2 - 1) + '*' if i != 0 else '*' * (i * 2 + 1))
        
#important - не излиза правилната буква :/

# *
#   * *    #info - output.
#  *   * 
# *******

print("\n")
print("*"*30)
print('\n')

# subchap Задача №9
#devider - Да се напише програма, която принтира следният шаблон:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

print("\n")
print("Задача №9")
print("\n")

#explain Генериране на шаблона
for i in range(1, 10):
    print(str(i) * i)

print("*"*30)
print('\n')

# subchap Задача №10

#devider - Да се напише програма, която принтира следният шаблон:

print("\n")
print("Задача №10")
print("\n")

def product(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        partial_sum = 1
        for j in range(i, 2 * i + 1):
            partial_sum *= j
        total_sum += partial_sum
    return total_sum

#explain Въвеждане на едноцифрено число
number = int(input("Въведете едноцифрено число: "))

#explain Проверка за валидност на числото
if 0 <= number <= 9:
    result = calculate_sum(number)
    print("Изход:", result)
else:
    print("Грешка! Въведете валидно едноцифрено число.")

print("\n")
print("*"*30)
print('\n')

# subchap Задача №11

#devider - Да се състави програма, която извежда всички цели числа от интервала [1-50], които удовлетворяват проверка на следното условие: c^3 = a^2 + b^2

print("\n")
print("Задача №11")
print("\n")

for c in range(1, 51):
    for a in range(1, 51):
        for b in range(1, 51):
            if c**3 == a**2 + b**2:
                result = a**2 + b**2
                print(f"Found result: {a}^2 + {b}^2 = {c}^3, Sum: {result}")

print("\n")
print("*"*30)
print('\n')

# subchap Задача №12

#devider - Да се състави програма, която извежда всички цели числа от интервала [1-50], които удовлетворяват проверка на следното условие: c^3 = a^2 + b^2

print("\n")
print("Задача №12")
print("\n")

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n")
print("*"*30)
print('\n')

# subchap Задача №13

#devider - Да се състави програма, чрез която се извежда квадрат от цифри. Сумите от елементите на произволен ред или стълб са равни на 45.

print("\n")
print("Задача №13")
print("\n")

for i in range(1, 11):
    row = [(i + j) % 10 for j in range(10)]
    print(" ".join(map(str, row)))

print("*"*30)
print('\n')

# subchap Задача №14

#devider - Да се напише програма, която да генерира число на случен принцип и да подкани потребителя да познае това число. Да извежда следните стойности too low, too high, или exactly right, в случай, че потребителя е познал, или не числото..

print("\n")
print("Задача №14")
print("\n")

import random

#explain Генериране на случайно число в интервала [1, 100]
secret_number = random.randint(1, 100)

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")

#explain Цикъл, в който потребителят може да опита да познае числото
while True:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Exactly right! The secret number was {secret_number}.")
        break

print("\n")
print("*"*30)
print('\n')

# subchap Задача №15

#devider - Да се напише програма, която подканва потребителя да въведе число и програмата да провери дали то е просто или не.

print("\n")
print("Задача №15")
print("\n")

def is_prime(n):
    if n <= 1:
        return False  #explain Числата <= 1 не са прости
    if n <= 3:
        return True  #explain Числата 2 и 3 са прости
    if n % 2 == 0 or n % 3 == 0:
        return False  #explain Числата, които се делят на 2 или 3, не са прости
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  #explain Числата, които се делят на i или i + 2, не са прости
        i += 6
    return True  #explain Ако не сме намерили делител до тук, числото е просто

#explain Въвеждане на число от потребителя
number = int(input("Please enter a number: "))

#explain Проверка дали числото е просто и извеждане на съобщение
if is_prime(number):
    print("The number is prime.")
else:
    print("The number is not prime.")

print("\n")
print("*"*30)
print('\n')

# subchap Задача №16

#devider - Да се създаде програма, която да въвежда текст от клавиатурата и да премахва повтарящите се букви в текста. Вход: aaabbbccc Изход: abc

print("\n")
print("Задача №16")
print("\n")

def remove_duplicates(text):
    result = []  #explain Тук ще съхраняваме уникалните букви
    seen = set()  #explain Тук ще съхраняваме буквите, които сме видели

    for char in text:
        if char not in seen:
            result.append(char) #explain Ако буквата не сме я видели, добавяме я към резултата
            seen.add(char)  #explain Добавяме я към "видените" букви

    return ''.join(result)  #explain Обединяваме уникалните букви в текст

#explain Въвеждане на текст от потребителя
text = input("Enter text: ")

#explain Премахване на повтарящите се букви и извеждане на резултата
result = remove_duplicates(text)
print("Result:", result)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №17

#devider - Да се напише програма, която да приема от клавиатурата цяло число n и като резултат да принтира всички числа до въведеното. Вход: n = 4 Вход: n = 11 Изход: 1-2-3-4 Изход: 1-2-3-4-5-6-7-8-9-1-0-1-1 Вход: n = 15 Изход: 1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5

print("\n")
print("Задача №17")
print("\n")

n = int(input("Enter a number: "))
output = "-".join(str(i) for i in range(1, n + 1))
print(output)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №18

#devider - Да се напише програма, която да приема като вход текст и да намира количеството знаци в текста. Включват се интервалите и текста трябва да е с малки букви. Ако няма дубликати, да се принтира 0.

print("\n")
print("Задача №18")
print("\n")


#explain Въвеждаме текст от потребителя и го преобразуваме към малки букви
text = input("Enter text: ").lower()

#explain Създаваме множество, което ще съдържа уникалните символи в текста
unique_chars = set(text) #important вграден тип данни, който създава колекция от уникални елементи без дубликати. 

#explain Изчисляваме разликата между общия брой на символите и броя на уникалните символи
count = len(text) - len(unique_chars) #important се използва, за да намерим дължината (броя на елементите) на дадена колекция, като например списък, низ или множество.

#explain Проверяваме дали има дублиращи се символи
if count == 0:
    print(0)
else:
    print(f"result: {count}")

print("\n")
print("*"*30)
print('\n')

# subchap Задача №19

#devider - Да се напише програма, която приема като вход текст и обръща буквите от дясно наляво на само на думите, чиято дължина е нечетна, тези които са с четен брой си остават така като са. Вход: Bananas Вход: One two three four Изход: sananaB Изход: enO owt eerht four

print("\n")
print("Задача №19")
print("\n")


def reverse_odd_words(text):
    words = text.split() #explain Разделяне на текста на думи
    reversed_words = []  #explain Списък за съхранение на обръщаните думи

    for word in words:
        if len(word) % 2 == 1:  #explain Проверка дали дължината на думата е нечетна
            reversed_word = word[::-1]  #explain Обръщане на думата
            reversed_words.append(reversed_word) #important използваме APPEND за добавяне на елемент към края на списък. 
        else:
            reversed_words.append(word) 

    reversed_text = ' '.join(reversed_words)  #explain Обединяване на думите обратно в текст
    return reversed_text

text = input("Enter text: ")
reversed_text = reverse_odd_words(text)
print("Reversed text:", reversed_text)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №20

#devider - Да се напише програма, която да намира най-близкото число палиндром дo въведено цяло число от клавиатурата.

#* - Полинома на 888 е 888 но програмата го представя като 878 заради глобалното условие. Ако се промени така че да изкарва верния полиндром за 888 ще показва грешни за останалите примери. 

print("\n")
print("Задача №20")
print("\n")

def is_palindrome(n):
    return str(n) == str(n)[::-1]
#~ Функция, която проверява дали дадено число е палиндром. Преобразува числото в низ и сравнява го с низа, обърнат на обратно срещу нормалния.
def nearest_palindrome(num): 
# ~ Функция, която намира най-близкия палиндром на дадено число. Тя използва двa цикъла, за да намери най-близкия палиндром, по-малък и по-голям от въведеното число.
    num = int(num)
    
    if num < 0:
        return "Invalid input"
    
    lower_palindrome = num - 1
    while not is_palindrome(lower_palindrome):
        lower_palindrome -= 1
        
    higher_palindrome = num + 1
    while not is_palindrome(higher_palindrome):
        higher_palindrome += 1
        
    if abs(num - lower_palindrome) <= abs(num - higher_palindrome):
        return lower_palindrome
    else:
        return higher_palindrome

number = input("Enter a number: ") #explain Вход от потребителя
nearest = nearest_palindrome(number)#explain Намиране на най-близкия палиндром и извеждане на резултата
print("The nearest palindrome is:", nearest)

print("\n")
print("*"*30)
print('\n')

# subchap Задача №21

#devider - Да се напише програма, която да принтира буквата M със *

print("\n")
print("Задача №21")
print("\n")

n = 7 
for i in range(n):
    print(" " * i + "*" + " " * (2 * n - 2 * i - 2) + "*" + " " * i)

# Отново не се получава както при задачата със буквата А. 

#!  *          * 
#!   *        *  
#!    *      *    #info output
#!     *    *    
#!      *  *     
#!       **    

print("\n")
print("*"*30)
print('\n')

# subchap Задача №22

#devider - Да се напише програма, която да принтира буквата D със *

print("\n")
print("Задача №22")
print("\n")

n = 7
for i in range(n):
    print("*" + " " * (n - 2) + "*")
for i in range(2):
    print("*" * n)

# Отново не се получава както при задачата със буквата А. 

#! *     *
#! *     *    output
#! *******
#! *******

print("\n")
print("*"*30)
print('\n')

#! subchap Задача №23

#. - Напишете програма, която пресмята N!/K! за дадени N и K (1<K<N). Без да се ползват вградени функции.

print("\n")
print("Задача №23")
print("\n")

#! Вариант №1

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


N = int(input("Въведете N: "))
K = int(input("Въведете K (1 < K < N): "))


if K <= 1 or K >= N:
    print("Грешка: K трябва да е по-голямо от 1 и по-малко от N.")
else:
    result = factorial(N) // factorial(K)
    print(f"{N}!/{K}! = {result}")

#! Вариант №2

""" import math

N = input(("Въведете числена стойност за N: "))
K = input(("Въведете числена стойност за K: "))
fact = 1

if N.isdigit() and K.isdigit():
    N = int(N)
    K = int(K)
    if N == 0 and K== 0:
        print("Invalid input")
        quit()
    if 1 < K and K < N:
        result = math.factorial(N)/math.factorial(K)
        print(f"The result of {N}! / {K}! is: {result}")
    else:
        print("K must be less than N")
else:
    print("Please enter a valid number for N and K.") """

print("\n")
print("*"*30)
print('\n')

#! subchap Задача №24

#. - Напишете програма, която пресмята N!*K!/(N-K)! за дадени N и K (1<K<N). Без да се ползват вградени функции.

print("\n")
print("Задача №24")
print("\n")

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

N = int(input("Въведете N: "))
K = int(input("Въведете K (1 < K < N): "))

if K <= 1 or K >= N:
    print("Грешка: K трябва да е по-голямо от 1 и по-малко от N.")
else:
    result = factorial(N)*factorial(K) // factorial(N-K)
    print(f"{N}!*{K}!/({N}-{K})! = {result}")

print("\n")
print("*"*30)
print('\n')

#! subchap Задача №25

#. - Напишете програма, която за дадено цяло число n, пресмята сумата: S=(1+(1!/x)+(2!/x^2)+...+(n!/x^n)

print("\n")
print("Задача №25")
print("\n")

import math

def calculate_sum(n, x):
    if n == 0 and x == 0:
        print("Грешка, не може да се дели на нула.")
        return None
    total_sum = 0
    for i in range(n + 1):
        factorial = math.factorial(i)
        denominator = x ** i
        term = factorial / denominator
        total_sum += term

    return total_sum

n = int(input("Въведете цяло число n: "))
x = float(input("Въведете реално число x: "))

result = calculate_sum(n, x)
print(f"S = {result}")

print("\n")
print("*"*30)
print('\n')

#! subchap Задача №26

#. - Напишете програма, която чете от конзолата положително цяло число N (N < 20) и отпечатва матрица с числа като на фигурата по-долу:
#. 123 при вход 3 // 1234
#. 234 при вход 3 // 2345 при вход 4
#. 345 при вход 3 // 3456
#. 345 при вход 3 // 4567

print("\n")
print("Задача №26")
print("\n")

N = int(input("Въведете положително цяло число N (< 20): "))

if N < 1 or N >= 20:
    print("Грешка: N трябва да бъде положително цяло число по-малко от 20.")
else:
    for i in range(1, N + 1):
        for j in range(i, i + N):
            print(j, end=" ")
        print()

print("\n")
print("*"*30)
print('\n')