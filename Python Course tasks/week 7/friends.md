Напишите функцию `friends`, которая из списка пар друзей сделает словарь, в котором для каждого человека будут перечислены все его друзья.

**Пример**

```python
>>> print(friends([("Ivan", "Maria"), ("Ella", "Ivan"), ("Ivan", "Oleg")])

{"Ivan":["Maria", "Ella", "Oleg"], "Ella":["Ivan"], "Maria": ["Ivan"], "Oleg": ["Ivan"]}
```

**Решение**

```python
def friends(pairs):
    result = dict()
    [result.update({first: result.get(first, []) + [second], second: result.get(second, []) + [first]}) for first, second in pairs]
    return result
```
