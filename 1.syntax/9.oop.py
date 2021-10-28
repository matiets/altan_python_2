# *** Полиморфизм ***

# поли-много,морф-форма= определяет разны формы чего то

# Полиморфизм операторов
res = 100 + 20 # сложение
res = "100" + "20" # конкатенация

# Полиморфизм функций
res = len("python")
res = len([10, 20, 30])

# print(res)

# Полиморфизм методов
class A:
    # атрибут создан без конструктора
    attr_1 = 100
    def m1(self, arg):
        print(arg + self.attr_1)

class B:
    def m1(self, arg):
        print(arg * 5)

obj_a = A()
obj_b = B()

# obj_a.m1(10)
# obj_b.m1(10)

class C(A):
    pass

class D(A):
    def m1(self):
        print("hello man", self.attr_1)

obj_c = C()
obj_d = D()

# obj_c.m1(10)
# obj_d.m1()

# Полиморфизм с "магическими" методами (методами перегрузки операторов)

class Sum:
    def __call__(self, a, b):
        print(a + b)
    def __str__(self):
        return "Sum object"
s = Sum()

# s = Sum()
# s(10, 20)
# print(s)


# *** Инкапсуляция ***

# Инкапсуляция - вскрытие атрибутов или методов
# что бы они не были доступны из экземпляров класса

# не строгая инкапсуляция 
class X:
    def __init__(self, arg):
        self._attr = arg

    def _m1(self, arg):
        return self._attr ** arg

    def m2(self, arg):
        print(self._m1(arg))

x = X(5)
x.m2(10)