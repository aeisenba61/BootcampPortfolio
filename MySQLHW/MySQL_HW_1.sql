use sakila; 
-- 1a. Display the first and last names of all actors from the table actor.
select first_name, Last_name 
FROM actor
ORDER by Last_Name;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select CONCAT(UPPER(first_name), ' ', UPPER(Last_name)) AS Full_Name
FROM actor
ORDER by Last_name;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
select actor_id, first_name, Last_name
FROM actor
where first_name = 'Joe';

-- 2b. Find all actors whose last name contain the letters GEN:
select actor_id, first_name, Last_name
FROM actor
where last_name like '%GEN%';

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select actor_id, first_name, Last_name
FROM actor
where last_name like '%LI%'
order by last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country
FROM country
where country in ('Afghanistan', 'Bangladesh', 'China');

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(50) AFTER first_name;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
ALTER TABLE actor
MODIFY COLUMN middle_name blob AFTER first_name;

-- 3c. Now delete the middle_name column.
ALTER TABLE actor
DROP COLUMN middle_name;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, count(last_name) as COUNTER
FROM actor
group by last_name
order by COUNTER desc;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, count(last_name) as COUNTER
FROM actor
group by last_name
having count(last_name) > 1
order by COUNTER desc;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
update actor 
set first_name = 'Harpo'
where first_name = 'Groucho' and last_name = 'Williams';

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
update actor 
set first_name = 'Mucho Groucho'
where first_name = 'Harpo' and last_name = 'Williams';

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
CREATE TABLE `address` (
  `address_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `address` varchar(50) NOT NULL,
  `address2` varchar(50) DEFAULT NULL,
  `district` varchar(20) NOT NULL,
  `city_id` smallint(5) unsigned NOT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `location` geometry NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`address_id`),
  KEY `idx_fk_city_id` (`city_id`),
  SPATIAL KEY `idx_location` (`location`),
  CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT first_name, last_name, address
FROM staff a
INNER JOIN address b
on a.address_id = b.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT first_name, last_name, total
FROM staff a
INNER JOIN (SELECT staff_id, SUM(amount) as total FROM payment
			where payment_date like '2005-08%'
			group by staff_id) b
on a.staff_id= b.staff_id
;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select title, sum(actor_id) as num_actors FROM film_actor a
INNER JOIN film b 
	on a.film_id = b.film_id
group by a.film_id
order by title asc; 

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT 'Hunchback Impossible' as Title, COUNT(*) as Copies FROM inventory where film_ID = (SELECT film_ID FROM Film where title = 'Hunchback Impossible');

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name ![Total amount paid](Images/total_payment.png)
SELECT concat(first_name, ' ', last_name) as full_name, total_amt_paid
FROM customer a
inner join (SELECT customer_id, sum(amount) as total_amt_paid FROM payment group by customer_id) b
	on a.customer_id = b.customer_id
order by last_name asc;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT title FROM film
where language_id = (SELECT language_id 
					 FROM language 
                     where name = 'english')
and (title like 'K%'
or title like 'Q%');

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT concat(first_name, ' ', last_name) as name 
FROM Actor 
where actor_id in (select actor_id 
				   FROM film_actor 
				   where film_id in (select film_id 
									 FROM film 
									 where title = 'Alone Trip'));

SELECT concat(first_name, ' ', last_name) as name 
FROM Actor 
where actor_id in (select actor_id 
				   FROM film_actor 
				   where film_id in (select film_id 
									 FROM film 
									 where title = 'Alter Victory'));
-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT concat(first_name, ' ', last_name) as name, email
FROM customer 
where address_id in (SELECT address_id 
					 FROM Address 
                     WHERE city_id in (select city_id 
									   FROM city
                                       where country_id in (SELECT country_id 
															from country 
                                                            where country = 'canada')));

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
SELECT title 
FROM film 
where film_id in (SELECT film_id 
				  FROM film_category
                  where category_id in (SELECT category_id 
										FROM category 
										where name = 'family'))
;

-- 7e. Display the most frequently rented movies in descending order.
SELECT title, count(c.inventory_id) as num_rented 
FROM film a
left join inventory b
	on a.film_id = b.film_id
left join rental c
	on b.inventory_id = c.inventory_id
group by a.title
order by num_rented desc;
    
-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT a.store_id, SUM(c.amount) as total_sales
FROM store a
LEFT join customer b
	on a.store_id = b.store_id
LEFT join payment c
	on b.customer_id = c.customer_id
group by a.store_ID;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT store_id, city, country 
FROM store a
inner join address b
	on a.address_id = b.address_id
inner join city c
	on b.city_id = c.city_id
inner join country d
	on c.country_id = d.country_id
;

-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT name as Genre, SUM(amount) as Gross_Revenue
FROM category a
inner join film_category b 
	on a.category_id = b.category_id
inner join inventory c
	on b.film_id = c.film_id
inner join rental d
	on c.inventory_id = d.inventory_id
inner join payment e
	on d.rental_id = e.rental_id
group by a.name
order by Gross_Revenue desc 
limit 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
create view top5Genres AS 
SELECT name as Genre, SUM(amount) as Gross_Revenue
FROM category a
inner join film_category b 
	on a.category_id = b.category_id
inner join inventory c
	on b.film_id = c.film_id
inner join rental d
	on c.inventory_id = d.inventory_id
inner join payment e
	on d.rental_id = e.rental_id
group by a.name
order by Gross_Revenue desc 
limit 5;

-- 8b. How would you display the view that you created in 8a?
SELECT * FROM top5Genres
;

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view top5genres
;
