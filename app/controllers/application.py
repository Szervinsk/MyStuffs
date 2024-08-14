from app.controllers.datarecord import DataRecord
from bottle import template, request
import time

class Application:

    def __init__(self):
        self.pages = {
            'pagina': self.pagina,
            'login': self.login,
            'cadastro': self.cadastro,
            'oficina': self.oficina,
        }
        self._model = DataRecord()
        self.current_username = None

    def helper(self):
        return template('app/views/html/helper')

    def render(self, page, **kwargs):
        content = self.pages.get(page, self.helper)
        return content(**kwargs)

# def do sistema de autenticação e cookies

    # pegar cookie
    def get_session_id(self):
        return request.get_cookie('session_id')

    # autenticaçao e controle de sessão
    def is_authenticated(self, username):
        session_id = self.get_session_id()
        current_username = self._model.getUserName(session_id)
        return username == current_username

    # autentica o ususario e retorna um session_id
    def authenticate_user(self, username, password):
        session_id = self._model.checkUser(username, password)
        if session_id:
            self.current_username = self._model.getUserName(session_id)
            return session_id, username
        return None, None

    # verifica se a sessão é valida
    def is_valid_session(self, session_id):
        return session_id in self._model._authenticated_users  # Mudança para um underscore

    # faz o logout do usuário
    def logout_user(self):
        self.current_username = None
        session_id = self.get_session_id()
        if session_id:
            self._model.logout(session_id)

# def das páginas de login e cadastro
    def login(self, error=None, sucess=None):
        return template('app/views/html/login', error=error, sucess=sucess)

    def cadastro(self, error=None):
        return template('app/views/html/cadastro', error=error)

# def das páginas 
    def pagina(self, username=None, current_user=None, login_message=None):
        if username and self.is_authenticated(username):
            session_id = self.get_session_id()
            current_user = self._model.getCurrentUser(session_id)
            return template('app/views/html/pagina', username=username, current_user=current_user, login_message=login_message)
        else: 
            return template('app/views/html/pagina', username=None, current_user=current_user, login_message=login_message)

    def oficina(self, username):
        if self.is_authenticated(username):
            session_id = self.get_session_id()
            user = self._model.getCurrentUser(session_id)
            return template('app/views/html/perfil', current_user=user)
        else:
            print('usuario nao autenticado, redirecionando para login')
            error = 'Você precisa estar logado para acessar a página de oficina.'
            return self.render('login', error=error)