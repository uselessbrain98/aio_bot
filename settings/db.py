import sqlite3


def connect_to_database():
    try:
        sqlite_connection = sqlite3.connect('database.db')
        sqlite_connection.row_factory = sqlite3.Row
        print("Успешное подключение к БД")
        if sqlite_connection:
            with sqlite_connection:
                cursor = sqlite_connection.cursor()

                cursor.execute("CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY, chat_title TEXT)")
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, user_nickname TEXT NOT NULL, user_first_name TEXT, user_last_name TEXT)")
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS user_chats (user_id INTEGER, chat_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(user_id), FOREIGN KEY(chat_id) REFERENCES chats(chat_id))")
        return sqlite_connection, cursor
    except sqlite3.Error as error:
        print("Ошибка при подключении к БД:", error)
        return None


def create_user(cursor, sqlite_connection, user_id, user_name, first_name, last_name, chat_id, chat_title):
    update_user_query = "UPDATE users SET user_nickname = ?, user_first_name = ?, user_last_name = ? WHERE user_id = ?"
    create_chat_query = "INSERT INTO chats (chat_id, chat_title) VALUES (?, ?)"
    create_user_query = "INSERT INTO users (user_id, user_nickname, user_first_name, user_last_name) VALUES (?, ?, ?, ?)"
    create_user_chat_query = "INSERT INTO user_chats (user_id, chat_id) VALUES (?, ?)"

    try:
        if cursor:
            user_exist = get_user(user_id, cursor=cursor, sqlite_connection=sqlite_connection)
            chat_exist = get_chats(chat_id, cursor=cursor, sqlite_connection=sqlite_connection)
            if user_exist and chat_exist:
                cursor.execute(update_user_query, (user_name, first_name, last_name, user_id))
                return f"Пользователь с user_id ={user_id} уже существует. Его данные обновлены."
            elif user_exist and not chat_exist:
                cursor.execute(update_user_query, (user_name, first_name, last_name, user_id))
                cursor.execute(create_chat_query, (chat_id, chat_title))
                cursor.execute(create_user_chat_query, (user_id, chat_id))
                return f"Пользователь с user_id ={user_id} уже существует. Его данные обновлены + добавлен новый чат"
            elif not user_exist and chat_exist:
                cursor.execute(create_user_query, (user_id, user_name, first_name, last_name))
                return f"Создан пользователь с user_id= {user_id}"
            else:
                cursor.execute(create_chat_query, (chat_id, chat_title))
                cursor.execute(create_user_query, (user_id, user_name, first_name, last_name))
                cursor.execute(create_user_chat_query, (user_id, chat_id))
                return f"Данные успешно добавлены в БД: user_id = {user_id}, user_chats = {chat_id}"
    except sqlite3.Error as error:
        print("Общая ошибка SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.commit()
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def get_user(user_id, cursor=None, sqlite_connection=None):
    if sqlite_connection and cursor:
        try:
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            user = cursor.fetchone()
            return user
        except sqlite3.Error as error:
            print("Ошибка при получении пользователя:", error)
    else:
        try:
            connection, cursor = connect_to_database()
            if connection and cursor:
                print("приступаю к извлечению")
                cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
                user = cursor.fetchone()
                connection.close()
                print("Закрыл соединение")
                return user
        except sqlite3.Error as error:
            print("Ошибка при получении пользователя:", error)


def get_user_chats(user_id, chat_id, cursor=None, sqlite_connection=None):
    if sqlite_connection and cursor:
        try:
            cursor.execute("SELECT * FROM user_chats WHERE user_id = ? AND chat_id = ?", (user_id, chat_id))
            user_chat = cursor.fetchone()
            return user_chat
        except sqlite3.Error as error:
            print("Ошибка при получении чатов пользователя:", error)
    else:
        try:
            connection, cursor = connect_to_database()
            if connection and cursor:
                print("приступаю к извлечению чатов пользователя")
                cursor.execute("SELECT * FROM user_chats WHERE user_id = ? AND chat_id = ?", (user_id, chat_id))
                user_chat = cursor.fetchone()
                connection.close()
                print("Закрыл соединение")
                return user_chat
        except sqlite3.Error as error:
            print("Ошибка при получении пользователя:", error)


def get_chats(chat_id, cursor=None, sqlite_connection=None):
    if sqlite_connection and cursor:
        try:
            cursor.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,))
            chat = cursor.fetchone()
            return chat
        except sqlite3.Error as error:
            print("Ошибка при получении чата:", error)
    else:
        try:
            connection, cursor = connect_to_database()
            if connection and cursor:
                print("приступаю к извлечению чата")
                cursor.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,))
                chat = cursor.fetchone()
                connection.close()
                print("Закрыл соединение")
                return chat
        except sqlite3.Error as error:
            print("Ошибка при получении чата:", error)

