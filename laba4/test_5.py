from structuredata.array import Array
# element_book - содержит 10 различных элементов книг (10 различных Book)
from temp.book import Book, element_book

ex_book1 = Book("П. Л. Нимский", "Эксмо", 520, 555, 9780000000000)
ex_book2 = Book("Шиткин", "Эксмо", 120, 55, 9780000000001)
same_cost = Book("И. Д. Тимухин", "Азбука", 520, 255, 9780000000002)

cap = 10
arr = Array(cap)
ind = 4

sorted_pages = sorted([i.pages for i in element_book])
sorted_cost = sorted([i.cost for i in element_book])
sorted_cost.reverse()

# добавление в конец
def test_append():
    for elem in element_book:
        arr.append(elem)
    
    for i in range(len(element_book)):
        assert element_book[i] == arr[i]

# проверка функций на get_ дающие значение
def test_gets():
    assert arr.get_capacity() == cap
    assert arr.get_length() == len(element_book)

    for i in range(len(element_book)):
        assert element_book[i] == arr.get(i)

# вставка с проверка размера
def test_resize_capacity():
    new_cap = cap * 2
    arr.append(element_book[2])
    assert arr.get_capacity() == new_cap

# вставка
def test_insert():
    arr.insert(ex_book1, ind)
    assert arr[ind] == ex_book1
    assert arr[ind - 1] == element_book[ind - 1]
    assert arr[ind + 1] == element_book[ind]
    arr.insert(ex_book2, 0)
    assert arr[0] == ex_book2
    assert arr[1] == element_book[0]
    arr.insert(same_cost, arr.get_length())
    assert arr[arr.get_length() - 1] == same_cost

# задаёт элемент по индексу
def test_set_elem():
    arr[0] = element_book[-1]
    assert arr[0] == element_book[-1]

# удаление и очистка
def test_remove_and_clear():
    assert arr.remove(0) == element_book[-1]
    assert arr.remove(arr.get_length() - 1) == same_cost
    assert arr.remove(arr.get_length() - 1) == element_book[2]
    assert arr.remove(ind) == ex_book1
    assert arr.get_length() == len(element_book)

# проверка быстрой сортировки 
def test_sort_quick():
    arr.sort_quick()
    for i in range(len(element_book)):
        assert arr[i].get_flag() == sorted_pages[i]

# проверка сортировки по основанию
def test_sort_radix():
    arr.sort_radix()
    for i in range(len(element_book)):
        assert arr[i].get_flag() == sorted_cost[i]

# проверка вывода
def test_str():
    list_str = "[" + ", ".join(map(str, sorted_cost)) + "]"
    assert list_str == str(arr)

# проверка работы итерации
def test_iteration():
    n = 0
    for elem in arr:
        assert elem.get_flag() in sorted_cost
        assert elem.get_flag() == sorted_cost[n]
        n += 1