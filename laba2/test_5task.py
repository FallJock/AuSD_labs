from stucturedata.hashtable import HashTable

hash_table = HashTable(5)
dit = [(1, 1), (5, 2), (9, 3), (99, 4)]
dit2 = [(1, 1), (5, 2), (9, 3), (99, 4), (95, 5), (33, 6)]
dit3 = [(5, 2), (9, 3), (99, 4)]

# вставка
def test_push():
    for key, value in dit:
        hash_table[key] = value
    for n in range(len(dit)):
        assert dit[n][1] in hash_table.values()
        assert dit[n][0] in hash_table

# вставка с количеством больше чем вместимость
def test_push_moreCapacity():
    for key, value in dit2:
        hash_table[key] = value
        print(hash_table[key], hash_table.keys())
    for n in range(len(dit2)):
        assert dit2[n][1] in hash_table.values()
        assert dit2[n][0] in hash_table

# очистка хэш-таблицы
def test_clear():
    hash_table.clear()
    assert hash_table.keys() == []
    assert hash_table.values() == []

# проверка методов keys() и values()
def test_keys_and_values():
    for key, value in dit2:
        hash_table[key] = value
        print(hash_table[key], hash_table.keys())
    k = set([i[0] for i in dit2])
    v = set([i[1] for i in dit2])
    assert k == set(hash_table.keys())
    assert v == set(hash_table.values())

# проверка удаления
def test_remove():
    hash_table.remove(95)
    hash_table.remove(33)
    for n in range(len(dit)):
        assert dit[n][1] in hash_table.values()
        assert dit[n][0] in hash_table
    hash_table.remove(1)
    for n in range(len(dit3)):
        assert dit3[n][1] in hash_table.values()
        assert dit3[n][0] in hash_table
    

