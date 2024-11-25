# import sys
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
from temp.car import Car
from temp.book import Book
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
    
    # Сортировка вставками - по возрастанию для Car - VIN
    def sort_insertion(self) -> None:
        # если массив пуст, то ничего не делается
        if self.length <= 0:
            return
        # проверка на тип - если класс Машина, то задаём основное значение - vin
        if type(self.arr[0]) == Car:
           for i in range(self.length):
                self.arr[i].set_flag("vin")
        # от 0 до длинны массива, i - индекс значения, который будем вставлять
        for i in range(self.length):
            # вставка self.arr[i] за j - индексом значения, отсчёт идет справа налево
            for j in range(i - 1, -1, -1):
                # Вставка происходит если значение индекса i будет меньше значение индекса j вместе с (вставка в начало j == 0 или если соседнее значение меньше чем вставляемое значение)
                if self.arr[i] < self.arr[j] and (j == 0 or self.arr[i] > self.arr[j - 1]):
                    # Вставка значения - копия в нужную позицию
                    self.insert(self.arr[i], j)
                    # Удаление значения со старой позиции
                    self.remove(i + 1)
                    # выходим из цикла, так как вставка уже произошла
                    break
    
    # Сортировка расчёской - по убыванию для Car - средняя скорость
    def sort_comb(self) -> None:
        # если массив пуст, то ничего не делается
        if self.length <= 0:
            return
        # проверка на тип - если класс Машина, то задаём основное значение - средняя скорость
        if type(self.arr[0]) == Car:
            for i in range(self.length):
                self.arr[i].set_flag("speed")
        
        # Функция - меняет местами значения по индексам   
        def swap(ind1: int, ind2: int) -> None:
            self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]
        
        # коэффицент разрыва
        k = 1.3
        # разрыв
        size = self.length
        # пока разрыв больше одного, то сортировка продолжается (разрыв = 1 в цикле присутствует)
        while size > 1:
            # задаём разрыв
            size = int(size // k)
            # идёт сортировка с диапазоном разрыва от 0 до длина массива - разрыв
            for i in range(self.length - size):
                # если значение меньше, то меняем местами
                if self.arr[i] < self.arr[i + size]:
                    swap(i, i + size)
    
    # Рекурсивная Сортировка быстрая - по возрастанию для Book - кол-во страниц
    def rec_sort_quick(self, start: int, end: int) -> None:
        # рекурсия идёт, пока конец меньше начала диапазона сортировки
        if start < end:
            # опорная точка - конец (от отобранного диапазона)
            pivot = self.arr[end]
            # less на сколько сдвинулась опорная точка влево
            less = 0
            for i in range(start, end):
                # если опорная точка меньше элемента то элемент ставим в конец диапазона end
                if pivot < self.arr[i - less]:
                    # удаляем элемент для переноса в конец диапазона
                    elem = self.remove(i - less)
                    # вставка элемента вправо в конец диапазона
                    self.insert(elem, end)
                    # сдвиг опорной точки влево + 1
                    less += 1
            # end - less = индекс опорной точки (она стоит на месте), рекурсия продолжается с левой и правой сторонной опорной точки
            self.rec_sort_quick(start, end - less - 1)
            self.rec_sort_quick(end - less + 1, end)
        
    # Сортировка быстрая - по возрастанию для Book - кол-во страниц
    def sort_quick(self) -> None:
        # если массив пуст, то ничего не делается
        if self.length <= 0:
            return
        # проверка на тип - если класс Книга, то задаём основное значение - кол-во страниц
        if type(self.arr[0]) == Book:
            for i in range(self.length):
                self.arr[i].set_flag("pages")
        # рекурсия быстрой сортировки
        self.rec_sort_quick(0, self.get_length() - 1)
    
    # Сортировка по основанию - по убыванию для Book - стоимость
    def sort_radix(self) -> None:
        # если массив пуст, то ничего не делаем
        if self.length <= 0:
            return
        # проверка на тип - если класс Книга, то задаём основное значение - стоимость
        if type(self.arr[0]) == Book:
            for i in range(self.length):
                self.arr[i].set_flag("cost")
        # сортировка по десятичной системе от 0 до 9 (включительно) - список из списков 
        nums = [[] for _ in range(10)]
        # новый массив для сортировки - копия 
        new_arr: ctypes.Array[T] = (self.length * ctypes.py_object)()
        for i in range(self.get_length()):
            new_arr[i] = self.get(i)
        # максимальная длина целого числа в массиве
        countmx = len(str(max(new_arr, key=lambda x: len(str(x)))))
        # от 0 до максимальной длины - сколько разрядов должен пройти для сортировки
        for round in range(countmx):
            # сортировка одного из разрядов (round) целых чисел 
            for i in new_arr:
                # значение - целое число
                flag = str(i)
                # если разряда нету (привышен), то считаем его за ноль
                if len(flag) >= round + 1:
                    # индекс разряда (начиная с конца целого числа)
                    index = (len(flag) - 1) - round
                    # добавляем в список десятичной системы 
                    nums[(len(nums) - 1) - int(flag[index])] += [i]
                else:
                    nums[len(nums) - 1] += [i]
            # счётчик индекса массива
            index = 0
            # заменяем отсортированные значения
            for i in nums:
                for j in i:
                    new_arr[index] = j
                    index += 1
            # очищяем список сортировки
            nums.clear()
            nums = [[] for _ in range(10)]
        # добавляем в основной массив отсортированные значения
        for i in range(self.length):
            self.arr[i] = new_arr[i]
    
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


# m = Array(15)
# element = [1, 3, 6, 5, 4, 10, 9, 7, 2, 8]


# for i in element:
#     m.append(i)
# # print(str([i.vin for i in m]))
# print(m)
# # m.insert(element[9], 0)
# m.sort_insertion()
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