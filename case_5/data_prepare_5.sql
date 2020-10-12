use sakila;
drop table if exists dm_month_store_amount;
create table dm_month_store_amount(
select c1.payment_date, 
		max(case when c1.store_id = 1 then c1.store_amount else 0 end) as store_1,
        max(case when c1.store_id = 2 then c1.store_amount else 0 end) as store_2
from (
	select  b1.store_id, substr(b1.payment_date, 1, 7) as payment_date, sum(b1.amount) as store_amount   /* DATE_FORMAT(payment_date,'%Y-%m') as payment_date */
	from (
		select a1.staff_id, a1.payment_date, a1.amount, a2.store_id
		from payment a1, staff a2
		where a1.staff_id = a2.staff_id
	) b1
	group by b1.store_id, substr(b1.payment_date, 1, 7)
) c1
group by c1.payment_date
);