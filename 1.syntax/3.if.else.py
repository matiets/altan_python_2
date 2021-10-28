# Логические и условные операторы

# Операторы сравнения

z = 3
w = 2

# операция "равно"
# мы спрашиваем "значение z рано значению переменной w"?
result = z == w

# операция "не равно"
result = z != w

# операция "меньше"
result = z < w

# операция "больше"
result = z > w

# операция "меньше либо равно"
result = z <= w

# операция "больше либо равно"
result = z >= w

# чистые логические операции

var_1 = False
var_2 = True

# оператор "НЕ" (NOT, инверция)
result = not var_2 

# оператор "И" (ADN, конъюнкция)
# возвращает значение True только тогда
# когда оба переменных является True 
result = var_1 and var_2

# оператор "ИЛИ" (OR, дизъюнкция)
# возвращает значение False только тогда
# когда оба переменных является False
result = var_1 or var_2

# пример комбинации логических операторов
a = 5
b = 3
c = 3

result = ((a > b) and (b != c)) or (a == c)

# print(result)


# условные операторы

var = 10

# оператор IF
# if var != 0:
#     print("hello")

# if True:
#     print("Hi!")

if not var < 12:
    print("Hello")

# оператор ELSE
var = -1

# if var > 0:
#     print("больше нуля")
# else:
#     print("не больше нуля")

# оператор ELIF
# else if
var = 0

# if var > 0:
#     print("больше нуля")
# elif var < 0:
#     print("меньше нуля")
# else:
#     print("равно нулю")

var = 'a'

if var == 'A':
    res = "literal A"
elif var == 'a':
    res = "literal a"
elif var == 'B':
    res = "literal B"
elif var == 'C':
    res = "literal C"

# print(res)


# пример. Калькулятор

num_1 = int(input("Введите первое число"))
num_2 = int(input("Введите второе число"))

op = input("Введите символ операции: ")

if op == '+':
    res = num_1 + num_2
elif op == '-':
    res = num_1 - num_2
elif op == '*':
    res = num_1 * num_2
elif op == '/':
    res = num_1 / num_2    
else:
    res = "символ операции не корректен! :("

print(f"Результат = {res}")