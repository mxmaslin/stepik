# Операция соединение, использование USING()

## Задание

Если в таблицах `supply` и `book` есть одинаковые книги, которые имеют равную цену,  вывести их название и автора, а также посчитать общее количество экземпляров книг в таблицах `supply` и `book`,  столбцы назвать `Название`, `Автор`  и `Количество`.

## Решение

```
select 
    q.title Название, q.name_author Автор, q.cnt + s.cnt Количество
from
    (
        select
            b.title title, a.name_author name_author, sum(b.amount) cnt, b.price price
        from
            book b
        join
            author a
            on a.author_id = b.author_id
        group by
            title, name_author, price
        having
            cnt > 0
    ) q
join
    (
        select
            title, author name_author, sum(amount) cnt, price
        from
            supply
        group by 
            title, name_author, price
        having
            cnt > 0
    ) s
    using(title, name_author, price)
```
