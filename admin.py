import sqlite3
import os
import uuid
import datetime
import json

class Administration:
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

    def getTables(self):

        self.connect()
        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()
        print(users)
        self.cursor.execute('SELECT * FROM sessions')
        sessoes = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM perfil')
        perfis = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM notes')
        notes = self.cursor.fetchall()
        self.cursor.execute('SELECT * FROM lixeira')
        lixos = self.cursor.fetchall()

        return users, sessoes, perfis, notes, lixos
    
    def update_notes(self, data):
        self.connect()
        try:
            self.cursor.execute('''
            UPDATE notes 
            SET title = ?, content = ?, created_at = DATETIME('now', '-3 hours') 
            WHERE id = ? AND username = ?
        ''', (data['title'], data['conteudo'], data['id_note'], data['username']))

            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Nota não encontrada ou não foi alterada!")
            return False
        except sqlite3.Error as e:
            print("Erro ao excluir a sessão:", e)
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()

    def update_lixeira(self, data):
        self.connect()
        try:
            self.cursor.execute("UPDATE lixeira SET id = ?,  title = ?, content = ? , created_at = DATETIME('now', '-3 hours') WHERE username = ?", (data['id_lixeira'], data['title'], data['conteudo'], data['username']))
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



    def update_perfis(self, data):
        self.connect()
        try:
            self.cursor.execute('''
                UPDATE perfil 
                SET id = ?, nome_pessoal = ?, email = ?, location = ?, bio = ?
                WHERE username = ?
            ''', (data['id'], data['nome'], data['email'], data['location'], data['bio'], data['username']))
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

    def update_usuarios(self, data):
        self.connect()
        try:
            # Corrigido para usar as chaves corretas do dicionário
            self.cursor.execute("UPDATE users SET id = ?, password = ? WHERE username = ?", 
                                (data['id'], data['senha'], data['username']))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Nota não encontrada ou não foi alterada!")
            return False
        except sqlite3.Error as e:
            print("Erro ao atualizar o usuário:", e)
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()
    def update_session(self, data):
        self.connect()
        try:
            self.cursor.execute('''
                UPDATE sessions 
                SET session_id = ? WHERE username = ?
            ''', (data['session_id'], data['username']))
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


    def delete_notes(self, data):
            self.connect()
            try:
                self.cursor.execute("DELETE FROM notes WHERE id = ? AND title = ? AND content = ? AND username = ?", (data['id_note'], data['title'], data['conteudo'], data['username']))
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

    def delete_lixeira(self, data):
        self.connect()
        try:
            self.cursor.execute("DELETE FROM lixeira WHERE id = ? AND  title = ? AND content = ? AND username = ?", (data['id_lixeira'], data['title'], data['conteudo'], data['username']))
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



    def delete_perfis(self, data):
        self.connect()
        try:
            self.cursor.execute('''
            DELETE FROM perfil WHERE username = ?
        ''', (data['username'],))
            self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (data['username'],))
            self.cursor.execute('''
            DELETE FROM notes WHERE username = ?
        ''', (data['username'],))
            self.cursor.execute('''
            DELETE FROM lixeira WHERE username = ?
        ''', (data['username'],))
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

    def delete_usuarios(self, data):
        self.connect()
        try:
            # Corrigido para usar as chaves corretas do dicionário
            self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (data['username'],))
            self.cursor.execute('''
            DELETE FROM perfil WHERE username = ?
        ''', (data['username'],))
            self.cursor.execute('''
            DELETE FROM notes WHERE username = ?
        ''', (data['username'],))
            self.cursor.execute('''
            DELETE FROM lixeira WHERE username = ?
        ''', (data['username'],))

            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Nota não encontrada ou não foi alterada!")
            return False
        except sqlite3.Error as e:
            print("Erro ao atualizar o usuário:", e)
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()
            
    def delete_session(self, data):
        self.connect()
        try:
            self.cursor.execute('''
                DELETE FROM sessions WHERE session_id = ? AND username = ?
            ''', (data['session_id'], data['username']))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Sessão não encontrada ou não foi alterada!")
            return False
        except sqlite3.Error as e:
            print("Erro ao excluir a sessão:", e)
            self.conn.rollback()  # Reverte a transação em caso de erro
            return False
        finally:
            self.close()
