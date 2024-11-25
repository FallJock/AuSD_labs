
# прыжковый поиск на прыжковом поиске
    # def search_jump(self, elem:T) -> int:
    #     if not self.is_sorted():
    #         raise ValueError("The value does not exist in this array")
        
    #     # диапазон, в котором будет поиск через скачки
    #     left, right = 0, self.get_length()
    #     # расстояние через, которое перепрыгнет
    #     jump = self.get_length()
    #     # пока left не дойдёт до конца или шаг прышка не будет 1 (в цикле только 1 круг пройдёт с шагом 1)
    #     while left < self.get_length() and jump > 1:
    #         # шаг прыжка - корень от шага прыжка
    #         jump = int(jump ** 0.5)
    #         # если левая часть равна, то возвращаем (чтобы если после прыжка индекс стал меньше, можно было вернуться назад i - jump)
    #         if self.arr[left] == elem:
    #             return left
    #         # выполняем прыжки и сравнения
    #         for i in range(left + jump, right, jump):
    #             # если равен, то нашли
    #             if elem == self.arr[i]:
    #                 return i
    #             # если больше, то берём отрезок от предыдущего прыжка до нынешнего + 1 (выход из цикла)
    #             elif elem > self.arr[i]:
    #                 left = i - jump
    #                 right = i + 1
    #                 break
    #     # если не нашёл, то -1
    #     return -1


# import sys
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# # ======================
# from temp.car import Car, element
# from temp.book import Book, element_book
import ctypes
from typing import Generic, TypeVar, Iterator

T = TypeVar("T")

class Array(Generic[T]):
    # основная переменная - вместимость массива:
    def __init__(self, capacity: int) -> None:
        self.length: int = 0
        self.capacity: int = capacity
        # создаём массив на основе Cи
        self.arr: ctypes.Array[T] = (capacity * ctypes.py_object)()
    
    # возвращает длину
    def get_length(self) -> int:
        return self.length
    
    # возвращает вместимость
    def get_capacity(self) -> int:
        return self.capacity
    
    # получить значение по индексу
    def get(self, index: int) -> T:
        # если индекс вне диапазона длины массива, то ошибка
        if index >= self.get_length() or index < 0:
            raise "Index is out of range"
        return self.arr[index]
    
    # магический метод - получение значения по индексу
    def __getitem__(self, index: int) -> T:
        # если индекс вне диапазона длины массива, то ошибка
        if index >= self.get_length() or index < 0:
            raise "Index is out of range"
        return self.arr[index]
    
    # выделяем больше места в массиве (увеличивает вместимость)
    def expand_capacity(self, cap: int) -> None:
        size = cap
        if size <= 0:
            size = 1
        # создаёт новый массив с новой вместимостью
        new_arr: ctypes.Array[T] = (size * ctypes.py_object)()
        # передаются все значения прошлого массива
        for i in range(self.get_length()):
            new_arr[i] = self.get(i)
        # передаём новые данные массив и вместимость
        self.arr: ctypes.Array[T] = new_arr
        self.capacity = size
    
    # добавляет в конец массива элемент
    def append(self, elem: T) -> None:
        # если вместимость кончается, то увеличиваем
        if self.length == self.capacity:
            self.expand_capacity(self.capacity * 2)
        # добавляем элемент
        self.arr[self.length] = elem
        self.length += 1
    
    # вставляет элемент на заданную позицию в массив
    def insert(self, elem: T, index: int) -> None:
        if index > self.length or index < 0:
            raise "Index is out of range"
        # если вместимость кончается, то увеличиваем
        if self.length == self.capacity:
            self.expand_capacity(self.capacity * 2)
        for i in range(self.length, index - 1, -1):
            if index == 0 and i - 1 < 0:
                self.arr[0] = elem
                continue
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = elem
        self.length += 1
        
    # Магический метод замены значения по индексу
    def __setitem__(self, index: int, elem: T) -> None:
        # если индекс вне диапазона длины массива, то ошибка
        if index >= self.get_length() or index < 0:
            raise "Index is out of range"
        self.arr[index] = elem
    
    # удаление по индексу - возвращает удалённый элемент
    def remove(self, index: int) -> T:
        # проверка индекса
        if index >= self.get_length() or index < 0:
            raise "Index is out of range"
        
        elem: T = self.get(index)
        # сдвиг значений по индексам плево на 1 шаг от индекса до длины - 1
        for i in range(index, self.get_length() - 1):
            self.arr[i] = self.arr[i + 1]
            
        self.length -= 1
        return elem

    # очистка (пустой массив)
    def clear(self) -> None:
        self.length = 0
        self.arr: ctypes.Array[T] = (self.capacity * ctypes.py_object)()
    
    # Сортировка вставками - по убыванию
    def sort_insertion(self) -> None:
        # если массив пуст, то ничего не делается
        if self.length <= 0:
            return
        # от 0 до длинны массива, i - индекс значения, который будем вставлять
        for i in range(self.length):
            # вставка self.arr[i] за j - индексом значения, отсчёт идет справа налево
            for j in range(i - 1, -1, -1):
                # Вставка происходит если значение индекса i будет больше значение индекса j вместе с (вставка в начало j == 0 или если соседнее значение больше чем вставляемое значение)
                if self.arr[i] > self.arr[j] and (j == 0 or self.arr[i] < self.arr[j - 1]):
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    break
    
    # Проверка - отсортирован ли массив по убыванию
    def is_sorted(self) -> bool:
        for i in range(self.length - 1):
            if self.arr[i] < self.arr[i + 1]:
                return False
        return True
    
    # Алгоритм бинарного поиска (условие - сортировка по убыванию), если не нашёлся элемент то возвращает -1
    def search_binary(self, elem:T) -> int:
        # Проверка отсортированности массива. если нет, то выдаёт исключение
        if not self.is_sorted():
            raise ValueError("Array is not sorted")
        
        # диапазон [левый индекс, правый индекс]
        left, right = 0, self.get_length() - 1
        # пока правый индекс больше или равно левого индекса, то продолжает искать
        while right >= left:
            # индекс центра (деление на цело - округляет в меньшую сторону)
            center = (right + left) // 2
            # если значение больше центрального, то берём левую сторону от центра
            if elem > self.arr[center]:
                right = center - 1
            elif elem < self.arr[center]:
                # если значение меньше центрального, то берём правую сторону от центра
                left = center + 1
            else:
                # иначе - нашёл и возвращет индекс значения
                return center
        # если не нашёл, то -1
        return -1
    
    # Алгоритм скачкообразного поиска (условие - сортировка по убыванию), если не нашёлся элемент то возвращает -1
    def search_jump(self, elem:T) -> int:
        # Проверка отсортированности массива. если нет, то выдаёт исключение
        if not self.is_sorted():
            raise ValueError("Array is not sorted")
        
        # диапазон, в котором будет поиск через скачки
        left, right = 0, self.get_length()
        # шаг прыжка - корень от шага прыжка
        jump = int(self.get_length() ** 0.5)
        # если левая часть равна, то возвращаем (чтобы если после прыжка индекс стал меньше, можно было вернуться назад i - jump)
        if self.arr[left] == elem:
            return left

        # выполняем прыжки и сравнения
        for i in range(left + jump, right, jump):
            # если равен, то нашли
            if elem == self.arr[i]:
                return i
            # если больше, то берём отрезок от предыдущего прыжка до нынешнего (выход из цикла)
            elif elem > self.arr[i]:
                left = i - jump
                right = i
                break
        else:
            # чтобы с начало не начинать линеный поиск, с последнего прыжка до конца
            left = i
            
        # линейный поиск с предыдущего прыжка до последнего прыжка / или последний прыжок до конца (если прыжки дошли до конца)
        for i in range(left, right):
            if elem == self.arr[i]:
                return i
        # если не нашёл, то -1
        return -1
    
    # магический метод итерирования - возвращает значение
    def __iter__(self) -> Iterator[T]:
        for i in range(self.get_length()):
            yield self.get(i)
    
    # магический метод вывода класса массива в формате [знач1, знач2, ... знач N]
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


    #  ==================================================
    def search_jump_n(self, elem:T) -> int:
        if not self.is_sorted():
            raise ValueError("The value does not exist in this array")
        
        # диапазон, в котором будет поиск через скачки
        left, right = 0, self.get_length()
        # расстояние через, которое перепрыгнет
        jump = self.get_length()
        # пока left не дойдёт до конца или шаг прышка не будет 1 (в цикле только 1 круг пройдёт с шагом 1)
        while left < self.get_length() and jump > 1:
            # шаг прыжка - корень от шага прыжка
            jump = int(jump ** 0.5)
            # если левая часть равна, то возвращаем (чтобы если после прыжка индекс стал меньше, можно было вернуться назад i - jump)
            if self.arr[left] == elem:
                return left
            # выполняем прыжки и сравнения
            for i in range(left + jump, right, jump):
                # если равен, то нашли
                if elem == self.arr[i]:
                    return i
                # если больше, то берём отрезок от предыдущего прыжка до нынешнего + 1 (выход из цикла)
                elif elem > self.arr[i]:
                    left = i - jump
                    right = i + 1
                    break
        # если не нашёл, то -1
        return -1
    
    
# m = Array(15)
# b = Array(15)
# # element = [1, 3, 6, 5, 4, 10, 9, 7, 2, 8]
# # element = list(range(1001))

# for i in element:
#     i.set_flag("vin")
#     m.append(i)

# for i in element_book:
#     i.set_flag("author")
#     b.append(i)
# # # print(str([i.vin for i in m]))
# # print(m)
# # # m.insert(element[9], 0)
# el = element[6]
# elb = element_book[6]

# # print(m.search_binary(el))
# # print(b.search_jump(elb))

# m.sort_comb()
# b.sort_comb()

# print(f"Search index of Car = {el}")
# print(m)
# print(f"\nindex of Car = {m.search_jump(el)}")


# print(f"\n\nSearch index of Book = {elb}")
# print(b)
# print(f"\nindex of Book = {b.search_jump(elb)}")
# for i in element:
#     nnn = m.search_jump(i)
#     print(f"{i} =", nnn)
#     print()
#     if m[nnn] != i:
#         raise ValueError


# print(m.search_binary(11))
# # m.insert(element_book[1], 3)
# # m.insert(element_book[1], 3)
# # # print(int(float("0.61")))
# # # print("444 444".isdigit())
# # m.insert(element_book[1], 12)
# print(m)



# print(m)
# # m.sort_radix()
# # print(m)
# # print("\n".join([str(i.cost) for i in m]))