"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from north_data.func import read_csv

# connect to db
with psycopg2.connect(host="localhost", database='north', user='postgres', password='123456') as conn:
    with conn.cursor() as cur:

        # execute query
        cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                        read_csv("north_data/employees_data.csv"))
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        # execute query
        cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", read_csv("north_data/customers_data.csv"))
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        # execute query
        cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", read_csv("north_data/orders_data.csv"))
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        for row in rows:
            print(row)
conn.close()