select
       trim(COALESCE(e.FirstName, '') || ' ' || COALESCE(e.LastName, '')) as fullname,
       count(i.Total) as total
from Invoice i
join Customer c on c.CustomerId = i.CustomerId
join Employee e on e.EmployeeId = c.SupportRepId
where i.InvoiceDate >= DATETIME('2010-01-01 00:00:00')
and (e.FirstName is not NULL or e.LastName is not NULL)
group by e.EmployeeId
order by 2 desc
;

