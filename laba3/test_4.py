from structuredata.binarysearchtree import BinarySearchTree
# element - содержит 10 различных элементов машин (10 различных Car)
from temp.car import Car, element
import os.path

ex_car1 = Car("Haval 0.2v", "LGUFF4A59HF507891", 7, 3_890_000, 88)
same_cost = Car("Haval 0.3v", "LHHFF4G67HF777001", 5, 3_890_000, 180)
binseatre = BinarySearchTree()


# вставка
def test_insert():
    for i in element:
        binseatre.insert(i)
    btree = binseatre.list_preorder_tree(binseatre.root)
    for it in element:
        assert it in btree

# вставка с таким же ключём и проверка размера
def test_insert_same_and_size():
    binseatre.insert(ex_car1)
    size1 = binseatre.get_size()
    btree_pre1 = binseatre.list_preorder_tree(binseatre.root)
    binseatre.insert(same_cost)
    size2 = binseatre.get_size()
    btree_pre2 = binseatre.list_preorder_tree(binseatre.root)
    assert btree_pre1 == btree_pre2
    assert size1 == size2
    binseatre.root = None
    assert binseatre.get_size() == 0

# удаление
def test_remove():
    for i in element:
        binseatre.insert(i)
    btree = binseatre.list_preorder_tree(binseatre.root)
    binseatre.insert(ex_car1)
    binseatre.remove(ex_car1)
    btree2 = binseatre.list_preorder_tree(binseatre.root)
    assert btree == btree2

# сохранение состояния в файл (проверка существует ли файл)
def test_save():
    path = "test_json1.json"
    binseatre.save(path)
    assert os.path.exists(path)

# загрузка файла в пустое дерево
def test_load():
    path = "test_json1.json"
    btree_pre = binseatre.list_preorder_tree(binseatre.root)
    btree_post = binseatre.list_postorder_tree(binseatre.root)
    btree_in = binseatre.list_inorder_tree(binseatre.root)
    binseatre.root = None
    binseatre.load(path)
    b1 = binseatre.list_preorder_tree(binseatre.root)
    b2 = binseatre.list_postorder_tree(binseatre.root)
    b3 = binseatre.list_inorder_tree(binseatre.root)
    assert b1 == btree_pre
    assert b2 == btree_post
    assert b3 == btree_in

# проверка нахождения ключа
def test_find():
    nen = binseatre.find(same_cost)
    assert nen is None
    assert binseatre.find(element[3]).key == element[3]

# Проверка на максимальное значение и минимальное
def test_max_min():
    costs = [i for i in element]
    mx, mn = max(costs), min(costs)
    assert mx == binseatre.max()
    assert mn == binseatre.min()
