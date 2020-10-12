USE SAKILA;
/* 订单支付日汇总数据表 */
DROP TABLE IF EXISTS dm_payment_day;
CREATE TABLE dm_payment_day (SELECT DATE_FORMAT(payment_date,'%Y-%m-%d') as 日期,  SUM(amount) as 交易额  
FROM payment 
GROUP BY 日期 
ORDER BY 日期 
DESC);

/* 订单量日汇总数据表 */
DROP TABLE IF EXISTS dm_rental_day;
CREATE TABLE dm_rental_day (SELECT DATE_FORMAT(rental_date,'%Y-%m-%d') as 日期,  COUNT(rental_id) as 订单量 
FROM rental 
GROUP BY 日期 
ORDER BY 日期 
DESC);

/* 库存量日汇总数据表 */
DROP TABLE IF EXISTS dm_inventory_day;
CREATE TABLE dm_inventory_day (SELECT DATE_FORMAT(rental_date,'%Y-%m-%d') as 日期,  (SELECT COUNT(*) FROM inventory) as 库存量 
FROM rental
GROUP BY 日期 
ORDER BY 日期 
DESC);





