# Перекрестное соединение CROSS JOIN

## Задание

Есть список городов, хранящийся в таблице `city`:

| city_id | name_city |
|---|---|
| 1 | Москва |
| 2 | Санкт-Петербург |
| 3 | Владивосток |

Необходимо в каждом городе провести выставку книг каждого автора в течение 2020 года. Дату проведения выставки выбрать случайным образом. Создать запрос, который выведет город, автора и дату проведения выставки. Последний столбец назвать **Дата**. Информацию вывести, отсортировав сначала в алфавитном порядке по названиям городов, а потом по убыванию дат проведения выставок.

## Решение

```
select
    name_city, name_author, date_add('2020-01-01', interval floor(rand() * 365) day) Дата
from
    city, author
order by
    1, 3 desc
```
