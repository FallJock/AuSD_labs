



#  ===========    Не тот код    ================



from structuredata.array import Array
from temp.book import Book
from timeit import timeit
from random import choice, randint
from string import ascii_letters

times1 = ""

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
        x.set_flag("author")
        table.append(x)
    
    table.sort_insertion()
    find_elem = choice(dit)
    code1 = """table.search_jump(find_elem)"""

    time1 = timeit(code1, number=20, globals={"find_elem": find_elem, "table": table})
    table.clear()

    times1 += f"{k1}\t|\t{time1}\n"
             
print("Скачкообразный поиск - по полю автор")
print(f"Кол-во елементов\t|\tВремя")
print(times1)
