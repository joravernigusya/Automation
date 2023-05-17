# -*- coding: utf-8 -*-
import mysql.connector as mysql

db = mysql.connect(host="localhost",
                   user="root",
                   passwd="yan123654",
                   database='test_db_2')

cursor = db.cursor()

cursor.execute("CREATE TABLE orders "
               "(ord_no INT UNIQUE, "
               "purch_amt FLOAT, "
               "ord_date DATE, "
               "customer_id INT, "
               "salesman_id INT)")

sql = "INSERT INTO orders " \
      "(ord_no, purch_amt, ord_date, customer_id, salesman_id) " \
      "VALUES (%s, %s, %s, %s, %s)"
val = [
    (70001, 150.5, '2012-10-05', 3005, 5002),
    (70009, 270.65, '2012-09-10', 3001, 5005),
    (70002, 65.26, '2012-10-05', 3002, 5001),
    (70004, 110.5, '2012-08-17', 3009, 5003),
    (70007, 948.5, '2012-09-10', 3005, 5002),
    (70005, 2400.6, '2012-07-27', 3007, 5001),
    (70008, 5760, '2012-09-10', 3002, 5001),
    (70010, 1983.43, '2012-10-10', 3004, 5006),
    (70003, 2480.4, '2012-10-10', 3009, 5003),
    (70012, 250.45, '2012-06-27', 3008, 5002),
    (70011, 75.29, '2012-08-17', 3003, 5007),
    (70013, 3045.6, '2012-04-25', 3002, 5001)
]

cursor.executemany(sql, val)

db.commit()

# Вывод номера заказа, даты заказа и количество для каждого заказа, который
# продал продавец под номером 5002.
cursor.execute(
    "SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id = 5002")
result = cursor.fetchall()
for row in result:
    print("Order Number:", row[0])
    print("Order Date:", row[1])
    print("Purchase Amount:", row[2])

# Уникальные id продавца (salesman_id).
cursor.execute(
    "SELECT DISTINCT salesman_id FROM orders ORDER BY salesman_id ASC")
result = cursor.fetchall()
for row in result:
    print(row[0])

# Вывод по порядку данные о дате заказа, id продавца, номер заказа, количество.
cursor.execute("SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders ORDER BY ord_date, salesman_id, ord_no, purch_amt")
result = cursor.fetchall()
for row in result:
    print("Order Date:", row[0])
    print("Salesman ID:", row[1])
    print("Order Number:", row[2])
    print("Purchase Amount:", row[3])

# Заказы между 70001 и 70007.
cursor.execute("SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007")
result = cursor.fetchall()
for row in result:
    print(row)
