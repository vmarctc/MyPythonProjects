"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет,
не превышая ее вместимость.

При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.

"""


class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        if (self.money + v) > self.capacity:
            return False
        elif (self.money + v) <= self.capacity:
            return True

    def add(self, v):
        if self.can_add(v):
            self.money += v
            return True
        else:
            return False


money_box = MoneyBox(200)

print(money_box.add(100))
print(money_box.can_add(150))
print(money_box.money)
