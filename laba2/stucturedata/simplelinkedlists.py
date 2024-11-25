from typing import Generic, Optional, TypeVar, Iterator
from dataclasses import dataclass


T = TypeVar("T")

# класс Узла для ОдносвязногоСписка,
# в котором хранится элемент и ссылка на None или на следующий Узел
@dataclass
class Node(Generic[T]):
    data: T
    next: Optional['Node[T]'] = None
    

class SimpleLinkedList(Generic[T]):
    # две основные переменные:
    # голова (начальный Узел) и хвост (конечный Узел)
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
    
    # возвращает длинну Односвязного списка
    def get_length(self) -> int:
        length: int = 0
        node = self.head
        # если пусто то 0
        if node is None:
            return 0
        # засчитываем каждый Узел
        while node is not None:
            node = node.next
            length += 1
        return length
    
    # возвращает True если индекс есть в Списке, False - Нету
    def check_range(self, index: int) -> bool:
        length = self.get_length()
        # Если 0, то пусто
        if length == 0:
            return False
        # Если индекс меньше длинны и больше или равно нулю, то True, иначе - False
        return 0 <= index < length
    
    # вставка в начало
    def push_head(self, data: T) -> None:
        # создаем новый Узел с ссылкой на прошлый начальный Узел
        self.head = Node(data, self.head)
        # Если список пуст, то к хвосту присваивается тот же новый Узел
        if self.tail is None:
            self.tail = self.head
     
    # вставка в конец    
    def push_tail(self, data: T) -> None:
        # Если список не пуст, то добавляем к хвосту ссылку и назначаем новых хвост на новый Узел
        if self.head is not None:
            self.tail.next = Node(data, None)
            self.tail= self.tail.next
        else:
            # иначе если пуст, то начало и конец равны
            self.head = Node(data, None)
            self.tail = self.head
    
    # вставка по индексу, задаётся индекс туда, там и будет стоять новый Узел   
    def insert(self, index: int, data: T) -> None:
        # если в начало, то воспользуемся методом push_head
        if index == 0:
            self.push_head(data)
            return
        elif index == self.get_length():
            # если в конец, то воспользуемся методом push_tail
            self.push_tail(data) 
            return
        elif not self.check_range(index):
            # выдаёт ошибку, если индекс вне диапазона списка
            raise IndexError("Index is outside the range of the SingleLinkedList")

        node = self.head
        for _ in range(index - 1):
            node = node.next
        # добавляем новый Узел 
        node.next = Node(data, node.next)
    
    # получить Узел по индексу
    def get_node(self, index: int) -> Optional[Node[T]]:
        if not self.check_range(index):
            raise IndexError("Index is outside the range of the SingleLinkedList")
        # поиск значения 
        node = self.head
        for _ in range(index):
            node = node.next
        return node
    
    # получить значение по индексу
    def get(self, index: int) -> Optional[T]:
        return self.get_node(index).data
    
    # удаление Узла по индексу
    def remove(self, index: int) -> None:
        # проверка индекса
        if not self.check_range(index):
            raise IndexError("Index is outside the range of the SingleLinkedList")
        elif index == 0:
            # Если в начало, то сохраняем ссылку головы в саму голову
            self.head = self.head.next
            # Если же список теперь пуст, то в хвосте тоже должно быть пусто
            if self.head == None:
                self.tail = None
            return
        
        # удаление Узла по индексу
        node = self.head
        for _ in range(index - 1):
            node = node.next
        
        # Если удаляется конечный Узел (хвост), то нужно перезаписать хвост на предпоследний Узел
        if index == self.get_length() - 1:
            self.tail = node
        # Присваиваем к Узлу по index - 1 ссылку на Узел по index + 1 
        node.next = node.next.next
    
    # очистка (пустой список)
    def clear(self) -> None:
        self.head = None
        self.tail = None
    
    # магический метод итерирования - возвращает Узел
    def __iter__(self) -> Iterator[Optional[Node[T]]]:
        for i in range(self.get_length()):
            yield self.get_node(i)
    
    # магический метод вывода класса односвязного списка в формате [знач1, знач2, ... знач N]
    def __str__(self) -> str:
        text = ""
        for i in range(self.get_length()):
            text += str(self.get(i)) + ", "
        if text == "":
            return "[]"
        return f"[{text[:-2]}]"
    
    # магический метод предназначен для машинно-ориентированного вывода
    def __repr__(self) -> str:
        return self.__str__()
