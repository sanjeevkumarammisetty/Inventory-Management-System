import sqlite3

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

conn=sqlite3.connect('ims.db')
cn=conn.cursor()

def idgenerator(tab):
        
    cur = conn.cursor()
    idval = ''
    if tab=='CUSTOMER':
        idval = 'CUSTOMER_ID'
    if tab=='PRODUCT':
        idval = 'PRODUCT_ID'
    if tab=='ORDERS':
        idval = 'ORDER_ID'
    if tab=='SUPPLIER':
        idval = 'SUPPLIER_ID'
    print(tab,idval)
    cur.execute(f"SELECT {idval} FROM {tab}")
    new = cur.fetchall()
    cud = str(new[len(new)-1][0])
    for i in range(len(str(cud))):
        if cud[i].isnumeric():
            f = i
            break
    myint = cud[f:]
    myint = int(myint)+1
    return idval[0:3]+str(myint)



@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/show-customers')
def customer_show():
    conn=sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
        customer = {}
        customer['customer_id'] = i[0]
        customer['customer_name'] = i[1]
        customer['customer_address'] = i[2]
        customer['customer_email'] = i[3]
        data.append(customer)

    return render_template('showcustomers.html',data = data)


@app.route('/show-product')
def product_show():
    conn=sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from product")
    data = []
    for i in cn.fetchall():
        product = {}
        product['product_id'] = i[0]
        product['product_name'] = i[1]
        product['product_stock'] = i[2]
        product['product_price'] = i[3]
        product['product_supplier'] = i[4]
        data.append(product)

    return render_template('showproduct.html',data = data)


@app.route('/show-orders')
def orders_show():
    conn=sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from orders")
    data = []
    for i in cn.fetchall():
        orders = {}
        orders['order_id'] = i[0]
        orders['product_id'] = i[1]
        orders['customer_id'] = i[2]
        orders['quantity'] = i[3]
        data.append(orders)

    return render_template('showorders.html',data = data)


@app.route('/show-supplier')
def supplier_show():
    conn=sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from supplier")
    data = []
    for i in cn.fetchall():
        supplier = {}
        supplier['supplier_id'] = i[0]
        supplier['supplier_name'] = i[1]
        supplier['supplier_address'] = i[2]
        supplier['supplier_email'] = i[3]
        data.append(supplier)

    return render_template('showsupplier.html',data = data)

@app.route('/add-customer' ,methods = ['GET','POST'])
def addcustomer():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        customername = request.form.get("name")
        customeraddress =request.form.get("adress")
        customeremail = request.form.get("email")
        ID = idgenerator('CUSTOMER')
        cn.execute(f"insert into customer(customer_id,customer_name,customer_address,customer_email)values('{ID}','{customername}','{customeraddress}','{customeremail}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addcustomer.html')
    

@app.route('/add-products' ,methods = ['GET','POST'])
def addproducts():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        productname = request.form.get("name")
        stock =request.form.get("stock")
        price = request.form.get("price")
        supplierid = request.form.get("supplierid")
        ID = idgenerator('PRODUCT')
        cn.execute(f"insert into product(product_id,product_name,stock,price,supplier_id)values ('{ID}','{productname}',{stock},{price},'{supplierid}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addproducts.html')
    

@app.route('/add-orders' ,methods = ['GET','POST'])
def addorders():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        productid = request.form.get("productid")
        customerid =request.form.get("customerid")
        quantity = request.form.get("quantity")
        ID = idgenerator('ORDERS')
        cn.execute(f"insert into orders(order_id,product_id, customer_id, quantity) values ('{id}','{productid}','{customerid}', '{quantity}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addorders.html')
    

@app.route('/add-supplier' ,methods = ['GET','POST'])
def addsupplier():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        suppliername = request.form.get("suppliername")
        supplieraddress =request.form.get("supplieraddress")
        supplieremail = request.form.get("supplieremail")
        ID = idgenerator('SUPPLIER')
        cn.execute(f"insert into supplier(supplier_id,supplier_name,supplier_address,supplier_email) values ('{ID}','{suppliername}','{supplieraddress}','{supplieremail}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addsupplier.html')
    
@app.route('/update-customer' ,methods = ['GET','POST'])   
def updatecustomer():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        customerid = request.form.get("customerid")
        change =request.form.get("change")
        newvalue = request.form.get("newvalue")
        cn.execute(f"update customer set {change} = '{newvalue}' where customer_id = '{customerid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatecustomer.html')
    

@app.route('/update-product' ,methods = ['GET','POST'])   
def updateproduct():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        productid = request.form.get("productid")
        change =request.form.get("change")
        newvalue = request.form.get("newvalue")
        cn.execute(f"update product set {change} = '{newvalue}' where product_id = '{productid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateproduct.html')
    

@app.route('/update-orders' ,methods = ['GET','POST'])   
def updateorders():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        orderid = request.form.get("orderid")
        change =request.form.get("change")
        newvalue = request.form.get("newvalue")
        cn.execute(f"update orders set {change} = '{newvalue}' where order_id = '{orderid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateorders.html')
    

@app.route('/update-supplier' ,methods = ['GET','POST'])   
def updatesupplier():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        supplierid = request.form.get("supplierid")
        change =request.form.get("change")
        newvalue = request.form.get("newvalue")
        cn.execute(f"update supplier set {change} = '{newvalue}' where supplier_id = '{supplierid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatesuppliers.html')
    

@app.route('/delete-customer', methods=['GET', 'POST'])
def deletecustomer():
    if request.method == 'POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        customerid = request.form.get('customer_id')
        
        # Delete related records from ORDERS table
        cn.execute(f"DELETE FROM ORDERS WHERE CUSTOMER_ID = '{customerid}'")
        
        # Delete the customer
        cn.execute(f"DELETE FROM CUSTOMER WHERE CUSTOMER_ID = '{customerid}'")
        
        conn.commit()
        print('Data has been deleted successfully')
        return jsonify({'message': 'success'})
    else:
        return render_template('deletecustomer.html')

    


@app.route('/delete-product', methods=['GET', 'POST'])
def deleteproduct():
    if request.method == 'POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        product_id = request.form.get('product_id')
        
        # Delete related records from ORDERS table
        cn.execute(f"DELETE FROM ORDERS WHERE PRODUCT_ID = '{product_id}'")
        
        # Delete the product
        cn.execute(f"DELETE FROM PRODUCT WHERE PRODUCT_ID = '{product_id}'")
        
        conn.commit()
        print('Data has been deleted successfully')
        return jsonify({'message': 'success'})
    else:
        return render_template('deleteproduct.html')


@app.route('/delete-orders', methods=['GET', 'POST'])
def deleteorders():
    if request.method == 'POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        order_id = request.form.get('order_id')
        
        # Delete the order
        cn.execute(f"DELETE FROM ORDERS WHERE ORDER_ID = '{order_id}'")
        
        conn.commit()
        print('Data has been deleted successfully')
        return jsonify({'message': 'success'})
    else:
        return render_template('deleteorders.html')


@app.route('/delete-supplier', methods=['GET', 'POST'])
def deletesupplier():
    if request.method == 'POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        supplier_id = request.form.get('supplier_id')
        
        # Delete the supplier
        cn.execute(f"DELETE FROM SUPPLIER WHERE SUPPLIER_ID = '{supplier_id}'")
        
        conn.commit()
        print('Data has been deleted successfully')
        return jsonify({'message':'success'})
    else:
        return render_template('deletesupplier.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)

