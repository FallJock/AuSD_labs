# если из другой папки то меняем путь для библиотеки структур данных
# import sys
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from structuredata.minheap import MinHeap
from typing import Self
from dataclasses import dataclass
from functools import total_ordering

# дополняет недостающие методы за счёт других (изменятся >=, <=, !=, >)
@total_ordering
@dataclass
class Car:
    mark: str
    vin: str
    engine_capacity: float
    cost: float
    average_speed: float
    
    # магический метод - меньше <
    def __lt__(self, other: Self) -> bool:
        return self.cost < other.cost
    
    # магический метод - равно ==
    def __eq__(self, other: Self) -> bool:
        return self.cost == other.cost
    
    # магический метод - сложение +
    def __add__(self, other: Self) -> float:
        return self.cost + other.cost
    
    # магический метод - вычитание -
    def __sub__(self, other: Self) -> float:
        return self.cost - other.cost
    
    # магический метод - умножение *
    def __mul__(self, other: Self) -> float:
        return self.cost * other.cost
    
    # магический метод - деление //
    def __truediv__(self, other: Self) -> float:
        return self.cost / other.cost
    
    # магический метод - деление на цело //
    def __floordiv__(self, other: Self) -> float:
        return self.cost // other.cost
    
    # магический метод - вывода
    def __str__(self) -> str:
        return f"{self.mark} | {self.cost}"


# 10 раличных модель машин (10 элементов для дерева) 
element = [
    Car("Toyota", "JTJHY00W004036549", 10, 2_000_000, 150),
    Car("Lexus", "JTJHT00W604011511", 20, 2_104_000, 140),
    Car("Hyundai", "KMFGA17PPDC227020", 15, 3_003_000, 160.8),
    Car("Haval", "LGWFF4A59HF701310", 10.5, 2_500_000, 110.5),
    Car("Jeep", "1J8GR48K25C547741", 12.3, 2_111_000, 120),
    Car("Chery", "LVVDB11B6ED069797", 8, 1_800_500, 123),
    Car("Ford", "1FACP42D3PF141464", 30, 4_003_900.5, 180),
    Car("Tesla", "5YJ3E1EA8KF331791", 24.3, 3_060_000, 161.4),
    Car("Lada", "XTAKS0Y5LC6599289", 16, 2_044_000, 160),
    Car("Ravon", "XWBJA69V9JA004308", 18.2, 3_000_000, 152)
]