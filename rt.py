import sqlite3
conn=sqlite3.connect('ims.db')
cur=conn.cursor()
#cur.execute("create table customer (customer_id varchar (20),customer_name varchar (20),customer_address varchar(30),customer_email varchar(30))")
#cur.execute("create table product (product_id varchar(10),product_name varchar(10),stock int,price float,supplier_id varchar(10))")
#cur.execute("create table orders (order_id varchar(10),product_id varchar(10), customer_id varchar(10), quantity int) ")
#cur.execute("create table supplier (supplier_id varchar(10),supplier_name varchar(20),supplier_address varchar(30),supplier_email varchar(30))")



cur.execute("insert into customer (customer_id ,customer_name ,customer_address ,customer_email) values ('CUS1','PAVANI','SIDDIPET', 'PAVANISID@GMAIL.COM')")
cur.execute("insert into product (product_id ,product_name ,stock ,price ,supplier_id)  values ('PRO1','oneplus',4500,23000,'SUP1')")
cur.execute("insert into orders (order_id ,product_id , customer_id , quantity ) values ('ORD1','PRO1','CUS1', 3000)")
cur.execute("insert into supplier (supplier_id ,supplier_name ,supplier_address ,supplier_email)  values ('SUP1','SAI','HYD', 'SAIHYD@GMAIL.COM')")

conn.commit()