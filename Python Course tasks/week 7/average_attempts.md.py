Даны два списка. В первом записи вида: id на Степике, id задачи, количество попыток. Во втором: id на Степике и имя. Напишите функцию, которая посчитает для каждого человека среднее число попыток и сделает словарь с результатами.
 
**Пример**

```python
attempts = [(1232323323415, 1, 43),
            (1232323323415, 2, 3),
            (114349, 1, 0)
            ]
names = [(114349, "Arkady"),
         (1232323323415, "Random")]

average_attempts(attempts, names) == {'Random': 23.0, 'Arkady': 0.0}
```

**Решение**

```python
def average_attempts(attempts, names):
    d = {}
    for name in names:
        grades = [attempt[-1] for attempt in attempts if name[0] == attempt[0]]
        if grades:
	        avg = sum(grades) / len(grades)
    	    d[name[1]] = avg
    return d
```