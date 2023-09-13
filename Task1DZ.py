# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi as pi

from Task3 import SizeException


class Circle:
    def __init__(self, r: int):
        self.r = r

    def check_radius(self):
        if self.r>0:
            return self.r
        else:
            raise SizeException(self.r)
    def get_leght(self) -> float:
        self.check_radius()
        return pi * 2 * self.r

    def get_squre(self) -> float:
        self.check_radius()
        return pi * (self.r ** 2)




if __name__ == '__main__':
    cir_one = Circle(-12)
    print(cir_one.get_leght())
    print(cir_one.get_squre())
