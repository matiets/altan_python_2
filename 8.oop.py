# *** Основы объектно ориентированого программирования ***

# Объекты обладают свойствами и методами
# Каждый объект пренадлежит определенному классу (типу)
# Класс = "чертеж"объекта.
# Объект = экземпляр (инстанс)класса

# Создание (определение)класса.
# Название классов принято писать с заглавной буквы.
class Cat:
    # метод-конструктор
    def __init__(self):
        # свойства (атрибуты, поля)
        self.name = None
        self.color = None
        
    # метод (атрибут) - функция пренадлежащая к классу
    def mur(self):
        print("Mur-mur!")
    def speech(self):
        print(f"Name: {self.name}, Color: {self.color}")
    # Магический метод(метод перегрузки операторов),который наделяет объект способностью функций

    def __call__(self, a, b):
        return a + b

# Создание объектов (экземпляров) на базе cat
cat_1 = Cat()
cat_2 = Cat()

# запись данных в свойства
cat_1.name = "Pushok"
cat_1.color = "white"

cat_2.name = "Juchka"
cat_2.color = "black"

# чтение данных из свойств
# print(cat_1.name)
# print(cat_2.name)

# Вызов метода 

# cat_1.mur()
# cat_1.speech()

# cat_2.mur()
# cat_2.speech()


# благодаря методу  __call__ объекты ведут себя как функции
# result = cat_1(100, 20)
# print(result)

# *** Принципи ООП ***


# Принцип наследования

# Создание родительского (предкого) класса
class Animal:
    def __init__(self, num_legs):
        self.legs = num_legs
    
    def move(self):
        print("я двигаюсь!")

# Создание дочерних классов
class Human(Animal):
    def __init__(self, num_legs, name):
        super().__init__(num_legs)
        self.name = name

    def speech(self):
        print(f"My name is {self.name}.Legs: {self.legs}")

class Cat_2(Animal):
    def __init__(self, legs, name, color):
        super().__init__(legs)
        self.name = name
        self.color = color
    def speech(self):
        print(f"My name is {self.name}.Legs: {self.legs}, Color: {self.color}")

    def mur(self):
        print("Mur-mur!")

# Создание объектов
bug = Animal(6)

man_1 = Human(2, "Petya")
women_1 = Human(2, "Katya")

cat_1 = Cat_2(4, "Pushok", "green")

# Вызовы методов
bug.move()
print(bug.legs)

man_1.move()
man_1.speech()

cat_1.move()
cat_2.speech()
cat_1.mur()
