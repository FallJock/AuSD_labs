



#  ===========    Не тот код    ================




from structuredata.array import Array
from temp.car import Car, element
from timeit import timeit
from random import choice, randint

times1 = ""
times2 = ""

for su in range(1, 6):
    # колличество элементов
    k1 = 10 ** su
    table = Array(k1)
    dit = []
    marks = [i.mark for i in element]
    for i in range(k1):
        dit += [Car(
            mark=choice(marks),
            vin="".join(choice("0123456789ABCDEFGHJKLMNPRSTUVWXYZ") for i in range(17)),
            engine_capacity=randint(50, 400),
            cost=randint(900_000, 6_000_000),
            average_speed=randint(70_00, 250_00)/100
        )]
        
    for x in dit:
        table.append(x)
    code1 = """table.sort_insertion()"""

    time1 = timeit(code1, number=1, globals={"dit": dit, "table": table})
    table.clear()
    
    for x in dit:
        table.append(x)
    code2 = """table.sort_comb()"""
    
    time2 = timeit(code2, number=1, globals={"dit": dit, "table": table})
    table.clear()
    
    times1 += f"        {k1}            |          {time1}\n"
    times2 += f"        {k1}            |        {time2}\n"
             
print("Сортировка вставками: по возврастанию - по полю vin")
print(f"Кол-во елементов    |   Время")
print(times1)

print("Сортировка расчёской: по убыванию - по полю средняя скорость")
print(f"Кол-во елементов    |   Время")
print(times2)