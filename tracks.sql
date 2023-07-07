select
    il.TrackId as trackid,
    sum(il.Quantity) as sells
from Invoice i
join InvoiceLine il on i.InvoiceId = il.InvoiceId
where i.InvoiceDate >= DATETIME('2010-01-01 00:00:00')
    and il.TrackId is not NULL
group by il.TrackId
order by sells desc, trackid asc;