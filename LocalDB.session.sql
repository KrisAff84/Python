INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (4, 4, 1, (SELECT price FROM products WHERE product_id = 4));

SELECT * FROM customers;

BEGIN TRANSACTION;
INSERT INTO orders VALUES (DEFAULT, 1002, 0, DEFAULT);
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (MAX(order_id), 11, 2, (SELECT price FROM products WHERE product_id = 11));
COMMIT TRANSACTION;
END TRANSACTION;

SELECT * FROM orders;

SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = "orders";



