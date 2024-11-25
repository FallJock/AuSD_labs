



#  ===========    Не тот код    ================




from structuredata.array import Array
from temp.car import Car, element
from timeit import timeit
from random import choice, randint

times1 = ""

for su in range(1, 5):
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
        x.set_flag("vin")
        table.append(x)
    
    table.sort_insertion()
    find_elem = choice(dit)
    code1 = """table.search_binary(find_elem)"""

    time1 = timeit(code1, number=20, globals={"find_elem": find_elem, "table": table})
    table.clear()

    times1 += f"{k1}\t|\t{time1}\n"
             
print("Бинарный поиск - по полю vin")
print(f"Кол-во элементов\t|\tВремя")
print(times1)

