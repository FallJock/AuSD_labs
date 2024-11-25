from timeit import timeit
from stucturedata.stack import Stack

times1 = ""
times2 = ""

for capacity in range(1, 4):
    for su in range(1, 4):
        k1 = 10 ** capacity
        stack = Stack(k1)
        dit = []
        for i in range(k1):
            dit += [i * 2]
        code1 = """for x in dit:
            stack.push(x)
        """
        code2 = """for x in dit:
            stack.pop()
        """
        time1 = timeit(code1, number=1, globals={"dit": dit, "stack": stack})
        time2 = timeit(code2, number=1, globals={"dit": dit, "stack": stack})
        times1 += f"        {k1}         |          {time1}\n"
        times2 += f"        {k1}         |          {time2}\n"

print("Вставка")
print(f"Кол-во елементов (вместимость)     |   Время")
print(times1)
print("Удаление")
print(f"Кол-во елементов (вместимость)    |   Время")
print(times2)
