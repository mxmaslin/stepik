Есть файл в котором в каждой строчке два числа разделенных запятой: ID студента и ID решенной задачи. Пример:

```
1,2
1,4
1,3
1,3
2,1
2,2
2,3
2,4
```

Напишите функцию, которая принимает имя файла и возвращает словарь, в котором для каждого студента будет указано количество решенных им задач. Записи о решенных задачах могут повторятся.

**Решение**

```
def solved_tasks(filename): 
    with open(filename) as f: 
        data = f.readlines() 
    lines = {tuple(int(y) for y in x.split(',')) for x in data} 
    result = {} 
    for line in lines: 
        student, _ = line 
        result[student] = result.get(student, 0) + 1 
    return result
```