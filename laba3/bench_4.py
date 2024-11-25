from structuredata.binarysearchtree import BinarySearchTree
from temp.car import Car, element
from timeit import timeit
from random import choice, randint

times1 = ""
times2 = ""

for su in range(1, 6):
    table = BinarySearchTree()
    # колличество элементов
    k1 = 10 ** su
    dit = []
    marks = [i.mark for i in element]
    for i in range(k1):
        dit += [Car(
            mark=choice(marks),
            vin="".join(choice("0123456789ABCDEFGHJKLMNPRSTUVWXYZ") for i in range(17)),
            engine_capacity=randint(5_00, 40_00)/100,
            cost=randint(900_000 * 100, 6_000_000 * 100)/100,
            average_speed=randint(70_00, 250_00)/100
        )]
        
    for x in dit:
        table.insert(x)
    for x in dit:
        table.remove(x)
    code1 = """for x in dit:
        table.insert(x)
    """
    code2 = """for x in dit:
        table.remove(x)
    """
    time1 = timeit(code1, number=1, globals={"dit": dit, "table": table})
    time2 = timeit(code2, number=1, globals={"dit": dit, "table": table})
    times1 += f"        {k1}            |          {time1}\n"
    times2 += f"        {k1}            |        {time2}\n"
             
print("Вставка")
print(f"Кол-во елементов    |   Время")
print(times1)
print("Удаление")
print(f"Кол-во елементов    |   Время")
print(times2)