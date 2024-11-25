import sqlite3

conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()
import sqlite3

conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS email_idx ON Users (email)")
# Очищаем таблицу, если там были данные
cursor.execute("DELETE FROM Users")
# Создаем новых пользователей
for i in range(1, 10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i*10}", 1000))
conn.commit()
# Обновляем баланс у каждого второго, начиная с первого
cursor.execute("SELECT id FROM Users") # выбираем все идентификаторы пользователей в бд
all_rec = cursor.fetchall()
for i, (rec_id,) in enumerate(all_rec):
    if i % 2 == 0:
        # Обновляем баланс у нужных пользователей
        cursor.execute("UPDATE Users SET balance = ? where  id = ?", (500, rec_id))
conn.commit()

#Удаляем каждую 3-ю запись в бд
cursor.execute("SELECT id FROM Users") # выбираем все идентификаторы пользователей в бд
all_rec = cursor.fetchall()
for i, (rec_id,) in enumerate(all_rec):
    if i % 3 == 0:
        # Удаляем каждую 3-ю запись
        cursor.execute("DELETE FROM Users  where  id = ?", (rec_id,))
conn.commit()

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
all_rec = cursor.fetchall()
for i, (user, email, age, bal) in enumerate(all_rec):
    print(f'Имя: {user} | Почта: {email} | Возраст: {age} | Баланс: {bal}')

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
conn.commit()

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(f'Количество пользователей в бд: {total_users}')

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(f'Сумма всех балансов пользователей в бд: {all_balances}')

cursor.execute("SELECT AVG(balance) FROM Users")
total_avg = cursor.fetchone()[0]
print(f'Расчет среднего баланса пользователей в бд с помощью запроса: {total_avg}')

print(f'Расчет среднего баланса на основании полученных данных из бд: {all_balances / total_users}')


conn.close()
