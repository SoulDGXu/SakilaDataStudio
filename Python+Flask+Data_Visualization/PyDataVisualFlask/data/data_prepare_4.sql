use sakila;
drop table if exists dm_customer_address;
create table dm_customer_address(
select  rental_id, rental_date, inventory_id, return_date, staff_id, c1.*
from (
	select b1.customer_id, b1.address_id, b1.address, b1.district, b1.location, b1.city_id, b1.city, b1.country_id, b1.country
	from (
		select a1.*, a2.city, a2.country_id, a3.country, a4.customer_id
		from address a1, city a2, country a3, customer a4
		where a1.city_id = a2.city_id and a2.country_id = a3.country_id and a1.address_id = a4.address_id
		order by a1.address_id) b1) c1
right join rental 
on c1.customer_id = rental.customer_id
);

/* 查询各国家/地区的客户数量*/
select country, count(distinct rental_id) as customer_num
from dm_customer_address
group by country_id
order by country_id
;

/* 查询中国各省市的客户数量*/
select district, count(distinct rental_id) as customer_num
from dm_customer_address
where country="China" 
group by district
order by district
;

/* 查询中国山东省各城市的客户数量*/
select city, count(distinct rental_id) as customer_num
from dm_customer_address
where country="China" and district="Shandong"
group by city
order by city
;
