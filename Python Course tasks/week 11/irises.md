У вас есть файл со следующим содержимым (первые 10 строк):

"sepal.length","sepal.width","petal.length","petal.width","variety"
5.1,3.5,1.4,.2,"Setosa"
4.9,3,1.4,.2,"Setosa"
4.7,3.2,1.3,.2,"Setosa"
4.6,3.1,1.5,.2,"Setosa"
5,3.6,1.4,.2,"Setosa"
5.4,3.9,1.7,.4,"Setosa"
4.6,3.4,1.4,.3,"Setosa"
5,3.4,1.5,.2,"Setosa"
4.4,2.9,1.4,.2,"Setosa"
В этом файле записаны данные о цветах ирисах: длина чашелистика, ширина чашелистика, длина и ширина лепестка и сорт ириса.

Напишите функцию, которая будет принимать имя файла и название сорта и возвращать среднюю длину лепестка.

Обратите внимание, название сорта будет передаваться без лишних кавычек. Например:

`mean_petal('filename', 'Setosa')`

**Решение**

```
def mean_petal(filename, variety):
    with open(filename) as f:
        data = f.read().split()[1:]
    result = []
    for line in data:
        _, _, petal_length, _, line_variety = line.split(',')
        if variety == line_variety[1:-1]:
            result.append(float(petal_length))
    if len(result):
        return sum(result) / len(result)
    return 0
```