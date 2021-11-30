# Соединение INNER JOIN

## Задание

Вывести название, жанр и цену тех книг, количество которых больше 8, в отсортированном по убыванию цены виде.

## Решение

```
select 
    b.title, g.name_genre, b.price
from 
    book b
join
    genre g
    on g.genre_id = b.genre_id
where 
    b.amount > 8
order by 
    b.price desc
```
