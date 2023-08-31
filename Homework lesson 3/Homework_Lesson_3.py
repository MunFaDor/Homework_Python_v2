
#chapter - Домашна работа - урок 3 

#subchap - Задача №1

print("23 4.5 False John")

print('*'*30) #devider - разделение между задачите. 

#subchap - Задача №2
print('\n')
name = "Ivo"
activity1 = "voleyball"
activity2 = "Python/FrontEnd/Backend"

text1 = "{}'s favorite sports is {}.".format(name, activity1)
text2 = "{} is working on {} programming!".format(name, activity2)

print(text1)
print(text2)

print('*'*30) #devider - разделение между задачите. 

#subchap - Задача №3
print('\n')
paragraph = "\"Python is a great language!\", said Fred. \"I don't ever remember having this much fun before."
print(paragraph)

print('*'*30) #devider - разделение между задачите. 

#subchap - Задача №4 (Задача №1 втора част от лекцията.)
print('\n')
school = "school"  #info Създаване на стринг с името "school"
school = school.replace("school", "СОУ Св.Патриарх Евтимий") #info Модификация на стринга, като заместваме "school" с името на нашето  училище:

print(school)  #info  Извеждане на модифицирания стринг
print('*'*30) #devider - разделение между задачите. 

#subchap - Задача №5 (Задача №2 втора част от лекцията.)
print('\n')

#info  Създаване на стринг "usa" и присвояване на променливата country
country = "usa"

#info  Използване на метода upper() за да създадем нов стринг с големи букви
correct_country = country.upper()

#info  Извеждане на оригиналната страна (с малки букви) и коригираната страна (с големи букви)
print("Страна:", country)
print("Коригирана страна:", correct_country)

print('*'*30) #devider - разделение между задачите. 

#subchap - Задача №6 (Задача №3 втора част от лекцията.)
print('\n')

filename = "hello.py"

#info Проверка дали стринга завършва на ".java"

if filename.endswith(".java"):
    print("Файлът е Java файл.")
else:
    print("Файлът не е Java файл.")

#info  Намиране на индекса на "py"

index_of_py = filename.index("py")
print("Индексът на 'py' във filename е:", index_of_py)

#info Проверка дали думата започва с "world"

if filename.startswith("world"):
    print("Файлът започва с 'world'.")
else:
    print("Файлът не започва с 'world'.")

print('*'*30) #devider - разделение между задачите. 

#subchap - Задача №7 (Задача №4 втора част от лекцията.)
print('\n')

text = "Примерен текст"#info Дефиниране на начален текст

uppercase_text = text.upper() #info Използване на метода .upper() за създаване на нов стринг с главни букви
print(uppercase_text) #info Извеждане на текста с главни букви

print('*'*30) #devider - разделение между задачите. 

#subchap - Задача №8 (Задача №5 втора част от лекцията.)
print('\n')
name = "$$John Smith"


name_lstrip = name.lstrip("$$") #info Използване на .lstrip() за премахване на "$$" от началото на името

name_strip = name.strip("$$") #info Използване на .strip() за премахване на "$$" от началото и края на името


print('След използване на.lstrip():', name_lstrip)
print('След използване на.strip():', name_strip)

#important .lstrip() премахва подадения символ или низ от началото на стринга
#important .strip() премахва подадения символ или низ както от началото, така и от края на стринга.

print('/'*30) #devider - разделение между задачите. 

#subchap - Задача №8 (Задача №5 втора част от лекцията.)
print('\n')

#info Дефиниране на необходимите текстови променливи
header = "*"*70
company_name = "CODING TEMPLATE, INC."
address_line1 = "283 FRANKLIN ST."
address_line2 = "BOSTON, MA."
separator = "="*70
product_header = "Product name    Product Price"
product_lines = ["Books", "Computer", "Monitor"]
product_prices = [49.95, 579.99, 124.89]
total_line = "TOTAL:  ${:.2f}".format(sum(product_prices))
thank_you = "Thank you for shopping with us today!"
footer = "*"*70

#info Създаване на изходния текст, като обединим всички променливи
output = f"""
{header}
{company_name.center(70)}
{address_line1.center(70)}
{address_line2.center(70)}
{separator}
{product_header}
"""

#info Добавяне на редовете за продуктите и техните цени
for product, price in zip(product_lines, product_prices):
    output += f"\n{product.ljust(15)} ${price:.2f}"

#info Добавяне на останалите части от изходния текст
output += f"""
{separator}
{total_line.rjust(68)}
{separator}
{thank_you.center(72)}
{footer}
"""

#infoИзвеждане на изходния текст
print(output)
