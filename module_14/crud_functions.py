import sqlite3


conn = sqlite3.connect("shop.db")
cursor = conn.cursor()


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
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER
        );
        ''')
    connection.commit()
    connection.close()


def get_all_products(product_id):
    # with sqlite3.connect('shop.db') as connection:
    # cursor = conn.cursor()
    products = cursor.execute("SELECT  title, description, price FROM Products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    return product


def add_user(username, email, age):
    check_in_db = is_included(username)
    if check_in_db is True:
        cursor.execute(f'''
                INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)
                ''')
        conn.commit()
    else:
        return f'Пользователь с таким именем уже существует!'


def is_included(username):
    cursor.execute(f"SELECT id FROM Users WHERE username = ?", (username,))
    check_username = cursor.fetchone()
    if check_username is None:
        return True
    else:
        return False
# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Витамин Д3+К2', 'Витамины в таблетках', 100);")
# connection.commit()
# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Омега-3', 'Капсулы', 200);")
# connection.commit()
# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Витамин Е', 'Таблетки', 300);")
# connection.commit()
# cursor.execute("INSERT INTO Products(title, description, price) VALUES ('Комплекс витаминов', 'Набор витаминов для здоровья', 400);")


if __name__ == '__main__':
    initiate_db()



