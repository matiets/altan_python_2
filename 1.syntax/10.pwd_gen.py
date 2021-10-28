# *** Генератор паролей ***

# password_fb

# импортирование модулей
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar
import tkinter

def generator():
    # чтение строки сырой пароли
    pwd_str = pwd.get()
    # кодирование в байт-строка
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]

    # вывод хеш-строки
    # print(hex_str)
    hash_pwd.set(hex_str)
# generator("qwerty")

# Создаем объект окна
window = Tk()
window.title("Pwd generator v.0.1")

# объекты для хранения строк
pwd = StringVar()
hash_pwd = StringVar()

# тестирование StringVar
# pwd.set("qwerty")

# print(pwd.get())

# Виджет (компонент) текстовой метки

lbl = Label(text="Пароль:")
lbl.grid(row=0, column=0)

# Виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1)

# Виджет кнопки
Button(text="СТАРТ",command=generator).grid(row=1, column=0)

# Виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1)

#  Точка входа программы (место где программа запускается)
window.mainloop()