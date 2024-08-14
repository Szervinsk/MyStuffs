from app.controllers.datarecord import DataRecord
from bottle import template, request

class Application():

    def __init__(self):
        self.pages = {
            'pagina': self.pagina,
            'login': self.login,
            'cadastro':self.cadastro,
            'oficina':self.oficina,
        }
        self.__model = DataRecord()
        self.current_username = None

    def render(self, page, **kwargs):
        content = self.pages.get(page, self.helper)
        return content(**kwargs)

    def get_session_id(self):
        return request.get_cookie('session_id')

    def helper(self):
        return template('app/views/html/helper')

    def login(self, error=None , sucess=None):
        return template('app/views/html/login', error=error , sucess=sucess)

    def cadastro(self, error=None):
        return template('app/views/html/cadastro', error=error)

    def pagina(self, username=None):
        if username and self.is_authenticated(username):
            session_id = self.get_session_id()
            current_user = self.__model.getCurrentUser(session_id)
            return template('app/views/html/pagina', current_user=current_user)
        else:
            return template('app/views/html/pagina', current_user=None)

    def verify(self,username,password):
        if self.__model.compareUsers(username):
            print('tem um usuario já existente com os dados fornecidos')
            return True
        else:
            print('nn tem nenhum usuario ainda')
            self.__model.book(username,password)
            return False

    def is_authenticated(self, username): #vai pegar o cara atual e ver se ele tá logado atravez do cookie
        session_id = self.get_session_id() #pegar o cookie
        current_username = self.__model.getUserName(session_id) #pegar o usuario e comparar com o atual
        return username == current_username

    def authenticate_user(self, username, password):
        session_id = self.__model.checkUser(username, password)
        if session_id:
            # self.logout_user()
            self.current_username = self.__model.getUserName(session_id)
            return session_id, username
        return None, None

    def logout_user(self):
        self.current_username = None
        session_id = self.get_session_id()
        if session_id:
            self.__model.logout(session_id)

    def oficina(self, username):
        if self.is_authenticated(username):
            session_id = self.get_session_id()
            user = self.__model.getCurrentUser(session_id)
            return template('app/views/html/perfil', current_user=user)
        else:
            print('Usuário não autenticado, redirecionando para login.')
            return self.render('login', error='Você precisa estar logado para acessar a página de perfil')

