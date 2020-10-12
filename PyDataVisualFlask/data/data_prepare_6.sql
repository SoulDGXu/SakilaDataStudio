use sakila;
/**门店各项数据汇总表**/
drop table if exists dm_store_compare;
create table dm_store_compare (
select b1.store_id, b1.payment_date, sum(b1.amount) as store_amount,
		count(distinct b1.customer_id) as store_customer,
        count(b1.rental_id) as store_order,
        count(distinct b2.category_id) as store_film_category
from (
	select a1.staff_id, substr(a1.payment_date, 1, 4) as payment_date, a1.amount, a1.rental_id, a1.customer_id, a2.store_id
	from payment a1, staff a2
	where a1.staff_id = a2.staff_id) b1
left join 
	(
	select a3.rental_id, a3.inventory_id, a4.store_id, a4.film_id, a5.category_id
	from rental a3, inventory a4, film_category a5
	where a3.inventory_id = a4.inventory_id and a4.film_id = a5.film_id ) b2
on b1.rental_id = b2.rental_id
group by b1.store_id, b1.payment_date
);





/** 门店各项数据表 转换行列**/
drop table if exists dm_store_all;
create table dm_store_all (
	select *
	from (
		select "store_amount" as category, payment_date, 
				max(case when store_id=1 then store_amount else 0 end) as store_1,
				max(case when store_id=2 then store_amount else 0 end) as store_2
		from dm_store_compare
		group by payment_date
		UNION ALL
		select "store_customer" as category , payment_date, 
				max(case when store_id=1 then store_customer else 0 end) as store_1,
				max(case when store_id=2 then store_customer else 0 end) as store_2
		from dm_store_compare
		group by payment_date
		UNION ALL
		select "store_order" as category, payment_date, 
				max(case when store_id=1 then store_order else 0 end) as store_1,
				max(case when store_id=2 then store_order else 0 end) as store_2
		from dm_store_compare
		group by payment_date
		UNION ALL
		select "store_film_category" as category, payment_date, 
				max(case when store_id=1 then store_film_category else 0 end) as store_1,
				max(case when store_id=2 then store_film_category else 0 end) as store_2
		from dm_store_compare
		group by payment_date
		order by payment_date, category
	) c1
);