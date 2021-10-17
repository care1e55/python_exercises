select
    client_sum_order.id as id,
    avg(client_sum_order.sum_order) as avg_order
from (
    select
        c.id as id,
        sum(p.price*p.cnt) as sum_order
    from client c
    join "order" o on c.id = o.client_id
    join product p on o.id = p.order_id
    where c.id in (
        select
            orders_more_than_1000.client_id
        from (
            select
                o.client_id,
                p.order_id
            from product p
            join "order" o on p.order_id = o.id
                group by o.client_id, order_id
            having sum(p.cnt*p.price) > 1000
        ) as orders_more_than_1000
        group by client_id
        having count(orders_more_than_1000.order_id) >= 2
    )
    group by c.id, o.id
) as client_sum_order
group by client_sum_order.id
order by client_sum_order.id;