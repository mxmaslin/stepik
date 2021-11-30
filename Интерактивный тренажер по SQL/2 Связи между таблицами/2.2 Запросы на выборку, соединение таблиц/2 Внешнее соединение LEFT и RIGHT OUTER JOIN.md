# Внешнее соединение LEFT и RIGHT OUTER JOIN

## Задание

Вывести все жанры, которые не представлены в книгах на складе.

## Решение

```
select 
    name_genre
from
    genre g
left join
    book b
    on b.genre_id = g.genre_id
where
    b.book_id is null
```
