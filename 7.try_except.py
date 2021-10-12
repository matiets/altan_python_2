# Исключение (исключительные события,ситуации,ошибки)

# Пример исключения при делении на нуль
a = 100
b = 0

# отлов исключения
# try:
#     # потенцияльно аварийный код
#     print("все нормально :)")
#     c = a / b
# except:
#     # код который должен сработать при исключении
#     print("что то пошло не так :(")
#     c = 0

# print(c)


# Обработка множества исключений 
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
# # Конкретные типы исключений    
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Нужно ввести число!")    
# # общее исключение
# except Exception as err:
#     print(error)

# Конструкция "try-except-finally"
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
#     print("Полет нормальный! :)")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
#     result = 0
# finally:
#     print("Сработала finally")
#     result = 10    

# print(result)    


# Кастомизированные исключения











# Пример приближенный к реальности
# while True:
#     try:
#         a = int(input("Введите число: "))
#         с = 100 / a
#     except ZeroDivisionError:
#         print("Деление на ноль не допустимо!")
#         continue
#     except ValueError:
#         print("Вы ввели не число!")
#         continue
#     print(f"Result: {с}")
#     break

# Пример калькулятор
def calculate(n1, n2, op):
    d ={
        '+': lambda x, y: x + y
        '-': lambda x, y: x - y
        '*': lambda x, y: x * y
        '/': lambda x, y: x / y
    }  
    return d[op](n1, n2)  

while True:
    # Ввод данных
    cmd = input("Командуйте, сэр: ")
    if cmd == "stop":
        print("Bye,bye")
        break

    try:
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        op = input("Введите символ операции!")

    # Обработка данных
    result = calculate(num_1, num_2, op)
    except ZeroDivisionError:
        result "На ноль делить нельзя")
        continue
    except ValueError:
        result = "Вы ввели не число"
        continue
    finally:
    # Ввод данных
    print(f"Результат: {result}")