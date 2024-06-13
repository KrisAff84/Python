import mysql.connector
from decouple import config

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config('DB_PASSWORD'),
    database="e_commerce_store"
)

cursor = db.cursor()

print("Products:")
print()
cursor.execute("SELECT * FROM products")

for product in cursor:
    print(f'ID: {product[0]}    Name: {product[1]}    Price: ${product[3]}')

customer_id = input("\nPlease enter your customer ID: ")

cursor.execute(
    "INSERT INTO orders (order_id, customer_id, total_price, order_date) VALUES (DEFAULT, %s, %s, DEFAULT)",
    (customer_id, 0.00)
) 
order_id = cursor.lastrowid

while True:
    product_id = input("\nPlease enter the ID of the product you would like to add to your cart: ")
    quantity = input("How many would you like to add to your cart? ")

    cursor.execute(
        "INSERT INTO order_items (order_id, product_id, quantity, price)"
        "VALUES (%s, %s, %s, (SELECT price FROM products WHERE product_id = %s))",
        (order_id, product_id, quantity, product_id)
    )
    
    add = input("Would you like to add any other items to your cart? (y/n) ")
    if 'y' in add.lower():
        continue
    else:
        break

print("Here are the items in your cart:")

cursor.execute("SELECT * FROM order_items WHERE order_id = %s", (order_id,))

for item in cursor:
    print(f'Product ID: {item[1]}    Quantity:{item[2]}    Price Per Item:${item[3]}   Sub Total: ${item[2] * item[3]}')

cursor.execute("SELECT total_price FROM orders WHERE order_id = %s", (order_id,))
total_price = cursor.fetchone()[0]

print(f'\nTotal: ${total_price}')

confirm = input("Would you like to confirm your order? (y/n) ")
if 'y' in confirm.lower():
    # Update the current date in the orders table
    cursor.execute(
        "UPDATE orders SET order_date = DEFAULT WHERE order_id = %s",
        (order_id,)
        )
    db.commit()
    print("Your order has been confirmed!")
else:
    db.rollback()
    print("Your order has been cancelled.")


