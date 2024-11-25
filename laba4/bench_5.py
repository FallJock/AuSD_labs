



#  ===========    Не тот код    ================



from structuredata.array import Array
from temp.book import Book
from timeit import timeit
from random import choice, randint
from string import ascii_letters

times1 = ""
times2 = ""

for su in range(1, 5):
    # колличество элементов
    k1 = 10 ** su
    table = Array(k1)
    dit = []
    for i in range(k1):
        dit += [Book(
            author="".join(choice(ascii_letters) for i in range(randint(5, 30))),
            publisher="".join(choice(ascii_letters) for i in range(randint(5, 30))),
            pages=randint(10, 1000),
            cost=randint(100, 10000),
            isbn=int("".join(str(choice(range(10))) for i in range(13)))
        )]
        
    for x in dit:
        table.append(x)
    code1 = """table.sort_quick()"""

    time1 = timeit(code1, number=1, globals={"dit": dit, "table": table})
    table.clear()
    
    for x in dit:
        table.append(x)
    code2 = """table.sort_radix()"""
    
    time2 = timeit(code2, number=1, globals={"dit": dit, "table": table})
    table.clear()
    times1 += f"        {k1}            |          {time1}\n"
    times2 += f"        {k1}            |        {time2}\n"
             
print("Быстрая сортировка: по возврастанию - по полю кол-во страниц")
print(f"Кол-во елементов    |   Время")
print(times1)

print("Сортировка по основанию: по убыванию - по полю стоимость")
print(f"Кол-во елементов    |   Время")
print(times2)