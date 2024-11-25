import json
from typing import List, Optional

# Класс - Граф на основе матрицы смежности
class Graph:
    # принимает - True|False (ориентированный граф или нет) и хранит матрицу
    def __init__(self, directed: bool = False) -> None:
        # матрица смежности
        self.adjacenc_matrix: List[List[Optional[int | float]]] = []
        # ориентированный - True | неориентированный - False (соединяется вершины с двух сторон)
        self.directed: bool = directed
    
    # возвращает длину N матрицы NxN
    def get_length(self) -> int:
        return len(self.adjacenc_matrix)
    
    # добавляет вершину
    def add_vertex(self) -> None:
        matrix = self.adjacenc_matrix
        # если пуст, то добавляем одну вершину
        if len(matrix) == 0:
            matrix.append([None])
            return
        # к каждой вершине добавляем место для новой вершины
        for el in matrix:
            el.append(None)
        # добавление новой вершины (учитывая количество вершин)
        matrix.append([None] * len(el))
    
    # добавляет ребро с весом от одной вершине к другой по индексам
    def add_edge(self, from_index: int, to_index: int, weight: int | float) -> bool:
        matrix = self.adjacenc_matrix
        # если индекс меньше 0 или превышает или равен колличество вершин или индексы равны
        if min(from_index, to_index) < 0 or max(from_index, to_index) >= len(matrix) or from_index == to_index:
            return False
        # если пуст или только одна вершина, то выход
        if len(matrix) < 2:
            return False
        
        # добавляем ребро от одной вершины к другой
        matrix[from_index][to_index] = weight
        # и наоборот добавляем от другой к одной вершине, если ненаправленный
        if not self.directed:
            matrix[to_index][from_index] = weight
        return True
    
    # возвращает список вершины, хранящий все вершины с которыми соединён и нет
    def get_vertex(self, index: int) -> Optional[List[Optional[int | float]]]:
        matrix = self.adjacenc_matrix
        if index < 0 or index >= len(matrix):
            return
        return matrix[index]
    
    # возвращает вес ребра
    def get_edge(self, from_index: int, to_index: int) -> Optional[int | float]:
        matrix = self.adjacenc_matrix
        if min(from_index, to_index) < 0 or max(from_index, to_index) >= len(matrix) or from_index == to_index:
            return
        return matrix[from_index][to_index]
    
    # удаляет вершину
    def remove_vertex(self, index: int) -> None:
        matrix = self.adjacenc_matrix
        # если пуст ил индекс вышел из диапазона списка, то выход
        if len(matrix) == 0 or index < 0 or index >= len(matrix):
            return
        # удаление всех мест индекса
        for el in matrix:
           el.pop(index)
        matrix.pop(index)
    
    # удаляет ребро (равняет в None)
    def remove_edge(self, from_index: int, to_index: int) -> Optional[int | float]:
        matrix = self.adjacenc_matrix
        # если индекс меньше 0 или превышает или равен колличество вершин или индексы равны
        if min(from_index, to_index) < 0 or max(from_index, to_index) >= len(matrix) or from_index == to_index:
            return
        # если пуст или только одна вершина, то выход
        if len(matrix) < 2:
            return
        # вес ребра
        weight = matrix[from_index][to_index]
        # удаляем ребро от одной вершины к другой
        matrix[from_index][to_index] = None
        # и наоборот удаляем от другой к одной вершине, если ненаправленный
        if not self.directed:
            matrix[to_index][from_index] = None
        return weight
    
    # Очистка матрицы Графа
    def clear(self) -> None:
        self.adjacenc_matrix.clear()
    
    # Сохранение состояния Графа в json формате 
    def save(self, path: str) -> None:
        with open(path, "w", encoding="UTF-8") as file_save:
            json.dump(self.adjacenc_matrix, file_save, ensure_ascii=False, default=str)
    
    # Загрузка состояния Графа в json формате        
    def load(self, path: str) -> None:
        with open(path, "r", encoding="UTF-8") as file_load:
            self.adjacenc_matrix.clear()
            self.adjacenc_matrix = json.load(file_load)
    
    # Алгоритм Дейкстры - поиск кратчайщего пути (возвращает список последовательности индексов и сумму мас их рёбер)
    def shortest_path_Dijkstra(self, start: int, end: int) -> Optional[tuple[List[int], int | float]]:
        # если граф пустой - выход
        if self.get_length() == 0:
            return
        matrix = self.adjacenc_matrix
        # текущий индекс вершины, из которого будет отмеряется расстояние к другим вершинам
        index = start
        # к каждой вершине назначаем бесконечную сумму (в будущем это будут их минимальные суммы)
        min_sum = [float("inf") for _ in range(self.get_length())]
        # у начальной вершины расстояние = 0
        min_sum[index] = 0
        # обработанные вершины (на которых уже были)
        vers = []
        # сохранение индексов вершин минимальных путей расстояний
        path = [[] for _ in range(self.get_length())]
        # начальная вершина имеет себя, в качестве первой вершины
        path[index] = [index]
        # алгоритм продолжается пока индекс не дойдёт до конечной вершины
        while index != end:
            # существующие рёбра вершины индекса (index)
            ed = []
            for i in range(self.get_length()):
                # если это ребро, то записываем при условии, что вершина ещё не пройдена
                if matrix[index][i] is not None and i not in vers:
                    ed += [i]
            # перебираем рёбра (индексы вершин)
            for i in ed:
                # получаем расстояние ребра
                mas = self.get_edge(index, i)
                # если ребро меньше, нынешней суммы вершины, к которой идём то переписываем сумму этого индекса и вписываем в пути
                if min_sum[index] + mas < min_sum[i]:
                    min_sum[i] = min_sum[index] + mas
                    # записывает весь накопленный путь вершины вместе с вершиной, к которой идём
                    path[i] = path[index] + [i]
            # записываем текущий индекс, как уже пройдённый
            vers += [index]
            # вычитае через set уберёт из списка пройденные вершины
            index_min = list(set(range(self.get_length())) - set(vers))
            # берём за индекс самую минимальную сумму, но не берём уже пройденные
            index = min(index_min, key=lambda x: min_sum[x])
        # возвращаем список самой короткой последовательности вершин и её сумму
        return (path[end], min_sum[end])
        
    # Алгоритм Форда-Беллмана - поиск кратчайщего пути (возвращает список последовательности индексов и сумму мас их рёбер)
    def shortest_path_Bellman_Ford(self, start: int, end: int) -> Optional[tuple[List[int], int | float]]:
        # если граф пустой - выход
        if self.get_length() == 0:
            return
        # все существующие рёбра - в виде записи (от вершины, до вершины, масса ребра)
        edges = []
        for i in range(self.get_length()):
           
            for j in range(self.get_length()):
                # если индексы равны - пропускаем
                if i == j:
                    continue
                # если есть у вершин соединение (ребро), то записываем в edges
                w = self.get_edge(i, j)
                if w is not None:
                    edges += [(i, j, w)]
                
        # к каждой вершине назначаем бесконечную сумму (в будущем это будут их минимальные суммы)
        min_sum = [float("inf") for _ in range(self.get_length())]
        # у начальной вершины расстояние = 0
        min_sum[start] = 0
        # сохранение индексов вершин минимальных путей расстояний
        path = [[] for _ in range(self.get_length())]
        # начальная вершина имеет себя, в качестве первой вершины
        path[start] = [start]
        # есть ли отрицательный цикл
        cycle_minus = True
        # итерации идут до максимального количества возможных вершин в пути
        for _ in range(self.get_length() - 1):
            # если не изменится суммы, то нахождение пути и её суммы возможна
            cycle_minus = False
            # перебор всех рёбер
            print(f"\n Iteration - {_ + 1} |", min_sum)
            for i, j, w in edges:
                # если ребро меньше, нынешней суммы вершины, к которой идём то переписываем сумму этого индекса и вписываем в пути
                if min_sum[i] + w < min_sum[j]:
                    print(f"[V] {i} -> {j}:  {min_sum[i]} + {w}[{min_sum[i] + w}] < {min_sum[j]}")
                    min_sum[j] = min_sum[i] + w
                    # записывает весь накопленный путь вершины вместе с вершиной, к которой идём
                    path[j] = path[i] + [j]
                    # возможен отрицательный цикл
                    cycle_minus = True
                else:
                    print(f"[X] {i} -> {j}:  {min_sum[i]} + {w}[{min_sum[i] + w}] >= {min_sum[j]}")
            # возвращаем путь до заданной вершины (end) и её сумму - так как итерация ничего не изменила
            if not(cycle_minus):
                return (path[end], min_sum[end])
            print("Path:", path[end], "| Sum:", min_sum[end])
        # Бесконечный отрицательный цикл либо нету рёбер
        if cycle_minus:
            return None
        # Иначе возвращаем путь до заданной вершины (end) и её сумму
        return (path[end], min_sum[end])
        
    # Магический метод вывода Графа
    def __str__(self) -> str:
        txt = ""
        for i in self.adjacenc_matrix:
            txt += ("\t".join(map(str, i)).replace("None", "0") + "\n")
        else:
            txt = txt[:-1]
        return txt



def to_graph(txt: str, graph: Graph) -> int:
    col:list = txt.rstrip("\n").split("\n")[1:]
    for vs in range(len(col)):
        graph.add_vertex()
    for vs in range(len(col)):
        lt = col[vs].split("\t")[1:]
        for v in range(len(lt)):
            if lt[v].replace("-", "").isdigit():
                graph.add_edge(vs, v, int(lt[v]))
    return len(col)
    
tx = """	A	B	C	D	E
A			4		5
B			-4		
C	-3				
D	4		7		3
E		2	3		"""

g = Graph(True)
# size = 5
# for i in range(size):
#     g.add_vertex()
# g.clear()
size = to_graph(tx, g)
print("Adjacenc matrix of Graph:")
print(g)
path, sm = g.shortest_path_Bellman_Ford(0, 2)
print("\nShort path:", path, "| Sum of path:", sm, "\n")

# """
# 	A	B	C	D	E
# A			-4		5
# B			-4		
# C	-3				
# D	4		-7		3
# E		2	3		"""     
  
# ggg = Graph(True)

# size = 5
# for i in range(size):
#     ggg.add_vertex()

# ggg.add_edge(0, 1, -3)

# ggg.add_edge(1, 0, 4)
# ggg.add_edge(1, 2, 5)
# ggg.add_edge(1, 4, 7)

# ggg.add_edge(2, 0, 6)
# ggg.add_edge(2, 3, 1)

# ggg.add_edge(3, 1, 5)
# ggg.add_edge(3, 4, 6)

# ggg.add_edge(4, 0, -4)
# ggg.add_edge(4, 2, 8)
       
# print(ggg) 
# print(ggg.shortest_path_Bellman_Ford(3, 2))  
# print(ggg.shortest_path_Bellman_Ford(3, 0))  
# print(ggg.shortest_path_Bellman_Ford(0, 3))    


# g.add_edge(3, 0, 4)  # D -> A, weight 4
# g.add_edge(3, 2, 7)  # D -> C, weight 7
# g.add_edge(3, 4, 3)  # D -> E, weight 3
# g.add_edge(0, 2, 4)  # A -> C, weight 4
# g.add_edge(2, 0, -3) # C -> A, weight -3
# g.add_edge(0, 4, -5)  # A -> E, weight 5
# g.add_edge(4, 2, 3)  # E -> C, weight 3
# g.add_edge(1, 2, -4) # B -> C, weight -4
# g.add_edge(4, 1, 2)  # E -> B, weight 2

# print(g)

# ggg.clear()
# n = 0
# t = "ABCDE"


# ggg = Graph()
# size = 6
# for i in range(size):
#     ggg.add_vertex()

# ggg.add_edge(0, 1, 7)
# ggg.add_edge(0, 2, 9)
# ggg.add_edge(0, 5, 14)

# ggg.add_edge(1, 2, 10)
# ggg.add_edge(1, 3, 6)

# ggg.add_edge(2, 3, 11)
# ggg.add_edge(2, 5, 2)

# ggg.add_edge(3, 4, 6)

# ggg.add_edge(5, 4, 9)


# for txt in tx.split("NON\n"):
#     n += 1
#     print("=== ЗАДАНИЕ", n)
#     g.clear()
#     size = to_graph(txt, ggg)
#     print("Adjacenc matrix of Graph:")
#     print(ggg, "\n")
#     for i in range(0, size):
#         for j in range(0, size):
            
#             nn = ggg.shortest_path_Bellman_Ford(i, j)
#             if nn is not None:
#                 path, sm = nn
#                 print(f"{t[i]} {t[j]}", "Short path:", path, "| Sum of path:", sm, "\n")     
#             else:
#                 print("тут имеется отрицательный цикл")
#                 break
#         if nn is None:
#             break
# ggg = Graph()

# tx = """	A	B	C	D	E
# A		1			
# B	1		2	2	7
# C		2			3
# D		2			4
# E		7	3	4	
# NON
# 	A	B	C	D	E
# A		5	3		
# B	5		1	4	
# C	3	1		6	
# D		4	6		1
# E				1	
# NON
# 	A	B	C	D	E
# A		3	7		
# B	3		2		8
# C	7	2		4	
# D			4		1
# E		8		1	
# NON
# 	A	B	C	D	E
# A		1			
# B	1		4	2	8
# C		4			4
# D		2			4
# E		8	4	4	
# NON
# 	A	B	C	D	E
# A		4	7		
# B	4		1	5	
# C	7	1		3	
# D		5	3		1
# E				1	
# NON
# 	A	B	C	D	E
# A		7	4		
# B	7		2		4
# C	4	2		4	
# D			4		4
# E		4		4	
# NON
# 	A	B	C	D	E
# A		3			
# B	3		1	2	6
# C		1			3
# D		2			3
# E		6	3	3	
# NON
# 	A	B	C	D	E
# A		2	5	1	
# B	2		3		
# C	5	3		3	2
# D	1		3		
# E			2		
# NON
# 	A	B	C	D	E
# A		2		1	
# B	2		3	3	
# C		3		3	2
# D	1	3	3		
# E			2		
# NON
# 	A	B	C	D	E
# A		2	3		
# B	2			3	5
# C	3			4	
# D		3	4		1
# E		5		1	
# NON
# 	A	B	C	D	E
# A		2	6	4	
# B	2		3		
# C	6	3		3	2
# D	4		3		
# E			2		
# NON
# 	A	B	C	D	E	F
# A		4	11			33
# B	4		4			
# C	11	4		7	11	20
# D			7			13
# E			11			8
# F	33		20	13	8	"""

# n = 0
# for txt in tx.split("NON\n"):
#     n += 1
#     print("=== ЗАДАНИЕ", n)
#     ggg.clear()
#     size = to_graph(txt, ggg)
#     print("Adjacenc matrix of Graph:")
#     print(ggg, "\n")
#     path, sm = ggg.shortest_path_Bellman_Ford(0, size - 1)
#     print("Short path:", path, "| Sum of path:", sm, "\n")




        
        
        
        