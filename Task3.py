# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

#
# Задание №6
# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода
# проекта.
from Task4 import User


class MyException(Exception):
    pass


class LevelException(MyException):
    def __init__(self, level: int, user: User):
        self.user = user
        self.level = level

    def __str__(self):
        return f'Нельзя добавить пользователя с {self.level}' \
               f'Вы вошли как {self.user.name} с уровнем {self.user.user_level}'


class AccesException(MyException):
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'Отказано в доступе!' \
               f'Пользователь{self.name} {self.user_id}не найден'


class SizeException(MyException):
    def __init__(self, r: int):
        self.r = r

    def __str__(self):
        return f'Данные введены не верно. Радиус должен быть больше нуля!'

class NameException(MyException):
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'Данные введены не верно! Введены недопустимые символы'