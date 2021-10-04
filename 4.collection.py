# Коллекции

# Список (list)

# создание пустого списка
my_list = []
my_list = list()

# создание предварительно наполненного списка
# my_list = [10, 20, 3, 7, "python" 3.14, [1,2,3]]

# добавление объекта (элемента) в список
my_list = {}

# my_list.append(100)
# my_list.append(2.5)
# my_list.append("hello")
# my_list.append([10,20,30])

# Чтение значений элемента списка
# Прямая индексация( с лева на право)

el = my_list[1]
el = my_list[4]

# Чтение значений вложеных коллекций

el = my_list[2][1]

# Обратная индексация
el = my_list[-1]

# Замена значений
my_list[3] = 777.0

# Удаление элемента позначению
my_list.remove(2.5)

# Удаление элемента по индексу
del my_list[-1]

print(my_list)
# print(el)

# Срез списка

#  создание исходного списка из строки
s = "Hello,World!"
my_list = list(s)


# Срез от начала до конца
my_slice = my_list[:]

# Срез от второго индекса до конца исходного списка
my_slice = my_list[2:]

# Срез с начала списка до пятого индекса не включительно

my_slice = my_list[:5]

# Срез с третьего индекса до седьмого индекса не включительноM
my_slice = my_list[3:7]

# Cрез от начала до конца списка с шагом 2
my_slice = my_list[::2]

# Срез с третьего индекса до восьмого не включительно
my_slice =my_list[3:10:3]

# Срез от -2 до -9 не включительно с шагом 2

my_slice = my_list[-2:-9:-2]

# Переворот спискасрезом
my_slice = my_list[::-1]

# print(my_list)
# print(my_slice)

# Длина - число элементов в объекте
# print(len(my_list))


# Кортеж (tuple)

# Неизменяемая (immutable)
# легковеснее, чемм список

# создание кортежа
my_tuple = (10, 20, 30, 40)

# Чтение значений
el = my_tuple[0]

# срез

print(my_tuple)
print(el)

my_slice = my_tuple[2:]

# Словарь (dict)
# пара "ключ-значение"
# {ключ_1:значение_1, ключ_2:значение_2}

# Создание словаря
my_dict = {10:3.14, "abc":[1,2,3], 'A':"python"}

# чтение значения
val = my_dict["abc"]

print(my_dict)
print(val)