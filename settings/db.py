import sqlite3

def create_user(user_id, user_name, first_name, last_name, chat_id, chat_title):
    try:
        sqlite_connection = sqlite3.connect('database.db')
        cursor = sqlite_connection.cursor()
        print("Успешное подключение к БД")

        cursor.execute("CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER NOT NULL UNIQUE, chat_title TEXT)")
        sqlite_connection.commit()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (user_id INTEGER NOT NULL UNIQUE, user_nickname TEXT NOT NULL, user_first_name TEXT,user_last_name TEXT)")
        sqlite_connection.commit()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS user_chats (user_id INTEGER, chat_id INTEGER)")
        sqlite_connection.commit()
        create_chat_query = "INSERT INTO chats (chat_id, chat_title) VALUES (?, ?)"
        create_user_query = "INSERT INTO users (user_id, user_nickname, user_first_name, user_last_name) VALUES (?, ?, ?, ?)"
        create_user_chat_query = "INSERT INTO user_chats (user_id, chat_id) VALUES (?, ?)"
        cursor.execute(create_chat_query, (chat_id, chat_title))
        sqlite_connection.commit()
        cursor.execute(create_user_query, (user_id, user_name, first_name, last_name))
        sqlite_connection.commit()
        cursor.execute(create_user_chat_query, (user_id, chat_id))
        sqlite_connection.commit()
    except sqlite3.Error as error:
        print("Ошибка:", error)
    finally:
        if (sqlite_connection):
            cursor.close()
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
