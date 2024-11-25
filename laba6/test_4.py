from structuredata.graph import Graph
import os.path

matrix = Graph()
size = 4
m1 = [[None] * size for _ in range(size)]
m2_direct = [[None] * size for _ in range(size)]
m3 = [[None] * size for _ in range(size)]
element = [
    (0, 1, 1),
    (1, 2, 1),
    (2, 3, 1),
    (0, 3, 1)
]

for i, j, w in element:
    m2_direct[i][j] = w
    m3[i][j] = w
    m3[j][i] = w

grafs = """	A	B	C	D	E
A		1			
B	1		2	2	7
C		2			3
D		2			4
E		7	3	4	
NON
	A	B	C	D	E
A		5	3		
B	5		1	4	
C	3	1		6	
D		4	6		1
E				1	
NON
	A	B	C	D	E
A		3	7		
B	3		2		8
C	7	2		4	
D			4		1
E		8		1	"""

negative_graph = """	A	B	C	D	E
A			4		5
B			-4		
C	-3				
D	4		7		3
E		2	3		
NON
	A	B	C	D	E
A			-4		5
B			-4		
C	-3				
D	4		-7		3
E		2	3		"""

otv = [
    ([0, 1, 2, 4], 6),
    ([0, 2, 1, 3, 4], 9),
    ([0, 1, 2, 3, 4], 10)
    ]

negative_otv = [
    ([0, 4, 1, 2], 3),
    None,
    ]

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

# добавление в конец вершины
def test_add_vertex():
    for _ in element:
        matrix.add_vertex()
    assert m1 == matrix.adjacenc_matrix

# добавление ребра с весом
def test_add_edge():
    for i, j, w in element:
        matrix.add_edge(i, j, w)
    assert matrix.adjacenc_matrix == m3

# проверка функций на get_ дающие значение
def test_gets():
    assert matrix.get_length() == len(element)
    for i in range(matrix.get_length()):
        assert matrix.get_vertex(i) == m3[i]
        for j in range(matrix.get_length()):
            assert matrix.get_edge(i, j) == m3[i][j]
      
# удаление вершины
def test_remove_vertex():
    ind = 1
    matrix.remove_vertex(ind)
    assert matrix.get_length() == size - ind
    assert matrix.get_edge(ind, 0) == m3[ind + 1][0]
    assert matrix.get_edge(ind, 1) == m3[ind + 1][2]
    assert matrix.get_edge(ind, 2) == m3[ind + 1][3]
     
# удаление ребра
def test_remove_edge():
    weight = matrix.remove_edge(element[0][0], element[0][1])
    assert weight == None
    assert matrix.get_edge(element[0][0], element[0][1]) == None

# удаление и очистка
def test_clear():
    matrix.clear()
    assert matrix.get_length() == 0
    assert matrix.adjacenc_matrix == []

# если граф ориентированный
def test_add_edge_direct():
    matrix.directed = True
    for _ in element:
        matrix.add_vertex()
    for i, j, w in element:
        matrix.add_edge(i, j, w)
    assert matrix.adjacenc_matrix == m2_direct
    matrix.directed = False
    
# проверка вывода
def test_str():
    list_str = ""
    for i in m2_direct:
        list_str += "\t".join(map(str, i)).replace("None", "0") + "\n"
    else:
        list_str = list_str[:-1]
    assert list_str == str(matrix)

# сохранение состояния в файл (проверка существует ли файл)
def test_save():
    path = "test_json1.json"
    matrix.adjacenc_matrix = [i for i in m3]
    matrix.save(path)
    assert os.path.exists(path)

# загрузка файла в пустое дерево
def test_load():
    path = "test_json1.json"
    matrix.clear()
    matrix.load(path)
    assert matrix.adjacenc_matrix == m3

# сверка ответов Алгоритма Дейкстры
def test_dijkstra():
    n = -1
    for txt in grafs.split("NON\n"):
        n += 1
        matrix.clear()
        size = to_graph(txt, matrix)
        path, sm = matrix.shortest_path_Dijkstra(0, size - 1)
        assert path == otv[n][0]
        assert sm == otv[n][1]

# сверка ответов Алгоритма Форда-Беллмана
def test_bellman_ford():
    matrix.directed = True
    n = -1
    for txt in negative_graph.split("NON\n"):
        n += 1
        matrix.clear()
        size = to_graph(txt, matrix)
        res = matrix.shortest_path_Bellman_Ford(0, 2)
        assert res == negative_otv[n]
    n = -1
    for txt in grafs.split("NON\n"):
        n += 1
        matrix.clear()
        size = to_graph(txt, matrix)
        path, sm = matrix.shortest_path_Bellman_Ford(0, size - 1)
        assert path == otv[n][0]
        assert sm == otv[n][1]


# test_add_vertex()
# test_add_edge()
# test_gets()
# test_remove_vertex()
# test_remove_edge()
# test_clear()
# test_add_edge_direct()
# test_str()
# test_save()
# test_load()
# test_dijkstra()
# test_bellman_ford()