from app.controllers.application import Application
from bottle import Bottle, request, redirect, static_file, response, run

app = Bottle()
clt = Application()

#-----------------------------------------------------------------------------#
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper():
    return clt.render('helper')

#-----------------------------------------------------------------------------#
# Suas rotas aqui:

@app.route('/', method='GET')
@app.route('/<username>', method='GET')
def action_pagina(username=None):
    session_id = clt.get_session_id()  # Obtém o session_id do cookie
    message = request.get_cookie('message')

    current_user = None
    if session_id and clt.is_valid_session(session_id):
        current_user = clt._model.getCurrentUser(session_id)
        
        # Se username não for fornecido, usa o username do usuário atual
        if not username:
            username = current_user.username

        # Se o username fornecido não corresponder ao usuário atual ou não estiver autenticado
        if username and (not current_user or username != current_user.username):
            error = 'Você deve estar logado para acessar esta página'
            return clt.render('login', error=error)

    # Renderiza a página com base na presença de username e current_user
    return clt.render('pagina', username=username, current_user=current_user, message=message)

@app.route('/login', method='GET')
def login():
    return clt.render('login', error=None, success=None)

@app.route('/login', method=['POST'])
def action_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(f"Tentativa de login com Username: {username}, Password: {password}")

    session_id, username = clt.authenticate_user(username, password)

    print(f'sessionId = {session_id}')

    if session_id:
        response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600000)
        
        response.set_cookie('message', 'Login realizado com sucesso!', max_age=5)
        redirect(f'/{username}')
    else:
        print("ERRO" * 5)
        error = 'Falha ao realizar o login, por favor tente novamente'
        return clt.render('login', error=error)

@app.route('/cadastro', method="GET")
def cadastro():
    return clt.render('cadastro', error=None)

@app.route('/cadastro', method=['POST'])
def action_cadastro():
    username = request.forms.get('username')
    password = request.forms.get('password')
    
    cadastro = clt.verify(username, password)

    if cadastro == 1:
        success = 'Cadastro realizado com sucesso!'
        return clt.render('login', success=success)
    elif cadastro == 2: 
        error = 'Já existe uma conta com as informações cadastradas'
        return clt.render('cadastro', error=error)
    elif cadastro == 3:
        error = 'Você precisa preencher todos os campos'
        return clt.render('cadastro', error=error)

@app.route('/logout', method='POST')
def logout():
    clt.logout_user()
    response.delete_cookie('session_id')
    response.set_cookie('message', 'Logout realizado com sucesso!', max_age=5)
    redirect('/')

@app.route('/oficina', method=['POST'])
@app.route('/oficina/<username>', method=['GET'])
def action_perfil(username=None):
    if verification(username):
        return clt.render('oficina', username=username) # renderiza a página de perfil

@app.route('/perfil/<username>', method='GET')
def perfil(username=None):
    if verification(username):
        return clt.render('perfil', username=username)

def verification(username):
    session_id = clt.get_session_id()  # Obtém o session_id do cookie    
    current_user = None
    if session_id and clt.is_valid_session(session_id):
        current_user = clt._model.getCurrentUser(session_id)
        return current_user
    
    if not current_user or (username and username != current_user.username):
        error = 'Você deve estar logado para acessar essa página'
        return clt.render('login', error=error)
    

#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)  # Use debug=True para desenvolvimento
