Напишите функцию `fix_duplicates`, которая будет принимать на вход список строк-идентификаторов и исправлять их так, чтобы в результирующем списке не было дубликатов. Для этого она будет прибавлять к повторяющимся идентификаторам постфикс `_n`, где `n` - количество раз, сколько такой идентификатор уже встречался.

**Пример**

```python
ids = ["a", "b", "c", "a", "a", "d", "c"]
fix_duplicates(ids) == ['a', 'b', 'c', 'a_1', 'a_2', 'd', 'c_1']
```

**Решение**

```python
def fix_duplicates(ids):
    result = []
    for i, e in enumerate(ids):
        count = ids[:i].count(e)
        appendix = f'_{count}' if count else ''
        result.append(f'{e}{appendix}')
    return result
```
