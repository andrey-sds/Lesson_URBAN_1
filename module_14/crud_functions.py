import sqlite3


def initiate_db():
    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    connection.commit()
    connection.close()


def get_all_products(product_id):
    with sqlite3.connect('shop.db') as connection:
        cursor = connection.cursor()
        products = cursor.execute("SELECT  title, description, price FROM Products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
    return product

# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Витамин Д3+К2', 'Витамины в таблетках', 100);")
# connection.commit()
# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Омега-3', 'Капсулы', 200);")
# connection.commit()
# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Витамин Е', 'Таблетки', 300);")
# connection.commit()
# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Комплекс витаминов', 'Набор витаминов для здоровья', 400);")





