from structuredata.array import Array
# element - содержит 10 различных элементов машин (10 различных Car)
from temp.car import Car, element

ex_car1 = Car("Haval 0.2v", "LGUFF4A59HF507891", 7, 3_890_000, 88)
ex_car2 = Car("Haval 0.3v", "JJJF4A59HF567892", 6, 3_000_100, 58)
same_cost = Car("Haval 0.4v", "LHHFF4G67HF777001", 5, 3_890_000, 180)

cap = 10
arr = Array(cap)
ind = 4

sorted_vin = sorted([i.vin for i in element])
sorted_average_speed = sorted([i.average_speed for i in element])
sorted_average_speed.reverse()

# добавление в конец
def test_append():
    for elem in element:
        arr.append(elem)
    
    for i in range(len(element)):
        assert element[i] == arr[i]

# проверка функций на get_ дающие значение
def test_gets():
    assert arr.get_capacity() == cap
    assert arr.get_length() == len(element)

    for i in range(len(element)):
        assert element[i] == arr.get(i)

# вставка с проверка размера
def test_resize_capacity():
    new_cap = cap * 2
    arr.append(element[2])
    assert arr.get_capacity() == new_cap

# вставка
def test_insert():
    arr.insert(ex_car1, ind)
    assert arr[ind] == ex_car1
    assert arr[ind - 1] == element[ind - 1]
    assert arr[ind + 1] == element[ind]
    arr.insert(ex_car2, 0)
    assert arr[0] == ex_car2
    assert arr[1] == element[0]
    arr.insert(same_cost, arr.get_length())
    assert arr[arr.get_length() - 1] == same_cost

# задаёт элемент по индексу
def test_set_elem():
    arr[0] = element[-1]
    assert arr[0] == element[-1]

# удаление и очистка
def test_remove_and_clear():
    assert arr.remove(0) == element[-1]
    assert arr.remove(arr.get_length() - 1) == same_cost
    assert arr.remove(arr.get_length() - 1) == element[2]
    assert arr.remove(ind) == ex_car1
    assert arr.get_length() == len(element)

# проверка сортировки вставками
def test_sort_insertion():
    arr.sort_insertion()
    for i in range(len(element)):
        assert arr[i].get_flag() == sorted_vin[i]

# проверка сортировки расчёской
def test_sort_comb():
    arr.sort_comb()
    for i in range(len(element)):
        assert arr[i].get_flag() == sorted_average_speed[i]

# проверка вывода
def test_str():
    list_str = "[" + ", ".join(map(str, sorted_average_speed)) + "]"
    assert list_str == str(arr)

# проверка работы итерации
def test_iteration():
    n = 0
    for elem in arr:
        assert elem.get_flag() in sorted_average_speed
        assert elem.get_flag() == sorted_average_speed[n]
        n += 1
        