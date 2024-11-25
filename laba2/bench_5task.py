from timeit import timeit
from stucturedata.hashtable import HashTable


times1 = ""
times2 = ""
for capacity in range(1, 4):
    for su in range(1, 4):
        table = HashTable(10 ** capacity)
        k1 = 10 ** su
        dit = []
        for i in range(k1):
            dit += [(i, i * 2)]
            for x in dit:
                table[x[0]] = x[1]
        code1 = """for x in dit:
            table[x[0]] = x[1]
        """
        code2 = """for x in dit:
            table.remove(x[0])
        """
        time1 = timeit(code1, number=1, globals={"dit": dit, "table": table})
        time2 = timeit(code2, number=1, globals={"dit": dit, "table": table})
        times1 += f"        {k1}            |        {10 ** capacity}         |          {time1}\n"
        times2 += f"        {k1}            |        {10 ** capacity}           |        {time2}\n"
             
print("Вставка")
print(f"Кол-во елементов    |    Вместимость хэш-таблицы |   Время")
print(times1)
print("Удаление")
print(f"Кол-во елементов    |    Вместимость хэш-таблицы |   Время")
print(times2)