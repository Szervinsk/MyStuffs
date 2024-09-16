<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oficina</title>
    <link rel="stylesheet" href="../../static/css/admin.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css" integrity="sha384-rbsA6ez33eEJ6RCXnYj0QO3/TfM/6b1B2hbJwD4nXzochzU1EyHXkSfj/z4cPzxL" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.10.3/font/bootstrap-icons.min.css">

</head>
<body>

    <div id="div_nav"></div>

        % if message:
            <div id="msg" class="message">{{message}}</div>
        % end

        <nav id="navbar">
            <div id="div_logo">
                
                <a href="/admin">
                    <img id="logo" src="../../static/img/MyStuffs icon.png" alt="Logo">
                    <img id="loguin" src="../../static/img/Package.png" alt="Loguin">
                </a>
            </div>

            <div id="div_itens">
                <ul>
                    <li>
                        <a href="/admin">
                            <i class="bi bi-house-fill"></i>
                            <h2 class="tags"> Home </h2>
                        </a>
                    </li>
                    <li>
                        <a href="/oficina/{{username}}">
                            <i class="bi bi-pen-fill"></i>
                            <h2 class="tags"> Oficina </h2>
                        </a>
                    </li>
                    <li>
                        <a href="/configuracoes/{{username}}">
                            <i class="bi bi-gear-fill"></i>
                            <h2 class="tags"> Configurações </h2>
                        </a>
                    </li>
                </ul>
            </div>                
        </nav>
    </div>

    <main>
        <div id="content_title">
            <h1> Bem vindo a administração </h1>
        </div>

        <div id="content_tags">
            <h2 class="tags_table , selected" onclick="switchSection('user_table', this)">Usuários</h2>
            <h2 class="tags_table" onclick="switchSection('sessoes_table', this)">Sessões</h2>
            <h2 class="tags_table" onclick="switchSection('perfis_table', this)">Perfis</h2>
            <h2 class="tags_table" onclick="switchSection('notas_table', this)">Notas</h2>
            <h2 class="tags_table" onclick="switchSection('lixeira_table', this)">Lixeiras</h2>
        </div>

        <div id="content_filtro">
            <div class="depe">
                <label for="filtro">Conteúdo</label>
                <input type="text" id="filtro" name="filtro">
            </div>
        </div>

        <div id="line"></div>

        <div id="tables_area">

            <div class="divs_tables" id="user_table" style="display: flex;">
                
                <table>
                    <thead>
                        <tr>
                            <th></th>
                            <th>id</th>
                            <th>Nome</th>
                            <th>Senha</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for user in users:
                        <tr>
                            <th><input class="row-select" type="checkbox" name="" id=""></th>
                            <th><input class="inputs" type="text" value="{{user[0]}}" readonly="true"></th>
                            <th><input class="inputs , username" type="text" value="{{user[1]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{user[2]}}" readonly="true"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

                <div id="edit_row_users">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/edit_adm" method="post">
                        <input name="tabela" type="hidden">
                        <label for="id"> id :</label>
                        <input class="inputs id" name="id" type="text">
                        
                        <label for="username">Nome:</label>
                        <input class="inputs username" name="username" type="text" readonly='true'>
                        
                        <label for="Senha">Senha:</label>
                        <input class="inputs Senha" name="senha" type="text">

                        <button type="submit">Salvar alterações</button>
                    </form>
                </div>

                <div id="delete_row_users">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/delete_adm" method="post">
                        <input name="tabela" type="hidden">
                        <input class="inputs id" name="id" type="hidden">
                        
                        <input class="inputs username" name="username" type="hidden" readonly='true'>
                        
                        <input class="inputs Senha" name="senha" type="hidden">

                        <button>Não</button>
                        <button type="submit">Sim</button>
                    </form>
                </div>

                
            </div>

            <div class="divs_tables" id="sessoes_table">
                
                <table>
                    <thead>
                        <tr>
                            <th></th>
                            <th>Sessão</th>
                            <th>Usuário</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for sessao in sessoes:
                        <tr>
                            <th><input class="row-select" type="checkbox" name="" id=""></th>
                            <th><input class="inputs" name="session_id" type="text" value="{{sessao[0]}}" readonly="true"></th>
                            <th><input class="inputs , username" type="text" value="{{sessao[1]}}" readonly="true"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

                <div id="edit_row_sessions">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/edit_adm" method="post">
                        <input name="tabela" type="hidden">
                        <label for="session_id"> Sessão :</label>
                        <input class="inputs session_id" name="session_id" type="text">
                        
                        <label for="username">Usuário:</label>
                        <input class="inputs username" name="username" type="text" readonly='true'>
                        
                        <button type="submit">Salvar alterações</button>
                    </form>
                </div>

                <div id="delete_row_sessions">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/delete_adm" method="post">
                        <input name="tabela" type="hidden">
                        <input class="inputs session_id" name="session_id" type="hidden">
                        
                        <input class="inputs username" name="username" type="hidden" readonly='true'>
                        
                        <button>Não</button>
                        <button type="submit">Sim</button>
                    </form>
                </div>

            </div>

            <div class="divs_tables" id="perfis_table">
                
                <table>
                    <thead>
                        <tr>
                            <th></th>
                            <th>id</th>
                            <th>Username</th>
                            <th>Nome pessoal</th>
                            <th>Email</th>
                            <th>Localização</th>
                            <th>Descrição</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for perfil in perfis:
                        <tr>
                            <th><input class="row-select" type="checkbox" name="" id="" ></th>
                            <th><input class="inputs" type="text" value="{{perfil[0]}}" readonly="true"></th>
                            <th><input class="inputs , username" type="text" value="{{perfil[1]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{perfil[3]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{perfil[4]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{perfil[5]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{perfil[6]}}" readonly="true"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

                <div id="edit_row_perfil">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/edit_adm" method="post">
                        <input name="tabela" type="hidden">
                        <label for="id"> Id :</label>
                        <input class="inputs id" name="id" type="text">
                        
                        <label for="username">Username:</label>
                        <input class="inputs username" name="username" type="text" readonly='true'>
                        
                        <label for="nome">Nome pessoal:</label>
                        <input class="inputs nome" name="nome" type="text">
                        
                        <label for="Email">Email:</label>
                        <input class="inputs email" name="email" type="text">
                        
                        <label for="location">Localização:</label>
                        <input class="inputs location" name="location" type="text">
                        <!-- <input class="table_tag" type="text"> -->

                        <label for="bio">Descrição:</label>
                        <input class="inputs bio" name="bio" type="text">
                        
                        <button type="submit">Salvar alterações</button>
                    </form>
                </div>

                <div id="delete_row_perfil">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/delete_adm" method="post">
                        <input name="tabela" type="hidden">
                        <input class="inputs id" name="id" type="hidden">
                        
                        <input class="inputs username" name="username" type="hidden" readonly='true'>

                        <input class="inputs nome" name="nome" type="hidden" readonly='true'>
                        
                        <input class="inputs email" name="email" type="hidden" readonly="true">
                        
                        <input class="inputs location" name="location" type="hidden" readonly="true">
                        
                        <input class="inputs bio" name="bio" type="hidden" readonly="true">
                        
                        <h2> Tem certeza?</h2>
                        
                        <button>Não</button>
                        <button type="submit">Sim</button>
                    </form>
                </div>


            </div>
            
            <div class="divs_tables" id="notas_table">
                <table>
                    <thead>
                        <tr>
                            <th></th>
                            <th>id</th>
                            <th>Nome</th>
                            <th>Titulo</th>
                            <th>Conteudo</th>
                            <th>Data</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for note in notes:
                        <tr>
                            <th><input class="row-select" type="checkbox" name="" id="" ></th>
                            <th><input class="inputs" type="text" value="{{note[0]}}" readonly="true"></th>
                            <th><input class="inputs , username" type="text" value="{{note[1]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{note[2]}}" readonly="true"></th>
                            <th><input class="inputs , conteudo" type="text" value="{{note[3]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{note[4]}}" readonly="true"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

                <div id="edit_row_notes">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/edit_adm" method="post">
                        <input name="tabela" type="hidden">

                        <label for="id_note"> Id :</label>
                        <input class="inputs id_note" name="id_note" type="text">
                        
                        <label for="username">Username:</label>
                        <input class="inputs username" name="username" type="text" readonly='true'>
                        
                        <label for="title">Título:</label>
                        <input class="inputs title" name="title" type="text">
                        
                        <label for="conteudo">Conteudo:</label>
                        <input class="inputs conteudo" name="conteudo" type="text">
                        
                        <label for="data">Data:</label>
                        <input class="inputs data" name="data" type="text">
                        <!-- <input class="table_tag" type="text"> -->
                        
                        <button type="submit">Salvar alterações</button>
                    </form>
                </div>

                <div id="delete_row_notes">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/delete_adm" method="post">
                        <input name="tabela" type="hidden">

                        <input class="inputs id_note" name="id_note" type="hidden">
                        
                        <input class="inputs username" name="username" type="hidden" readonly='true'>
                        
                        <input class="inputs title" name="title" type="hidden">
                        
                        <input class="inputs conteudo" name="conteudo" type="hidden">
                        
                        <input class="inputs data" name="data" type="hidden">
                        <!-- <input class="table_tag" type="text"> -->

                        <button>Não</button>
                        <button type="submit">Sim</button>
                    </form>
                </div>

            </div>

            <div class="divs_tables" id="lixeira_table">
                <table>
                    <thead>
                        <tr>
                            <th></th>
                            <th>id</th>
                            <th>Nome</th>
                            <th>Titulo</th>
                            <th>Conteudo</th>
                            <th>Data</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for lixo in lixos:
                        <tr>
                            <th><input class="row-select" type="checkbox" name="" id="" ></th>
                            <th><input class="inputs" type="text" value="{{lixo[0]}}" readonly="true"></th>
                            <th><input class="inputs , username" type="text" value="{{lixo[1]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{lixo[2]}}" readonly="true"></th>
                            <th><input class="inputs , conteudo" type="text" value="{{lixo[3]}}" readonly="true"></th>
                            <th><input class="inputs" type="text" value="{{lixo[4]}}" readonly="true"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

                <div id="edit_row_lixeira">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/edit_adm" method="post">
                        <input name="tabela" type="hidden">
                        <label for="id_lixeira"> Id :</label>
                        <input class="inputs id_lixeira" name="id_lixeira" type="text">
                        
                        <label for="username">Username:</label>
                        <input class="inputs username" name="username" type="text" readonly='true'>
                        
                        <label for="title">Título:</label>
                        <input class="inputs title" name="title" type="text">
                        
                        <label for="conteudo">Conteudo:</label>
                        <input class="inputs conteudo" name="conteudo" type="text">
                        
                        <label for="data">Data:</label>
                        <input class="inputs data" name="data" type="text">
                        <!-- <input class="table_tag" type="text"> -->
                        
                        <button type="submit">Salvar alterações</button>
                    </form>
                </div>

                <div id="delete_row_lixeira">
                    <div>
                        <button class="fechar"> X </button>
                    </div>

                    <form class="form" action="/delete_adm" method="post">
                        <input name="tabela" type="hidden">
                        <input class="inputs id_lixeira" name="id_lixeira" type="hidden">
                        
                        <input class="inputs username" name="username" type="hidden" readonly='true'>
                        
                        <input class="inputs title" name="title" type="hidden">
                        
                        <input class="inputs conteudo" name="conteudo" type="hidden">
                        
                        <input class="inputs data" name="data" type="hidden">
                        
                        <h2> Tem certeza?</h2>
                        
                        <button>Não</button>
                        <button type="submit">Sim</button>
                    </form>
                </div>


            </div>

            <div id="div_text">
                <h2 id="selec_table"> TABELA SELECIONADA </h2>
                <button id="alterar"> Editar </button>
                <button id="deletar"> Deletar </button>
            </div>

        </div>




    </main>






</body>
<script src="../../static/js/admin.js"></script>
</html>
    