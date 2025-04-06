import sqlite3


def create_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def products_1():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    products = [
        ("Молоко", 1.5, 20),
        ("Хлеб", 0.8, 50),
        ("Яйца", 2.3, 30)]
    cursor.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()

def display():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
    conn.close()


def up_product():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ?, quantity = ? WHERE id = ?", (2.0, 15, 1))
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (2,))
    conn.commit()
    conn.close()



if __name__ == "__main__":
    create_db()
    products_1()
    display()
    up_product()
    display()
    delete()
    display()