from stucturedata.stack import Stack

stack = Stack(5)
lt1 = [5, 4, 3, 2, 1]

# проверка вставки
def test_push():
    for i in range(len(lt1)):
        stack.push(lt1[i])
    m = str(stack).replace("[", "").replace("]", "").replace(",", "").split()
    n = 0
    lt1.reverse()
    for i in map(int, m):
        assert i == lt1[n]
        n += 1

# проверка удаления
def test_remove():
    assert stack.pop() == lt1[0]
    assert stack.pop() == lt1[1]
    assert stack.pop() == lt1[2]
    assert stack.pop() == lt1[3]
    assert stack.pop() == lt1[4]

# проверка пустой ли стект
def test_empty():
    assert stack.is_empty() is True

# проверка фенкции peak (верхушки стека)
def test_peak():
    lt1.reverse()
    for i in range(len(lt1)):
        stack.push(lt1[i])
        assert stack.peak() == lt1[i]

# проверка размера стека
def test_size():
    assert stack.get_size() == 5
    stack.pop()
    assert stack.get_size() == 4
    stack.pop()
    assert stack.get_size() == 3
    stack.pop()
    assert stack.get_size() == 2
    stack.pop()
    assert stack.get_size() == 1
    stack.pop()
    assert stack.get_size() == 0
    stack.push(45)
    assert stack.get_size() == 1