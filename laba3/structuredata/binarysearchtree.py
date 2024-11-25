# import sys
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
from temp.car import Car
import json
from typing import Generic, Optional, TypeVar
from dataclasses import dataclass

T = TypeVar("T")

# класс Узла для Двоичного дерева поиска,
# в котором хранится элемент и ссылки на None или на левый и правый Узел
@dataclass
class Node(Generic[T]):
    key: T
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None


# Класс Двоичного дерева поиска
class BinarySearchTree(Generic[T]):
    # Хранит путь (начальный узел) Двоичного дерева поиска
    def __init__(self) -> None:
        self.root: Optional[Node[T]] = None 
    
    # Вставка по ключу
    def insert(self, key: T) -> None:
        # если пусто, то создаём узел
        if self.root is None:
            self.root = Node(key)
            return
        root = self.root
        while root is not None:
            if key == root.key:
                return
            # если в значение ключа больше то в правую ветвь
            if key > root.key:
                if root.right is None:
                    root.right = Node(key)
                    return
                root = root.right
            else:
                # иначе в значение ключа меньше то в левую ветвь
                if root.left is None:
                    root.left = Node(key)
                    return
                root = root.left
        return
    
    # Находит по ключу узел из Двоичного дерева поиска
    def find(self, key: T) -> Optional[Node[T]]:
        return self.recursive_find(self.root, key)
    
    # (Рекурсия) Возвращает узел по заданному пути ключа и ключу
    def recursive_find(self, root: Optional[Node[T]], key: T) -> Optional[Node[T]]:
        # если нету продолжения в узле ключа, возвращаем место, на котором остановились или если нашёл ключ
        if root is None or key == root.key:
            return root
        
        # рекурсия для прохождения по всем узлам если значение ключа больше чем у узле, то вправо иначе влево
        if key > root.key:
            return self.recursive_find(root.right, key)
        return self.recursive_find(root.left, key)
    
    # (Рекурсия) Возвращает предыдущий узел ключа (который имеет ссылку на ключ) и True|False (флаг) для понимания справа или слева 
    def recursive_prefind(self, root: Optional[Node[T]], key: T) -> tuple[Optional[Node[T]], bool]:
        # если нету продолжения в узле ключа, возвращаем место, на котором остановились или если ключ равен (если выбран начальный ключ)
        if root is None or key == root.key:
            return root, False
        # Если у предыдущего ключа справа ключ, то возвращаем узел и True (ключ справа)
        if root.right is not None and key == root.right.key:
            return root, True
        # Если у предыдущего ключа слева ключ, то возвращаем узел и False (ключ слева)
        if root.left is not None and key == root.left.key:
            return root, False
        
        # рекурсия для прохождения по всем узлам если значение ключа больше чем у узле, то вправо иначе влево
        if key > root.key:
            return self.recursive_prefind(root.right, key)
        return self.recursive_prefind(root.left, key)
    
    # Возвращает максимальное значение из узел Двоичного дерева поиска
    def max(self) -> Optional[T]:
        return self.get_max(self.root)
    
    # Возвращает минимальное значение из узел Двоичного дерева поиска
    def min(self) -> Optional[T]:
        return self.get_min(self.root)
    
    # Возвращает с заданным путём(узлом) максимальное значение из узел (по правой ветке)
    def get_max(self, xroot: Optional[Node[T]]) -> Optional[T]:
        root = xroot
        if root is None:
            return
        while root.right is not None:
            root = root.right
        return root.key
    
    # Возвращает с заданным путём(узлом) минимальное значение из узел (по левой ветке)
    def get_min(self, xroot: Optional[Node[T]]) -> Optional[T]:
        root = xroot
        if root is None:
            return
        while root.left is not None:
            root = root.left
        return root.key

    # Метод удаления по ключу
    def remove(self, key: T) -> None:
        # находим узел ключа
        root = self.find(key)
        # если не был найден, то прекращаем удаление
        if root is None:
            return
        # предыдущий узел, справа? (да/нет)
        pre_root, is_right = self.recursive_prefind(self.root, key)
        # у узла есть ветвления влево, вправо?
        left, right = root.left is not None, root.right is not None
        # нету слева и нету справа
        if not(left) and not(right):
            if pre_root == root:
                self.root = None
            # если ключ справа, иначе слева - присваиваем пустоту None
            if is_right:
                pre_root.right = None
            else:
                pre_root.left = None
        elif left and not(right):
            # (нету ветки справа) если ключ справа, иначе слева - присваиваем левую ветку узла
            if is_right:
                pre_root.right = root.left
            else:
                pre_root.left = root.left
        elif not(left) and right:
            # (нету ветки слева) если ключ справа, иначе слева - присваиваем правую ветку узла
            if is_right:
                pre_root.right = root.right
            else:
                pre_root.left = root.right
        else:
            # ветки есть слева и справа - ищем у узла по левой ветки его максимум, а по правой ветки его минимум
            mx, mn = self.get_max(root.left), self.get_min(root.right)
            # Минимальный ключ - Делаем сравнение по модулю (у кого разница меньше с значением ключа, того заменяем на место удаления)
            key_min = min([mx, mn], key=lambda x: abs(key - x))
            # Предыдущий узел минимального ключа, справа? (да/нет)
            pop_root, pop_is_right = self.recursive_prefind(root, key_min)
            
            # значение узла минимального ключа
            popkey: Optional[T] = None
            if pop_is_right:
                # присваиваем ключ для замены и чистим путь
                popkey = pop_root.right
                pop_root.right = None
            else:
                popkey = pop_root.left
                pop_root.left = None
            
            # делаем замену на другой ключ
            if popkey.right is not None:
                root.right = popkey.right
            if popkey.left is not None:
                root.left = popkey.left
            
            if root == pop_root:
                if pop_is_right:
                    mn = self.get_min(root.right)
                    if mn is not None:
                        ro = self.find(mn)
                        ro.left = popkey.left
                else:
                    mx = self.get_max(root.left)
                    if mx is not None:
                        ro = self.find(mx)
                        ro.right = popkey.right
            root.key = popkey.key
    
    # Шаг слева для метода рисования простого графика дерева (путь, шаг слева, список чисел шагов) - возвращает максимальный левый шаг
    def steps_left(self, root: Optional[Node[T]], step:int=0, m:list[int]=[]) -> int:
        if root is None:
            return max(m)
        m += [step]
        self.steps_left(root.right, step - 1, m)
        self.steps_left(root.left, step + 1, m)
        return max(m)
    
    # Рисует простой график дерева
    def graph_print_tree(self, root: Optional[Node[T]], step:int, n:int=0, k:int=0) -> Optional[Node[T]]:
        if root is None:
            return None
        # значение ключа
        tx = root.key.__str__()
        # шаг слева с табуляцией
        print(f"{(step - k) * "\t" } {n * "+"} [ {tx} ] {k * "-"}")
        self.graph_print_tree(root.left, step, n - 1, k + 1)
        self.graph_print_tree(root.right, step, n + 1, k - 1)
    
    # (возвращает список ключей) Предпоследовательный обход - обход начиная с корня сначала слева, а потом справа (сохраняет все значение ключей в список)
    def list_preorder_tree(self, root: Optional[Node[T]], n:list[T]=list()) -> list:
        if root is None:
            return n
        n += [root.key]
        self.list_preorder_tree(root.left, n)
        self.list_preorder_tree(root.right, n)
        return n
    
    # (возвращает список ключей) Последовательный обход - обход по порядку 
    def list_inorder_tree(self, root: Optional[Node[T]], n:list[T]=list()) -> list:
        if root is None:
            return n
        self.list_inorder_tree(root.left, n)
        n += [root.key]
        self.list_inorder_tree(root.right, n)
        return n
    
    # (возвращает список ключей) Последующий обход - обход сначала слева, а потом справа заканчивая корнем
    def list_postorder_tree(self, root: Optional[Node[T]], n:list[T]=list()) -> list:
        if root is None:
            return n
        self.list_postorder_tree(root.left, n)
        self.list_postorder_tree(root.right, n)
        n += [root.key]
        return n
    
    # Количество ключей
    def get_size(self) -> int:
        if self.root is None:
            return 0
        return len(self.list_preorder_tree(self.root, []))
    
    # Методы с приставкой print_ - выводы обходов
    def print_preorder_tree(self) -> None:
        spis = map(str, self.list_preorder_tree(self.root, []))
        print("Предпоследовательный обход: " + ", ".join(spis))
        
    def print_inorder_tree(self) -> None:
        spis = map(str, self.list_inorder_tree(self.root, []))
        print("Последовательный обход: " + ", ".join(spis))
        
    def print_postorder_tree(self) -> None:
        spis = map(str, self.list_postorder_tree(self.root, []))
        print("Последующий обход: " + ", ".join(spis))
    
    # Сохранение состояния Двоичного дерева поиска в json формате 
    def save(self, path: str) -> None:
        with open(path, "w", encoding="UTF-8") as file_save:
            json.dump(self.__dict__, file_save, ensure_ascii=False, default=str)
    
    # Загрузка состояния Двоичного дерева поиска в json формате        
    def load(self, path: str) -> None:
        with open(path, "r", encoding="UTF-8") as file_load:
            self.root = eval(json.load(file_load)["root"])
    
    # Графический вывод через магический метод
    def __str__(self) -> str:
        k = self.steps_left(self.root)
        self.graph_print_tree(self.root, k)
        return ""