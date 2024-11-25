# если из другой папки то меняем путь для библиотеки структур данных
# import sys
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from structuredata.minheap import MinHeap
from typing import Self, Optional
from dataclasses import dataclass
from functools import total_ordering

# дополняет недостающие методы за счёт других (изменятся >=, <=, !=, >)
@total_ordering
@dataclass
class Car:
    mark: str
    vin: str
    engine_capacity: int
    cost: int
    average_speed: float
    
    # флаг - переключатель основного параметра - по умолчанию cost
    def __post_init__(self) -> None:
        self.flag = "cost"
    
    # задать основной параметр
    def set_flag(self, text: str) -> None:
        if text in ["mark", "vin", "capacity", "cost", "speed"]:
            self.flag = text
    
    # получить основной параметр или получить параметр
    def get_flag(self, text: Optional[str] = None) -> str | float:
        tx = self.flag
        if text is not None:
            tx = text
        if tx == "mark":
            return self.mark
        elif tx == "vin":
            return self.vin
        elif tx == "capacity":
            return self.engine_capacity
        elif tx == "cost":
            return self.cost
        elif tx == "speed":
            return self.average_speed
        return self.cost
    
    # магический метод - меньше <
    def __lt__(self, other: Self) -> bool:
        other_any = other.get_flag(self.flag)
        return self.get_flag() < other_any
    
    # магический метод - равно ==
    def __eq__(self, other: Self) -> bool:
        other_any = other.get_flag(self.flag)
        return self.get_flag() == other_any
    
    # магический метод - сложение +
    def __add__(self, other: Self) -> str | float:
        other_any = other.get_flag(self.flag)
        return self.get_flag() + other_any
    
    # магический метод - вычитание -
    def __sub__(self, other: Self) -> float:
        other_any = other.get_flag(self.flag)
        return self.get_flag() - other_any
    
    # магический метод - умножение *
    def __mul__(self, other: Self) -> str | float:
        other_any = other.get_flag(self.flag)
        return self.get_flag() * other_any
    
    # магический метод - деление /
    def __truediv__(self, other: Self) -> float:
        other_any = other.get_flag(self.flag)
        return self.get_flag() / other_any
    
    # магический метод - деление на цело //
    def __floordiv__(self, other: Self) -> int | float:
        other_any = other.get_flag(self.flag)
        return self.get_flag() // other_any
    
    # магический метод - вывода
    def __str__(self) -> str:
        return str(self.get_flag())
    
    # магический метод предназначен для машинно-ориентированного вывода
    def __repr__(self) -> str:
        return str(self.get_flag())

# 10 раличных модель машин (10 элементов для дерева) 
element = [
    Car("Toyota", "JTJHY00W004036549", 10, 2_000_000, 150),
    Car("Lexus", "JTJHT00W604011511", 20, 2_104_000, 140),
    Car("Hyundai", "KMFGA17PPDC227020", 15, 3_003_000, 160.8),
    Car("Haval", "LGWFF4A59HF701310", 10, 2_500_000, 110.5),
    Car("Jeep", "1J8GR48K25C547741", 12, 2_111_000, 120),
    Car("Chery", "LVVDB11B6ED069797", 8, 1_8000_500, 123),
    Car("Ford", "1FACP42D3PF141464", 30, 4_003_900, 180),
    Car("Tesla", "5YJ3E1EA8KF331791", 24, 3_060_000, 161.4),
    Car("Lada", "XTAKS0Y5LC6599289", 16, 2_044_000, 160),
    Car("Ravon", "XWBJA69V9JA004308", 18, 3_900_000, 152)
]
