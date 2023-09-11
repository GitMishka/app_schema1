import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

def init_db():
    # Users
    cursor.execute("""
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        address TEXT,
        city TEXT,
        state TEXT,
        zipcode TEXT,
        country TEXT,
        phone_number TEXT
    )
    """)

    # Products
    cursor.execute("""
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        category_id INTEGER,
        name TEXT,
        description TEXT,
        price REAL,
        stock_quantity INTEGER,
        image_url TEXT,
        date_added TEXT
    )
    """)

    # Categories
    cursor.execute("""
    CREATE TABLE categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT
    )
    """)

    # ... add other tables similarly ...

    conn.commit()

init_db()
