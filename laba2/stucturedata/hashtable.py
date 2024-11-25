from typing import Generic, Optional, TypeVar, Iterator
from dataclasses import dataclass
from simplelinkedlists import SimpleLinkedList

# key - ключ
K = TypeVar("K")
# value - значение
V = TypeVar("V")

# класс для хранение ключа и значения,
@dataclass
class KV(Generic[K, V]):
    key: K
    value: V

# Хэш-таблица, принимает вместимость
class HashTable(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        # вместимость
        self.capacity = capacity
        # Односвязный список с узлами вместо индексов
        # - хранит либо ничего None либо Односвязный список из Узлов
        self.table: SimpleLinkedList[Optional[SimpleLinkedList[Optional[KV[K, V]]]]] = SimpleLinkedList()
        # заполняем хэш-таблицу пустотой
        for _ in range(capacity):
            self.table.push_tail(None)

    # генерируем хэш для ключа
    def hash(self, key: K) -> int:
        h = hash(key)
        # равное распределение ключа по хэшу (зависит от вместимости)
        return h % self.capacity

    # магический метод для назначения к ключу (хэш-ключу) - значение
    def __setitem__(self, key: K, value: V) -> None:
        # создаём хэш-ключ
        index: int = self.hash(key)
        # начальная позиция хэш-таблицы (односвязного списка)
        node = self.table.head
        # доходим до позиции хэш-ключа (индекс)
        for _ in range(index - 1):
            node = node.next
        # если пусто, то создаём новый Односвязный список
        if node.data is None:
            node.data = SimpleLinkedList()
            
        # проверяем есть ли в списке ещё ключи
        node_into = node.data.head
        while node_into is not None:
            # если нашёлся ключ, то вписываем в него значение
            if node_into.data.key == key:
                node_into.data.value = value
                return
            node_into = node_into.next
        # если не нашёлся, то создаём новый ключ со значением
        node.data.push_tail(KV(key, value))

    # магический метод получения значения по ключу
    def __getitem__(self, key: K) -> Optional[V]:
        # создаём хэш-ключ
        index: int = self.hash(key)
        node = self.table.head
        # доходим до позиции хэш-ключа (индекс)
        for _ in range(index - 1):
            node = node.next
        # если нету хэш-ключа, то возвращаем None
        if node.data is None:
            return None
        # перебераем ключи
        node_into = node.data.head
        while node_into is not None:
            # если ключ найден, то возвращаем его значение
            if node_into.data.key == key:
                return node_into.data.value
            node_into = node_into.next
        # если нету ключа в хэш-ключе, то возвращаем None
        return None

    # удаление ключа
    def remove(self, key: K) -> bool:
        index: int = self.hash(key)
        node = self.table.head
        # доходим до позиции хэш-ключа (индекс)
        for _ in range(index - 1):
            node = node.next
        # если нету хэш-ключа - то не удаляет
        if node.data is None:
            return False
        node_into = node.data.head
        # счётчик индекса (позиция ключа)
        length = 0
        # перебор ключей из хэш-ключа
        while node_into is not None:
            # если есть ключ то удаляется
            if node_into.data.key == key:
                # удаление из Односвязного списка Узел с ключём
                node.data.remove(length)
                # если теперь в хэш-ключе пусто, то назначаем None
                if node.data.head is None:
                    node.data = None
                # удаленно успешно
                return True
            node_into = node_into.next
            length += 1
        # не удаленно
        return False
    
    # возвращает список ключей
    def keys(self) -> list[K]:
        keys: list[K] = []
        # it - Узлы хэш-таблицы
        for it in self.table:
            # если пусто, то ищем дальше хэш-ключ
            if it.data is None:
                continue 
            node = it.data.head
            # добавляем ключи в список
            while node is not None:
                keys += [node.data.key]
                node = node.next
        return keys

    # возвращает список значений
    def values(self) -> list[V]:
        value: list[V] = []
        # it - Узлы хэш-таблицы
        for it in self.table:
            # если пусто, то ищем дальше хэш-ключ
            if it.data is None:
                continue 
            node = it.data.head
            # добавляем значения ключей в список
            while node is not None:
                value += [node.data.value]
                node = node.next
        return value

    # полная очистка хэш-таблицы
    def clear(self) -> None:
        self.table: SimpleLinkedList[Optional[KV[K, V]]] = SimpleLinkedList()
        for _ in range(self.capacity):
            self.table.push_tail(None)
    
    # магический метод нахождения ключа (есть ли ключ в Хэш-таблице)
    def __contains__(self, key: K) -> bool:
        return self.__getitem__(key) is not None
    
    # магический метод итерирования - при итерировании будет возвращать ключ
    def __iter__(self) -> Iterator[K]:
        for key in self.keys():
            yield key
    
    # магический метод вывода класса хэш-таблицы
    def __str__(self) -> str:
        return str(self.table)
