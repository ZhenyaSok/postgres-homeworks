-- SQL-команды для создания таблиц

CREATE TABLE customers
-- клиенты
(
	customer_id VARCHAR(50) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL,

);

CREATE TABLE employees
--сотрудники
(
	employee_id SERIAL PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text,
);

CREATE TABLE orders
--заказы. связь и с сотрудниками и с клиентами
(
	order_id SERIAL PRIMARY KEY
	customer_id varchar(100) NOT NULL
	employee_id int
	order_date date
	ship_city varchar(100) NOT NULL
);
