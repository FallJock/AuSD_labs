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
class Book:
    author: str
    publisher: str
    pages: int
    cost: int
    isbn: int
    
    # флаг - переключатель основного параметра - по умолчанию cost
    def __post_init__(self) -> None:
        self.flag = "cost"
    
    # задать основной параметр
    def set_flag(self, text: str) -> None:
        if text in ["author", "publisher", "pages", "cost", "isbn"]:
            self.flag = text
    
    # получить основной параметр или получить параметр
    def get_flag(self, text: Optional[str] = None) -> str | float:
        tx = self.flag
        if text is not None:
            tx = text
        if tx == "author":
            return self.author
        elif tx == "publisher":
            return self.publisher
        elif tx == "pages":
            return self.pages
        elif tx == "cost":
            return self.cost
        elif tx == "isbn":
            return self.isbn
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
    def __add__(self, other: Self) -> str | int | float:
        other_any = other.get_flag(self.flag)
        return self.get_flag() + other_any
    
    # магический метод - вычитание -
    def __sub__(self, other: Self) -> int | float:
        other_any = other.get_flag(self.flag)
        return self.get_flag() - other_any
    
    # магический метод - умножение *
    def __mul__(self, other: Self) -> str | int | float:
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
element_book = [
    Book("Л. Н. Толстой", "Эксмо", 1000, 472, 9785699120147),
    Book("О. Л. Ершова", "Эксмо", 520, 473, 9785699867935),
    Book("Роберт Джордан", "Азбука", 33, 401, 9785677520647),
    Book("В. Д. Афиногенов", "Вече", 45, 277, 9785697425819),
    Book("Люси Мод Монтгомери", "Азбука", 145, 370, 9785696450122),
    Book("М. Ю. Лермонтов", "Азбука", 76, 320, 9785699224456),
    Book("Н. Н. Телепова", "Эксмо", 80, 250, 9785693322112),
    Book("С. Н. Зигуненко", "Вече", 60, 501, 9785664550121),
    Book("И. Е. Забелин", "Азбука", 120, 399, 9785693124755),
    Book("В. Д. Афиногенов", "Вече", 230, 410, 9785699673146)
]


