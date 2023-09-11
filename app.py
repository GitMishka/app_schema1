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


    conn.commit()

init_db()

def add_user(first_name, last_name, email, password, address, city, state, zipcode, country, phone_number):
    cursor.execute("INSERT INTO users (first_name, last_name, email, password, address, city, state, zipcode, country, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, email, password, address, city, state, zipcode, country, phone_number))
    conn.commit()

def add_product(category_id, name, description, price, stock_quantity, image_url, date_added):
    cursor.execute("INSERT INTO products (category_id, name, description, price, stock_quantity, image_url, date_added) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (category_id, name, description, price, stock_quantity, image_url, date_added))
    conn.commit()

def get_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


def main():
    while True:
        print("1. Add User")
        print("2. Add Product")
        print("3. View Products")
        print("4. View Users")

        choice = input("Choose an option: ")

        if choice == "1":
            # Ask user for inputs and then call add_user()
            pass  # Fill in with actual functionality
        elif choice == "2":
            # Ask user for inputs and then call add_product()
            pass  # Fill in with actual functionality
        elif choice == "3":
            products = get_products()
            for product in products:
                print(product)
        elif choice == "4":
            users = get_users()
            for user in users:
                print(user)

if __name__ == "__main__":
    main()
