# Вложенный запрос, операторы ANY и ALL

## Задание

Вывести информацию о книгах(автор, название, цена), цена которых меньше самой большой из минимальных цен, вычисленных для каждого автора.

## Решение

```
select 
    author, title, price
from
    book b
where
    price < all(
        select
            max(price)
        from
            book b1
        where
            b1.author = b.author
    )
```
