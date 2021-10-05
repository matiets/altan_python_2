# Циклы (операторы циклов)

# jgthfnjh while

# бесконечный цикл (условие всегда истина (true))
# while True:
#     print("Hello")

# цикл (whil) прерывающийся по условии
num = 0

# while num < 10:
#     # print(num)
#     # # инкремент
#     # num = num + 1 # длинная запись
#     num += 1 # короткая запись
#     print(num)

# прерывание цикла по дополнительному условию
num = 10

# while num > 0:
#     print(num)
#     if num == 5:
#         # инструкция прерывания цикла
#         break
#     # декремент(уменьшение величины) (-= оператор декремента)
#     num -= 1

num = 50
# while num < 100:
#     s = input("Введите команду: ")
#     if s == "stop":
#         print("Bye,bye!")
#         break
#     print(f"Вы ввели: {s}")
#     num += 10

# пропуск куска кода в теле цикла
# while True:
#     s = input("Введите слово Да: ")
#     if s == "ДА":
#         print("Цикл продолжается! :)")
#         continue
#     print("Циклу конец :(")
#     break


# оператор for

#  1.читает значение элемента итерируемого объекта по порядку
#  2.значение присваивается в свою переменную
#  3.выполняет блок кода своего тела

# for n in [1,2,3,4,5]:
#     print(n)

# for m in [10,20,30,40,50]:
#       print(m)

# for _ in (1,2,3,4):
#     print("Hello")

    # for char in "python":
    #     print(char)

my_tuple = (100, 400, 200, 700)

# for i in my_tuple:
#     res = i * 2
#     print(res)

# for i in my_tuple[::-1]:
#     print(i)


# класс range()

# r = range(2, 10)
# print(r)

# for n in range(2, 10):
#     print(n)

# for n in range(10):
#     print(n)

# for n in range(10, 100, 10)[::-1]:
#     print(n)

# ***генератор списка***

my_list = [num for num in range(50, 100, 10)]

my_list = [num + 100 for num in range(10)]

my_list = [num for num in range(10) if num % 2 == 0]

print(my_list)