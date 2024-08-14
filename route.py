from app.controllers.application import Application
from bottle import Bottle, request, redirect, static_file, response, run

app = Bottle()
clt = Application()

#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper():
    return clt.render('helper')

#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/', method='GET')
@app.route('/<username>', method='GET')
def action_pagina(username=None):
    print(username)
    if clt.is_authenticated(username):
        return clt.render('pagina', username=username)
    else:
        error = 'Você deve estar logado para acessar a página' 
        return clt.render('login', error=error)

@app.route('/login', method='GET')
def login():
    return clt.render('login', error=None , sucess=None)

@app.route('/login', method=['POST'])
def action_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(f"Tentativa de login com Username: {username}, Password: {password}")

    session_id, username = clt.authenticate_user(username, password)

    print(f'sessionId = {session_id}')

    if session_id:
        response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
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
    
    if not cadastro:
        # cadastro deu bom, vai pedir para a pessoa fazer login
        sucess = 'Cadastro realizado com sucesso!'
        return clt.render('login', sucess=sucess)
    else: 
        error = 'Já existe uma conta com as informações cadastradas'
        return clt.render('cadastro', error=error)

@app.route('/logout', method='POST')
def logout():
    clt.logout_user()
    response.delete_cookie('session_id')
    redirect('/')


@app.route('/oficina/<username>', method=['POST', 'GET'])
def action_perfil(username=None):
    print(f'{username} from act perfil')
    if clt.is_authenticated(username):
        return clt.render('oficina', username=username)
    else:
        error = 'Você deve estar logado para acessar a página' 
        return clt.render('login', error=error)



#----------------------------------------   -------------------------------------

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)  # Use debug=True para desenvolvimento
