import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# Executes the query and returns the result as a Data Frame
def fetch_df(cursor, query: str) -> pd.DataFrame:
    cursor.execute(query)
    return pd.DataFrame(cursor.fetchall(),
                        columns=[col[0] for col in cursor.description])

# Prints a DataFrame without an index and with a header
def print_df(df: pd.DataFrame, title: str = "") -> None:
    if title:
        print(f"\n=== {title} ===")
    print(df.to_string(index=False))

# Reading .env variables
load_dotenv()

DB_CONFIG = {
    "host":     os.getenv("DB_HOST"),
    "user":     os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

try:
    with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:

            # Show all products
            all_products_sql = "SELECT * FROM Products"
            print_df(fetch_df(cursor, all_products_sql), "All products")

            # Show all orders
            all_products_sql = "SELECT * FROM Orders"
            print_df(fetch_df(cursor, all_products_sql), "All orders")

            # Show products more expensive $2
            expensive_sql = "SELECT name, price FROM Products WHERE price > 2.00"
            print_df(fetch_df(cursor, expensive_sql), "Products above $2")

            # Average product price
            cursor.execute("SELECT AVG(price) FROM Products")
            avg_price = cursor.fetchone()[0]
            print("\n=== Average product price ===")
            print(f"{avg_price:.2f}" if avg_price else "No data")

            # Most expensive order
            most_expensive_order_sql = """
                SELECT P.price * O.quantity AS total, O.order_date
                FROM Products P
                JOIN Orders O ON P.id = O.product_id
                ORDER BY total DESC
                LIMIT 1;
            """
            print_df(fetch_df(cursor, most_expensive_order_sql), "Most expensive order")

            # Number of products by categories
            count_by_category_sql = """
                SELECT category, COUNT(*) AS count
                FROM Products
                GROUP BY category;
            """
            print_df(fetch_df(cursor, count_by_category_sql), "Count by categories")

# Error catch
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Close connection
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()