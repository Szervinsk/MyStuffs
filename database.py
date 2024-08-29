import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name='myapp.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.close()

    def connect(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def create_tables(self):
        self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT UNIQUE NOT NULL,
                username TEXT NOT NULL,
                FOREIGN KEY(username) REFERENCES users(username))''')
        
        self.conn.commit()

    def add_user(self, username, password):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_user(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def update_password(self, username, new_password):
        self.connect()
        self.cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        self.conn.commit()

    def add_session(self, session_id, username):
        self.connect()
        self.cursor.execute("INSERT INTO sessions (session_id, username) VALUES (?, ?)", (session_id, username))
        self.conn.commit()

    #def get_user_by_session(self, session_id):
       # self.connect()
       # self.cursor.execute("SELECT username FROM sessions WHERE session_id = ?", (session_id,))
       # print()
       # return self.cursor.fetchone()

    def get_user_by_session(self, session_id):
        self.connect()
        self.cursor.execute("SELECT username FROM sessions WHERE session_id = ?", (session_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def is_valid_session(self, session_id):
        return self.get_user_by_session(session_id) is not None

    def logout(self, session_id):
        self.connect()
        try:
            self.cursor.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
            self.conn.commit()
        finally:
            self.close()  # Certifique-se de fechar a conexão após a operação

