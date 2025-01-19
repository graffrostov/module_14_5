import sqlite3


def initiate_db():

    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL);
    """)

    for i in range(1, 10):

        check_prod = cursor.execute('SELECT * FROM Products WHERE id = ?', (i, ))

        if check_prod.fetchone() is None:
            cursor.execute(f'''INSERT INTO Products VALUES("{i}", "Продукт {i}", "Описание {i}", {i * 100})''')

    connection.commit()
    connection.close()

    connection_users = sqlite3.connect('users.db')
    cursor_users = connection_users.cursor()

    cursor_users.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL);
        """)


    connection_users.commit()
    connection_users.close()

def get_all_products():

    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products GROUP BY id')
    product_all = cursor.fetchall()

    connection.commit()
    connection.close()

    return product_all

def add_user(username, email, age):

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    if not is_included(username):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))


    connection.commit()
    connection.close()

def is_included(username):

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    if cursor.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone() is None:

        check_user = False

    else:

        check_user = True

    connection.commit()
    connection.close()

    return check_user


# initiate_db()
