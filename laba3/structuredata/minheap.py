# import sys
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
from temp.car import element, Car
import json
from typing import Generic, Optional, TypeVar
from .simplelinkedlists import SimpleLinkedList, Node
# from simplelinkedlists import SimpleLinkedList, Node

T = TypeVar("T")


# Минимальная куча с реализацией на Односвязном списке
class MinHeap(Generic[T]):
    # Хранит Односвязный список
    def __init__(self) -> None:
        self.list: SimpleLinkedList[Optional[Node[T]]] = SimpleLinkedList()
    
    # Возвращает количество узлов в Односвязном списке
    def get_size(self) -> int:
        return self.list.get_length()
    
    # Возвращает индекс(позицию) родителя по индексу
    @staticmethod
    def get_index_parent(index: int) -> int:
        # index = 2i + 2 (справа) иначе indez = 2i + 1 (слева)
        if index % 2 == 0:
            return (index - 2) // 2
        return (index - 1) // 2
    
    # Возвращает значение узла по индексу
    def get(self, index: int) -> Optional[T]:
        return self.list.get(index)
    
    # Меняет местами узлы по индексам (меняет их ссылки - next)
    def swap(self, index1: int, index2: int) -> None:
        # индексы родителей
        preind1 = index1 - 1
        preind2 = index2 - 1

        # если индексы равны или индекс отрицательный или индекс вышел из диапазона то ничего не меняется
        if index1 == index2 or index1 < 0 or index2 < 0 or max(index1, index2) > self.get_size() - 1:
            return 
        
        # Узлы по индексу
        node_1: Optional[Node[T]] = self.list.get_node(index1)
        node_2: Optional[Node[T]] = self.list.get_node(index2)

        # Если первый индекс это голова (начальный узел) - то заменяем голову на другой узел
        if preind1 < 0:
            pre_node_2: Optional[Node[T]] = self.list.get_node(preind2)
            pre_node_2.next = node_1
            node_1.next, node_2.next = node_2.next, node_1.next
            self.list.head = node_2 
        elif preind2 < 0:
            # Если второй индекс это голова (начальный узел) - то заменяем голову на другой узел
            pre_node_1: Optional[Node[T]] = self.list.get_node(preind1)
            pre_node_1.next = node_2
            node_1.next, node_2.next = node_2.next, node_1.next
            self.list.head = node_1
        else:
            pre_node_1: Optional[Node[T]] = self.list.get_node(preind1)
            pre_node_2: Optional[Node[T]] = self.list.get_node(preind2)
            
            pre_node_1.next = node_2
            pre_node_2.next = node_1
            node_1.next, node_2.next = node_2.next, node_1.next
        
        # Если индекс это хвост (конец) - то меняем на другой узел
        if self.get_size() - 1 == index2:
            self.list.tail = node_1
        elif self.get_size() - 1 == index1:
            self.list.tail = node_2
        return
    
    def heapify(self) -> None:
        # Количество всех родительских веток (ветки, которые имеют одного или двух детей)
        step = self.get_index_parent(self.get_size() - 1) + 1
        save = 0
        if step - 1 < 0:
            return
        while save != step:
            save = 0
            for i in range(step):
                # индексы (позиции) левого и правого
                left = 2 * i + 1
                right = 2 * i + 2
                if self.get(left) is None:
                    min_ind_data = right
                elif self.get(right) is None:
                    min_ind_data = left
                else:
                    min_ind_data = min([left, right], key=self.get) 
                    
                if self.get(min_ind_data) < self.get(i):
                    self.swap(min_ind_data, i)
                else:
                    save += 1
    
    # Вставка в конец и применяется heapify для упорядочивании в соответствии со свойствами кучи
    def insert(self, data: T) -> None:
        self.list.push_tail(data)
        self.heapify()
    
    # Удаляет минимальное значение (корень кучи) и применяется heapify для упорядочивании в соответствии со свойствами кучи
    def remove(self) -> Optional[T]:
        if self.get_size() == 0:
            return None
        delnode = self.list.head.data
        self.swap(0, self.get_size() - 1)
        self.list.remove(self.get_size() - 1)
        self.heapify()
        return delnode
    
    # Возвращает корень кучи (минимальное значение)
    def peek(self) -> Optional[T]:
        if self.get_size() == 0:
            return None
        return self.list.head.data
    
    # Проверяет есть ли такой элемент (возвращает True если да, иначе False)
    def find(self, data: T) -> bool:
        if self.get_size() == 0:
            return False
            # Возвращает индекс по значению узла
        for it in self.list:
            if it.data == data:
                return True
        return False
    
    # Сохранение состояния Двоичного дерева поиска в json формате 
    def save(self, path: str) -> None:
        with open(path, "w", encoding="UTF-8") as file_save:
            json.dump(self.list.head, file_save, ensure_ascii=False, default=str)
    
    # Загрузка состояния Двоичного дерева поиска в json формате        
    def load(self, path: str) -> None:
        with open(path, "r", encoding="UTF-8") as file_load:
            self.list.clear()
            self.list.head = eval(json.load(file_load))
            self.list.tail = self.list.get_node(self.get_size() - 1)
    
    # Магический метод вывода кучи
    def __str__(self) -> str:
        return self.list.__str__()



# heap.save("test.json")
# # print(heap.list.head)
# print(heap, heap.list.tail)
# heap.load("test.json")
# print(heap)
# print(heap.list.tail)