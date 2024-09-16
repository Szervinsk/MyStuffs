from app.controllers.application import Application
from bottle import Bottle, request, redirect, static_file, response, run
from database import DatabaseManager
from admin import Administration

app = Bottle()
clt = Application()
db = DatabaseManager()
adm = Administration()

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

        if user[1] == 'admin':
            response.set_cookie('message', 'Logado como administrador!', max_age=2)
            redirect(f'/administracao')
        else:    
            response.set_cookie('message', 'Login realizado com sucesso!', max_age=2)
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

    response.set_cookie('message', 'Sua senha foi alterada com sucesso!', max_age=2)
    redirect(f'/perfil/{username}')

@app.route('/logout', method='POST')
def logout():
    clt.logout_user()
    response.delete_cookie('session_id')
    response.set_cookie('message', 'Logout realizado com sucesso!', max_age=2)
    redirect('/')

@app.route('/oficina/<username>', method=['GET'])
def action_oficina(username=None):
    message = request.get_cookie('message')
    response.delete_cookie('message')

    sessionId = clt.get_session_id()
    username = db.get_user_by_session(sessionId)

    if clt.is_authenticated(username):
        notes = db.get_notes(username)
        lixos = db.get_lixeira(username)

        return clt.render('oficina', 
                username=username, 
                message=message, 
                notes=notes,
                lixos=lixos
            )

    else:
        return clt.render('login', error='Você deve estar logado para acessar esta página.')
    
@app.route('/add_notes', method=['POST'])
def add_notes():
    session_id = clt.get_session_id()
    username = db.get_user_by_session(session_id)

    if request.method == 'POST':
        title = request.forms.get('title')
        content = request.forms.get('content')
        print(title,content)
        if db.add_note(username,title,content):
            response.set_cookie('message','Nota adicionada com sucesso!', max_age=2)
        else: 
            response.set_cookie('message','Error 404')
        redirect(f'/oficina/{username}')

@app.route('/edit_notes', method=['POST'])
def edit_note():
    sessionId = clt.get_session_id()
    username = db.get_user_by_session(sessionId)

    id = request.forms.get('noteId')
    title = request.forms.get('title_ed')
    content = request.forms.get('content_ed')

    if db.edit_notes(username, id, title, content):
        response.set_cookie('message','Informações atualizadas!', max_age=2)
    else: 
        response.set_cookie('message','Error 404')
    redirect(f'/oficina/{username}')

@app.route('/delete_note', method=['POST'])
def delete_note():
    sessionId = clt.get_session_id()
    username = db.get_user_by_session(sessionId)
    
    id = request.forms.get('noteId')
    if db.delete_notes(id,username):
        response.set_cookie('message','Nota deletada com sucesso!', max_age=2)
    else: 
        response.set_cookie('message','Error 404')
    redirect(f'/oficina/{username}')

@app.route('/restaurar_note', method=['POST'])
def restaurar_note():
    sessionId = clt.get_session_id()
    username = db.get_user_by_session(sessionId)
        
    id = request.forms.get('noteId')
    if db.restaura_note(id,username):
        response.set_cookie('message','Nota resgatada com sucesso!', max_age=2)
    else: 
        response.set_cookie('message','Error 404')
    redirect(f'/oficina/{username}')

@app.route('/send2Trash', method='POST')
def send_lixeira():
    sessionId = clt.get_session_id()
    username = db.get_user_by_session(sessionId)
    
    id = request.forms.get('noteId')
    if db.lixeira(id,username):
        response.set_cookie('message','Nota enviada para lixeira', max_age=2)
    else: 
        response.set_cookie('message','Error 404')
    redirect(f'/oficina/{username}')

@app.route('/configuracoes/<username>', method='GET')
def perfil(username=None):
    message = request.get_cookie('message')
    response.delete_cookie('message')  # Remove o cookie após usá-lo

    if clt.is_authenticated(username):
        perfil = db.get_perfil(username)
        if perfil:
            return clt.render('perfil', 
                username=username, 
                message=message, 
                nome_pessoal=perfil[0], 
                email=perfil[1], 
                location=perfil[2], 
                bio=perfil[3]
            )
        else:
            return 'Erro ao carregar o perfil'
    else:
        return clt.render('login', error='Você deve estar logado para acessar esta página.')


@app.route('/editperfil', method=["GET", "POST"])
def editar_perfil():
    sessionId = clt.get_session_id()
    username = db.get_user_by_session(sessionId)

    if request.method == "POST":
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        location = request.forms.get('location')
        bio = request.forms.get('bio')

        if db.update_perfil(username, nome, email, location, bio):
            response.set_cookie('message', 'Perfil atualizado com sucesso!', max_age=2)
            redirect(f'/perfil/{username}')
        else:
            return "Erro ao atualizar o perfil."

    else:
        perfil = db.get_perfil(username)
        if perfil:
            return clt.render('perfil', 
                message=None,
                username=username, 
                nome_pessoal=perfil[0], 
                email=perfil[1], 
                location=perfil[2], 
                bio=perfil[3]
            )
        else:
            return 'Erro ao carregar o perfil'

@app.route('/deleteUser', method='POST')
def delete_account():
    session_id = clt.get_session_id()
    username = db.get_user_by_session(session_id)

    if username:
        db.delete_user(username,session_id) 
        response.delete_cookie('session_id')
        response.set_cookie('message', 'Obrigado por escolher a MyStuffs, sentiremos saudades!', max_age=2)
        redirect('/')
    else:
        return "Usuário não encontrado ou sessão inválida."

@app.route('/toggle-favorite', method='POST')
def star():
    session_id = clt.get_session_id()
    username = db.get_user_by_session(session_id)

    id = request.forms.get('id')
    is_favorite = request.forms.get('toggle')

    # Define o novo status de favorito com base no valor do botão
    new_favorite_status = 1 if is_favorite == 'favorite' else 0

    print(f'ID: {id}, Favorito: {new_favorite_status}')
    if db.starSet(id, new_favorite_status):
        return redirect(f'/oficina/{username}')  # Redireciona após atualizar
    else: 
        return "Erro ao favoritar!", 400  # Retorna erro se falhar
    
@app.route('/administracao', method='GET')
def admin():
    response.delete_cookie('message')

    session_id = clt.get_session_id()
    username = db.get_user_by_session(session_id)
    
    if username == 'admin':

        message = request.get_cookie('message')
        response.delete_cookie('message') 

        users,sessoes, perfis, notes, lixos = adm.getTables()

        return clt.render('admin', username=username, message=message , users=users, sessoes=sessoes, perfis=perfis, notes=notes, lixos=lixos)
    else:
        return clt.render('login', error='Você não tem acesso a essa página')

@app.route('/edit_adm', method='POST')
def edit_from_adm():
    table = request.forms.get('tabela')

    # Captura todos os dados possíveis, mas não assume que todos estarão presentes
    data = {
        'id': request.forms.get('id'),
        'id_note': request.forms.get('id_note'),
        'id_lixeira': request.forms.get('id_lixeira'),
        'session_id': request.forms.get('session_id'),

        'username': request.forms.get('username'),
        'senha': request.forms.get('senha'),

        'title': request.forms.get('title'),
        'conteudo': request.forms.get('conteudo'),
        'data': request.forms.get('data'),

        'nome': request.forms.get('nome'),
        'email': request.forms.get('email'),
        'location': request.forms.get('location'),
        'bio': request.forms.get('bio'),
    }

    # Remove os campos que estão vazios ou não foram enviados
    data = {key: value for key, value in data.items() 
            if value is not None and value != ''}
    
    print(data)

    if table == 'users':
        if adm.update_usuarios(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de usuários atualizados com sucesso!', max_age=2)
    elif table == 'sessions':
        if adm.update_session(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de sessões atualizados com sucesso!', max_age=2)
    elif table == 'perfil':
        if adm.update_perfis(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de perfil atualizados com sucesso!', max_age=2)
    elif table == 'notes':
        if adm.update_notes(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de notas atualizados com sucesso!', max_age=2)
    elif table == 'lixeira':
        if adm.update_lixeira(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de lixeira atualizados com sucesso!', max_age=2)
    else:
        return "Tabela não encontrada."
    
@app.route('/delete_adm', method='POST')
def delete_from_adm():
    table = request.forms.get('tabela')

    # Captura todos os dados possíveis, mas não assume que todos estarão presentes
    data = {
        'id': request.forms.get('id'),
        'id_note': request.forms.get('id_note'),
        'id_lixeira': request.forms.get('id_lixeira'),
        'session_id': request.forms.get('session_id'),

        'username': request.forms.get('username'),
        'senha': request.forms.get('senha'),

        'title': request.forms.get('title'),
        'conteudo': request.forms.get('conteudo'),
        'data': request.forms.get('data'),

        'nome': request.forms.get('nome'),
        'email': request.forms.get('email'),
        'location': request.forms.get('location'),
        'bio': request.forms.get('bio'),
    }

    # Remove os campos que estão vazios ou não foram enviados
    data = {key: value for key, value in data.items() 
            if value is not None and value != ''}
    
    print(data)

    if table == 'users':
        if adm.delete_usuarios(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de usuários deletados com sucesso!', max_age=2)
    elif table == 'sessions':
        if adm.delete_session(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de sessões deletados com sucesso!', max_age=2)
    elif table == 'perfil':
        if adm.delete_perfis(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de perfil deletados com sucesso!', max_age=2)
    elif table == 'notes':
        if adm.delete_notes(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de notas deletados com sucesso!', max_age=2)
    elif table == 'lixeira':
        if adm.delete_lixeira(data):
            redirect('/administracao')
            response.set_cookie('message', 'dados de lixeira deletados com sucesso!', max_age=2)
    else:
        return "Tabela não encontrada."


#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=False)
