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
            self.conn.text_factory = str
            self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def create_tables(self):
        self.connect()
        self.cursor.execute('PRAGMA encoding = "UTF-8";')

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
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS perfil (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                foto BLOB,
                nome_pessoal TEXT DEFAULT '', 
                email TEXT DEFAULT '', 
                location TEXT DEFAULT '',
                bio VARCHAR(200) DEFAULT '',
                FOREIGN KEY(username) REFERENCES users(username)
    )''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                title TEXT DEFAULT '',
                content VARCHAR(1935),
                created_at TIMESTAMP DEFAULT (DATETIME('now', '-3 hours')),
                FOREIGN KEY(username) REFERENCES users(username)
            )''')

        self.conn.commit()

    def add_user(self, username, password):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.cursor.execute('INSERT INTO perfil (username) VALUES (?)', (username,))
            
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except sqlite3.Error as e:
            print(f"Erro ao adicionar usuário: {e}")
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()  # Certifique-se de fechar a conexão após a operação

    def add_note(self, username, title, content):
        self.connect()
        print('conectei')
        try:
            self.cursor.execute("INSERT INTO notes (username, title, content) VALUES (?,?,?)", (username, title, content))
            self.conn.commit()
            print('cheguei aqui')
            return True
        except sqlite3.IntegrityError:
            print('opas')
            return False
        except sqlite3.Error as e:
            print(f"Erro ao adicionar usuário: {e}")
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()
    
    def get_notes(self, username):
        self.connect()
        try:
            self.cursor.execute('SELECT title, content, created_at FROM notes WHERE username = ?', (username,))
            notes = self.cursor.fetchall()  # Retorna todas as notas
            return notes
        except sqlite3.Error as e:
            print(f"Erro ao buscar notas: {e}")
            return []
        finally:
            self.close()

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

    def get_user_by_session(self, session_id):
        self.connect()
        self.cursor.execute("SELECT username FROM sessions WHERE session_id = ?", (session_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None #result[0] é o username do cara

    def is_valid_session(self, session_id):
        return self.get_user_by_session(session_id) is not None

    def update_perfil(self, username, nome, email, location, bio):
        self.connect()
        try:
            self.cursor.execute('''
                UPDATE perfil 
                SET nome_pessoal = ?, email = ?, location = ?, bio = ?
                WHERE username = ?
            ''', (nome, email, location, bio, username))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(f"Erro ao atualizar perfil: {e}")
            return False

    def get_perfil(self, username):
        self.connect()
        self.cursor.execute('SELECT nome_pessoal, email, location, bio FROM perfil WHERE username = ?', (username,))
        perfil = self.cursor.fetchone()
        print(perfil)
        return perfil


    def logout(self, session_id):
        self.connect()
        try:
            self.cursor.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
            self.conn.commit()
        finally:
            self.close()  # Certifique-se de fechar a conexão após a operação

    def delete_user(self, username, session_id):
        self.connect()
        try:
            self.cursor.execute("DELETE FROM perfil WHERE username = ?", (username,))
            self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            self.cursor.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao excluir usuário: {e}")
            self.conn.rollback()  # Reverte a transação em caso de erro
        finally:
            self.close()  # Certifique-se de fechar a conexão após a operação



