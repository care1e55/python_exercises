select m.name, l.name, a.name, a.rating
from albums a 
    inner join musicians m
        on a.musician_id = m.id
    inner join labels l 
        on a.label_id = l.id
where 
    l.name in ('Граммофон', 'Скрипичный ключ')
    and a.rating > 4
    and a.rating < 10
order by m.name