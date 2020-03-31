Выведите на печать все простые числа до 1000 через пробел.

Ограничьтесь одной строкой и 200 символами.

**Решение**

```python
print(' '.join([str(2)] + [str(n) for n in range(3, 1001, 2) if all([False if n % x == 0 else True for x in range(2, int(n ** 0.5 + 1))])]))
```