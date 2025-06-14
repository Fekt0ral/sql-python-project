-- Delete tables if exists
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;

-- Products create
CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    category TEXT
);

-- Orders create
CREATE TABLE Orders (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    order_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

-- Products data
INSERT INTO Products (id, name, price, category) VALUES
(1, 'Milk', 1.99, 'Dairy'),
(2, 'Cheese', 2.49, 'Dairy'),
(3, 'Bread', 0.99, 'Bakery'),
(4, 'Butter', 3.49, 'Dairy');

-- Orders data
INSERT INTO Orders (id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2025-01-10'),
(2, 2, 1, '2025-01-11'),
(3, 1, 1, '2025-01-12'),
(4, 4, 3, '2025-01-15'),
(5, 3, 4, '2025-01-20');