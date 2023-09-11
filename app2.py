import sqlite3

# Create an in-memory database.
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

def init_db():
    # Users Table
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

    # Categories Table
    cursor.execute("""
    CREATE TABLE categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT
    )
    """)

    # Products Table
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

    # Orders Table
    cursor.execute("""
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        order_date TEXT,
        total_price REAL,
        shipping_address TEXT,
        city TEXT,
        state TEXT,
        zipcode TEXT,
        country TEXT,
        phone_number TEXT,
        status TEXT
    )
    """)

    # OrderDetails Table
    cursor.execute("""
    CREATE TABLE order_details (
        order_detail_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        price_at_purchase REAL
    )
    """)

    # Cart Table
    cursor.execute("""
    CREATE TABLE cart (
        cart_id INTEGER PRIMARY KEY,
        user_id INTEGER
    )
    """)

    # CartItems Table
    cursor.execute("""
    CREATE TABLE cart_items (
        cart_item_id INTEGER PRIMARY KEY,
        cart_id INTEGER,
        product_id INTEGER,
        quantity INTEGER
    )
    """)

    # Reviews Table
    cursor.execute("""
    CREATE TABLE reviews (
        review_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        user_id INTEGER,
        rating INTEGER,
        comment TEXT,
        date_posted TEXT
    )
    """)

    # Commit the changes.
    conn.commit()

# Initialize the database.
init_db()
def list_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]
print("Tables created:")
for table in list_tables():
    print(table)

print("Database schema initialized in memory!")

# This will keep the program running so you can inspect the in-memory database, if needed.
input("Press any key to exit...")
