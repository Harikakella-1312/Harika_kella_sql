-- 1.Make a table customers with name, email, and registration date.

create table c_customers (
customer_id serial primary key,
name varchar(100) not null,
email varchar(50) unique not null,
registration_date date not null
);


--2. Create a table products with name, price, and available stock.
create table prod_products (
name varchar(100) not null,
product_id int primary key,
price int,
available_stock varchar(100) not null);


-- 3.Design a table orders that links each order to a customer and stores order date.
create table o_order (
order_id serial primary key,
customer_id int not null,
order_date date not null,
foreign key (customer_id) references c_customers(customer_id))

-- 4.Build order_items to link products to orders and include quantity.
create table order_items(
order_items_id int not null,
product_id int not null,
quantity int not null check (quantity>0),
foreign key (order_items_id) references o_order(order_id),
foreign key (product_id) references prod_products(product_id));

-- 5. .Add a reviews table where customers rate and comment on products.
create table re_reviews(
reviews_id serial primary key,
product_id int not null,
customers_rate int not null,
comments varchar(100) not null,
foreign key (product_id) references prod_products(product_id));

--6. Create a view to list recent orders (last 7 days) with customer name.

create view orders_recent as
select o.order_id,
c.name as customer_name,
o.order_date
from o_order o
join c_customers c
on c.customer_id=o.customer_id
where o.order_date>= current_date - interval '7 days'


-- 7. 7.Create a view to list products that are out of stock.

create view list_of_products
as select p.product_id, p.name, oi.quantity
from prod_products p
join order_items oi on
oi.product_id = p.product_id
where oi.quantity = 0;


-- 8. Make a view showing average product rating using the reviews table.

create view avg_prod_rating as
select avg(customers_rate), product_id
from re_reviews
group by product_id;

-- 9. 9.Build a view that shows each customer’s total number of orders.
create view total_no_of_orders
as select c.name, count(o.order_id)
from c_customers c
join o_order o
on c.customer_id = o.order_id
group by c.name;


-- 10.Create a materialized view that shows total sales per month.

create materialized view total_sale
as select to_char(o.order_date,'%y-%m') as month,
sum(p.price), oi.product_id
from order_items oi
join o_order o 
on o.order_id = oi.order_items_id
join prod_products p
on p.product_id = oi.product_id
group by oi.product_id, to_char(o.order_date,'%y-%m')
order by month;

-- 11. Make one that lists each product’s average rating and number of reviews.

create view product_rate_summary 
as select count(r.reviews_id) as no_of_reviews,
avg(r.customers_rate) as avg_rating
from re_reviews r

--12. Create one that shows how much each customer has spent so far.
create view customer_spendings
as select o.customer_id, 
sum(p.price * oi.quantity) as total_spent_amount
from order_items oi
join prod_products p
on p.product_id = oi.product_id
join o_order o
on o.order_id = oi.order_items_id 
group by o.customer_id;




