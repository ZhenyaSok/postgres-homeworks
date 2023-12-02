-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id varchar(15) PRIMARY KEY,
	company_name varchar(50),
	contact_name varchar(50)
);

CREATE TABLE employees
--сотрудники
(
	employee_id int PRIMARY KEY,
	first_name varchar(40) NOT NULL,
	last_name varchar(40) NOT NULL,
	title varchar(200) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE orders
-заказы, имеют связи
(
	order_id SERIAL PRIMARY KEY,
	customer_id varchar(30) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar(30) NOT NULL
);
