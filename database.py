import sqlite3
import os
import uuid
import datetime
import json

class DatabaseManager:
    def __init__(self, db_name='MyStuffs.db'):
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
        # self.cursor.execute('PRAGMA encoding = "UTF-8";')

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
                bio TEXT DEFAULT '',
                FOREIGN KEY(username) REFERENCES users(username)
    )''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                title TEXT DEFAULT '',
                content TEXT DEFAULT '',
                created_at TEXT DEFAULT '',
                is_favorite INTEGER DEFAULT 0,
                FOREIGN KEY(username) REFERENCES users(username)
            )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS lixeira (
                id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                title TEXT DEFAULT '',
                content TEXT DEFAULT '',
                created_at TEXT DEFAULT '',
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

        data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        notaId = str(uuid.uuid4())

        try:
            self.cursor.execute("INSERT INTO notes (id, username, title, content, created_at) VALUES (?,?,?,?, ?)", (notaId, username, title, content, data_atual))
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
            self.cursor.execute('SELECT title, content, created_at, id, is_favorite FROM notes WHERE username = ?', (username,))
            notes = self.cursor.fetchall()  # Retorna todas as notas

            if notes:  # Verifica se há resultados
                updated_notes = []  # Lista para armazenar as notas atualizadas
                for note in notes:
                    note = list(note)  # Converte a tupla para lista para permitir alterações

                    # Substitui as quebras de linha por <br> no conteúdo
                    content = note[1].replace('\r\n', '<br>')
                    note[1] = content  # Atualiza o conteúdo formatado

                    # Formata a data e a hora
                    data_hora = note[2]
                    partes = data_hora.split(' ') #separa aqui
                    if len(partes) == 2:
                        data = partes[0]  # Separa a data
                        hora = partes[1]  # Separa a hora

                        inv_data = f"{data[8:10]}-{data[5:7]}-{data[0:4]}"
                        note[2] = f"{inv_data} {hora}"  # Atualiza a data e hora no formato desejado
                    else:
                        note[2] = data_hora
                    # Formata a data no formato dia-mes-ano

                    updated_notes.append(note)  # Adiciona a nota atualizada à lista

                return updated_notes  # Retorna as notas formatadas
            else:
                return [] 
        except sqlite3.IntegrityError:
            print('opas')
        except sqlite3.Error as e:
            print(f"Erro ao adicionar usuário: {e}")
            self.conn.rollback()  # Reverte a transação em caso de erro
        finally:
            self.close()


    def edit_notes(self, username, id, title, content):
        self.connect()
        try:
            self.cursor.execute("UPDATE notes SET title = ?, content = ? , created_at = DATETIME('now', '-3 hours') WHERE id = ? AND username = ?", (title, content, id, username))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Nota não encontrada ou não foi alterada!")
            return False
        except sqlite3.Error as e:
            print("Nota não encontrada ou não foi alterada!")
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()


    def lixeira(self, id, username):
        print(f'{username}, {id}')
        
        self.connect()
        try:
            self.cursor.execute('SELECT title, content , created_at FROM notes WHERE username = ? AND id = ?', (username, id))
            change = self.cursor.fetchone()  # Pega apenas uma nota (tupla com title e content)

            if change:  
                title, content, created_at = change  

                self.cursor.execute("INSERT INTO lixeira (id, username, title, content,created_at) VALUES (?, ?, ?, ?, ?)", (id, username, title, content, created_at))
                self.cursor.execute('DELETE FROM notes WHERE id = ? AND username = ?', (id, username))
                self.conn.commit()  # Confirma a transação
                return True
            else:
                print(f"Nota com id {id} não encontrada para o usuário {username}")
                return False

        except sqlite3.Error as e:
            print(f"Erro ao mover para lixeira: {e}")
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()

    def delete_notes(self,id, username):
        self.connect()
        try:
            self.cursor.execute('DELETE FROM lixeira WHERE id = ? AND username = ?', (id, username))
            self.conn.commit()
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

    def restaura_note(self, id, username):
        self.connect()
        try:
            self.cursor.execute('SELECT title, content, created_at FROM lixeira WHERE username = ? AND id = ?', (username, id))
            change = self.cursor.fetchone() 

            if change:  # Verificar se a nota foi encontrada
                title, content, created_at = change  # Desempacotar o título e o conteúdo
            
                self.cursor.execute("INSERT INTO notes (id, username, title, content, created_at) VALUES (?, ?, ?, ?, ?)", (id, username, title, content, created_at))
                self.cursor.execute('DELETE FROM lixeira WHERE id = ? AND username = ?', (id, username))
                self.conn.commit() 
                return True
            else:
                print(f"Nota com id {id} não encontrada na lixeira para o usuário {username}")
                return False
            
        except sqlite3.IntegrityError:
            print('Erro de integridade ao restaurar a nota')
            return False
        except sqlite3.Error as e:
            print(f"Erro ao restaurar a nota: {e}")
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()


    def get_lixeira(self, username):
        self.connect()
        try:
            self.cursor.execute('SELECT title, content, created_at, id FROM lixeira WHERE username = ?', (username,))
            lixos = self.cursor.fetchall()  # Retorna todas as notas

            updated_lixos = []  # Lista para armazenar as notas atualizadas
            if lixos:
                for lixo in lixos:
                    lixo = list(lixo)  # Converte a tupla para lista para permitir alterações

                    # Substitui as quebras de linha por <br> no conteúdo
                    content = lixo[1].replace('\r\n', '<br>')
                    lixo[1] = content  # Atualiza o conteúdo formatado

                    updated_lixos.append(lixo)  # Adiciona a nota atualizada à lista
                return updated_lixos
            else:
                return []
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
    
    def starSet(self, id, isFavorite):
        self.connect()
        
        try:
            self.cursor.execute('UPDATE notes SET is_favorite = ? WHERE id = ?', (isFavorite, id))
            self.conn.commit() 
            print(f"Nota {id} atualizada com sucesso. is_favorite = {isFavorite}")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar a nota: {e}")
            self.conn.rollback() 
            return False
        finally:
            self.close()


