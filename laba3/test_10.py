from structuredata.minheap import MinHeap
from temp.car import Car, element
import os.path

ex_car1 = Car("Haval 0.2v", "LGUFF4A59HF507891", 7, 3_890_000, 88)
same_cost = Car("Haval 0.3v", "LHHFF4G67HF777001", 5, 3_890_000, 180)
heap = MinHeap()
lheaply = [
    1800500, 2044000, 2000000, 2104000, 2111000,
    3003000, 4003900.5, 3060000, 2500000, 3000000
    ]

# вставка
def test_insert():
    for i in element:
        heap.insert(i)
    for it in element:
        assert heap.find(it)
    
# вставка с таким же ключём и проверка размера
def test_insert_same_and_size():
    heap.insert(ex_car1)
    heap.insert(same_cost)
    assert heap.get_size() == len(element) + 2

# удаление
def test_remove():
    m = element + [ex_car1] + [same_cost]
    for it in m:
        assert heap.remove() in m
    assert heap.get_size() == 0

# сохранение состояния в файл (проверка существует ли файл)
def test_save():
    for i in element:
        heap.insert(i)
    path = "test_json2.json"
    heap.save(path)
    assert os.path.exists(path)

# загрузка файла в пустое дерево
def test_load():
    path = "test_json2.json"
    orig = MinHeap()
    orig.list = heap.list
    heap.list.clear()
    heap.load(path)
    assert orig.list == heap.list

# проверка нахождения ключа
def test_find():
    assert heap.find(element[1])
    assert not(heap.find(ex_car1))

# Проверка на максимальное значение и минимальное
def test_heapify():
    for i in range(len(element)):
        assert heap.get(i).cost == lheaply[i]
