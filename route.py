from app.controllers.application import Application
from bottle import Bottle, request, redirect, static_file, response, run
from database import DatabaseManager

app = Bottle()
clt = Application()
db = DatabaseManager()

# Inicializa as tabelas do banco de dados
db.create_tables()

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/', method='GET')
@app.route('/<username>', method='GET')
def action_pagina(username=None):
    session_id = clt.get_session_id()
    message = request.get_cookie('message')

    current_user = None
    if session_id and clt.is_valid_session(session_id):
        current_user = db.get_user_by_session(session_id)
        print(f'acessando página de {current_user}')
        if not username:
            username = current_user

        if username and (not current_user or username != current_user):
            error = 'Você deve estar logado para acessar esta página'
            return clt.render('login', error=error)

    return clt.render('pagina', username=username, current_user=current_user, message=message)

@app.route('/login', method='GET')
def login():
    return clt.render('login', error=None, success=None)

@app.route('/login', method=['POST'])
def action_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    user = db.get_user(username)
    if user and user[2] == password:  # user[2] é a senha no banco de dados
        session_id = clt.create_session(username, password)
        response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600000)
        response.set_cookie('message', 'Login realizado com sucesso!', max_age=5)
        redirect(f'/{username}')
    else:
        error = 'Falha ao realizar o login, por favor tente novamente'
        return clt.render('login', error=error)

@app.route('/cadastro', method="GET")
def cadastro():
    return clt.render('cadastro', error=None)

@app.route('/cadastro', method=['POST'])
def action_cadastro():
    username = request.forms.get('username')
    password = request.forms.get('password')
    
    if not username or not password:
        error = 'Você precisa preencher todos os campos'
        return clt.render('cadastro', error=error)
    
    if db.add_user(username, password):
        success = 'Cadastro realizado com sucesso!'
        return clt.render('login', success=success)
    else:
        error = 'Já existe uma conta com as informações cadastradas'
        return clt.render('cadastro', error=error)

@app.route('/alterarSenha', method='POST')
def alterarSenha():
    session_id = clt.get_session_id()
    username = clt._model.get_user_by_session(session_id)
    
    password = request.forms.get('newpassword')
    db.update_password(username, password)

    response.set_cookie('message', 'Sua senha foi alterada com sucesso!', max_age=5)
    redirect(f'/perfil/{username}')

@app.route('/logout', method='POST')
def logout():
    clt.logout_user()
    response.delete_cookie('session_id')
    response.set_cookie('message', 'Logout realizado com sucesso!', max_age=5)
    redirect('/')

@app.route('/oficina/<username>', method=['GET'])
def action_oficina(username=None):
    if clt.is_authenticated(username):
        return clt.render('oficina', username=username)
    else:
        return clt.render('login', error='Você deve estar logado para acessar esta página.')

@app.route('/perfil/<username>', method='GET')
def perfil(username=None):
    message = request.get_cookie('message')

    if clt.is_authenticated(username):
        return clt.render('perfil', username=username, message=message)
    else:
        return clt.render('login', error='Você deve estar logado para acessar esta página.')

#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
