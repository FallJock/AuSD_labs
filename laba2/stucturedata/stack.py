from typing import TypeVar, Generic
from doublelinkedlists import DoubleLinkedList
from dataclasses import dataclass


T = TypeVar("T")


# ошибка если вместимость Стэка мала
class SizeIsOver(Exception):
    pass


# ошибка если при просмотре значения, а Стэк пуст 
class EmptyStack(Exception):
    pass


# Стэк принимает размер (вместимость)
class Stack(Generic[T]):
    # класс хранит - данную длинну, вместимость и Двусвязный список
    def __init__(self, size: int) -> None:
        self.length: int = 0
        self.size: int = size
        self.arr: DoubleLinkedList[Generic[T]] = DoubleLinkedList()

    # возвращает нынешную длинну
    def get_size(self) -> int:
        return self.length

    # Стэк пуст?
    def is_empty(self) -> bool:
        return self.length == 0

    # Вставляет значение на верхушку Двусвязного списка
    def push(self, value: T):
        if self.get_size() >= self.size:
            raise SizeIsOver(f"Size of Stack is over: {value}")
        self.arr.push_head(value)
        self.length += 1

    # Удаляет значение с верхушки Двусвязного списка
    def pop(self) -> T:
        if self.is_empty():
            raise EmptyStack("Stack is empty")
        self.length -= 1
        return self.arr.remove(0)
    
    # Возвращает значение верхушки Двусвязного списка
    def peak(self) -> T:
        if self.is_empty():
            raise EmptyStack("Stack is empty")
        return self.arr.get(0)
    
    # Вывод значений
    def __str__(self) -> str:
        return str(self.arr)
