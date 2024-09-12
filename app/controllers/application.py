from bottle import template, request
import uuid
from database import DatabaseManager

class Application:
    def __init__(self):
        self.pages = {
            'pagina': self.pagina,
            'login': self.login,
            'cadastro': self.cadastro,
            'oficina': self.oficina,
            'perfil': self.perfil,
            'admin':self.admin,
        }
        self._model = DatabaseManager()

    def render(self, page, **kwargs):
        content = self.pages.get(page)
        return content(**kwargs)

    def create_session(self, username, password):
        session_id = str(uuid.uuid4())
        self._model.add_session(session_id, username)
        return session_id

    def get_session_id(self):
        return request.get_cookie('session_id')

    def is_authenticated(self, username):
        session_id = self.get_session_id()
        current_username = self._model.get_user_by_session(session_id)
        return username == current_username

    def is_valid_session(self, session_id):
        return self._model.is_valid_session(session_id)

    def logout_user(self):
        session_id = self.get_session_id()
        if session_id:
            self._model.logout(session_id)

    def login(self, error=None, success=None):
        return template('app/views/html/login', error=error, success=success)
    
    def cadastro(self, error=None):
        return template('app/views/html/cadastro', error=error)

    def pagina(self, username=None, current_user=None, message=None):
        return template('app/views/html/pagina', username=username, current_user=current_user, message=message)

    # def oficina(self, username, message=None, title=None, content=None , created_at=None ):
    def oficina(self, username, message=None, notes=None, lixos=None):
        session_id = self.get_session_id()
        user = self._model.get_user_by_session(session_id)
        return template('app/views/html/oficina', current_user=user, message=message, notes=notes, lixos=lixos)
        # return template('app/views/html/oficina', current_user=user, message=message, title=title, content=content, created_at=created_at)
        
    def perfil(self, username, message=None, nome_pessoal=None, email=None, location=None, bio=None):
        session_id = self.get_session_id()
        user = self._model.get_user_by_session(session_id)
        return template('app/views/html/perfil', current_user=user, message=message, nome_pessoal=nome_pessoal, email=email, location=location, bio=bio)

    def admin(self, username=None, message=None, users=None, sessoes=None, lixos=None, notes=None, perfis=None):
        return template('app/views/html/admin', username=username, message=message, users=users, sessoes=sessoes, lixos=lixos, perfis=perfis, notes=notes)
    