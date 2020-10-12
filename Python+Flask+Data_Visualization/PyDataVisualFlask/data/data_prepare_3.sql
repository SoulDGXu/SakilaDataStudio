USE SAKILA;
/* 影片信息表 */
DROP TABLE IF EXISTS film_information_full;
CREATE TABLE film_information_full (
SELECT c1.*, c2.category_id, c2.category_name 
FROM (
	SELECT b1.日期, b2.* 
	FROM ( 
		SELECT a1.*, a2.film_id 
		FROM ( SELECT rental_id, inventory_id, DATE_FORMAT( rental_date, '%Y-%m-%d' ) AS 日期 FROM rental ) a1
		LEFT JOIN ( SELECT inventory_id, film_id FROM inventory ) a2 
		ON a1.inventory_id = a2.inventory_id 
		) b1
	LEFT JOIN (
		SELECT a3.*, a4.NAME as language_name
		FROM ( 
			SELECT film_id, language_id, rental_duration, rental_rate, length, replacement_cost, rating FROM film ) a3
            LEFT JOIN ( SELECT language_id, NAME FROM LANGUAGE ) a4 
            ON a4.language_id = a3.language_id 
			) b2 
	ON b2.film_id = b1.film_id 
    ) c1
LEFT JOIN ( 
	SELECT a5.*, a6.category_name 
	FROM ( SELECT film_id, category_id FROM film_category ) a5
	LEFT JOIN ( SELECT category_id, NAME AS category_name FROM category ) a6 
	ON a5.category_id = a6.category_id 
	) c2 
ON c1.film_id = c2.film_id 
);

/* 租借影片的订单量 */
SELECT 日期, COUNT(*) AS 订单量
FROM film_information_full
GROUP BY 日期
ORDER BY 日期
ASC
;

/* 不同类型的影片订单量 */
SELECT category_name AS 电影类型, COUNT(*) AS 订单量
FROM film_information_full
GROUP BY category_name
ORDER BY category_name 
;

/* 不同等级的影片订单量 */
SELECT rating AS 电影等级, COUNT(*) AS 订单量
FROM film_information_full
GROUP BY rating
ORDER BY rating 
;

/* 不同租赁时长的影片订单量 */
SELECT rental_duration AS 电影租赁时长, COUNT(*) AS 订单量
FROM film_information_full
GROUP BY rental_duration
ORDER BY rental_duration 
;

/* 不同租赁价格的影片订单量 */
SELECT rental_rate AS 电影租赁价格, COUNT(*) AS 订单量
FROM film_information_full
GROUP BY rental_rate
ORDER BY rental_rate 
;
