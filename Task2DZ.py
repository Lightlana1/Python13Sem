# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.
from enum import Enum

from Task3 import NameException
class Gender(Enum):
    male = 'male'
    female = 'female'

class Human:
    def __init__(self, name: str, patr_name: str, last_name: str, age: int, gender: Gender):
        self.name = name
        self.patr_name = patr_name
        self.last_name = last_name
        self.__age = age
        self.gender = gender

    def birtday(self):
        self.__age+=1

    def name_verification(self):
        if self.name.isalpha() == True and self.last_name.isalpha() == True:
            pass
        else:
            raise NameException(self.name, self.last_name)


    def get_age(self):
        self.name_verification()
        return self.__age

    def fell_name(self)->str:
        return f'{self.last_name}{self.name}{self.patr_name}'

if __name__ == '__main__':
    human1 = Human('Bob', '', 'Joh5nson', 27, Gender.male)
    print(human1.get_age())
    human1.birtday()
    print(human1.get_age())