# Вложенный запрос, оператор IN

## Задание

Вывести информацию (автора, книгу и количество) о тех книгах, количество экземпляров которых в таблице **book** не дублируется.

## Решение

```
select 
    author, title, amount
from
    book
where
    amount not in (
        select
            amount
        from 
            book
        group by
            amount
        having
            count(amount) > 1
    )
```
