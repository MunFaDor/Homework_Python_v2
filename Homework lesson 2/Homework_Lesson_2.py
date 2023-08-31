# Задача 1 (примери от упражнение)--------------------------------------------------
print("Задача №1") 
print("")
x1 = 9
x2 = 7  
x3 = x1 - 2

user_name = "John"  # (snake-case
User_name = "John"  # (snake-case)
user_Name = "John"  # (lower Camel-case)
User_Name = "John"  # (Camel-case)

print(3)
print(3.14)
print(-3.14)
print(+3.14)

print ('x jdskfsk jfdskds')

print('')  
print(' ')

print(4/3)  
print(4 % 3)

print(5/3)
print(5 % 3)

a1 = 3
print(a1)

user_age = 19
print(user_age+18) #37
print(user_age>18) #True
print(user_age==18) #False
print(user_age!=18) #True
print(user_age>=18) #True 

user_age=19
user_language="fr"
if user_language=='en':
    print('Welcome') 

user_age=25
user_language='en'
if user_age>=18 and user_language=='en':
    print('Welcome')
print("")

# Задача 2 -------------------------------------------------------------

print("Задача №2") 
print("")
my_name = 'Ivo Stefanov'  #string SNAKE CASE
My_name = 'Ivo Stefanov'  #string SNAKE CASE
my_Name = 'Ivo Stefanov'  #string LOWER CAMEL-CASE
My_Name = 'Ivo Stefanov'  #string CAMEL-CASE
a2 = 5 
b = 3.5 

print(my_name) #STRING
print(My_name) #STRING
print(my_Name) #STRING
print(My_Name) #STRING

print(True) #BOOLEAN

print(False) #BOOLEAN

print(a2) #INTEGER

print(b) #FLOAT
print("")

#Задача 3 -------------------------------------------------------------

print("Задача №3") 
print("")
print(type(my_name)) 
print(type(My_name))
print(type(my_Name))
print(type(My_Name))
print(type(a2))
print(type(b))
print(type(True))
print(type(False))
print("")

#Задача 4 -------------------------------------------------------------

print("Задача №4") 
print("")
x=3 
y=10
result1 = x * y
result2 = x + y

print(result1)
print(result2)
print("")

#Задача 5 -------------------------------------------------------------

print("Задача №5") 
print("")
a = 245.54 #Страна на тригълник срещуположна на височината
h = 13.66  #Височина на триъгълника. 

S = (1/2)*a*h #Според формулата за лице на триъгълни по височина и страна (S = (a*h)/2)

print("Лицето на триъгълника е:", S, "кв. см") #Показване на резултата. 
print("")

#Задача 6 -------------------------------------------------------------

print("Задача №6") 
print("")
print("Променливите не се виждат защото няма Print команда")

first_name = "димитър"          # Първо име(STRING)
last_name = "Иванов"            # Фамилия (STRING)
age = 30                        # Възраст (INTEGER)
gender = "M"                    # Пол ('м' или 'ж')
employee_id = 27560000          # Уникален номер на служителя (INTEGER)
print("")

#Задача 7 -------------------------------------------------------------

print("Задача №7") 
print("")
F = 5  #Променлива А
D = 10 #Променлива Б

print("Преди размяната") #Показваме че променливите са присвоени правилно.
print("F=", F)
print("D=", D)

#Разменяме стойностите на двете променливи.

temp = F
F = D
D = temp

print("След размяната") #Показваме че променливите са разменени правилно.
print("F=", F)
print("D=", D)

print("")

#Задача 8 ------------------------------------------------------------------------------

print("Задача №8") 
print("")

# Въвеждане на дължина и височина от потребителя
length = float(input("Въведете дължина на успоредник: "))
height = float(input("Въведете височина на успоредник: "))

# Изчисляване на периметъра и лицето на успоредник
perimeter = 2 * (length + height)
area = length * height

# Отпечатване на резултатите
print("Периметърът на успоредника е:", perimeter, "см")
print("Лицето на успоредника е:", area ,"кв. см")
print("")

#Задача 9 ------------------------------------------------------------------------------

print("Задача №9") 
print("")

# Въведете стойности за a, b и c
PTA = float(input("Въведете стойност за a: "))
PTB = float(input("Въведете стойност за b: "))
PTC = float(input("Въведете стойност за c: "))

# Пресмятане на a^2 + b^2
a_squared_plus_b_squared = PTA**2 + PTB**2

# Проверка дали уравнението a^2 + b^2 = c^2 е вярно
result = a_squared_plus_b_squared == PTC**2

if result:
    print("Дадените стойности удовлетворяват Питагоровата теорема.")
else:
    print("Дадените стойности НЕ удовлетворяват Питагоровата теорема.")

print("Пресметнатото a^2 + b^2 е:", a_squared_plus_b_squared)
print("Стойността на c^2 е:", PTC**2)
print(" ")

#Задача 10 ------------------------------------------------------------------------------

print("Задача №10") 
print("")

pi = 3.14 # числото Пи е зададено като константа

R = float(input("Въведете стойност за R:")) # въвеждане на радиуса на окръжността

Area_Circle = pi*R**2 #изчисляване на лицето на окръжността

print("Лицето на окръжността е:", Area_Circle ,"кв. см") #Показване на резултата

#Задача 11 ------------------------------------------------------------------------------

print("Задача №11") 
print("")

INCH = int(input("Въведете INCH: "))

CM = INCH*2.54

print(f"{INCH} инча са {CM} сантиметра")

#Показване на резултата с използване на f-стринг (форматиран низ)