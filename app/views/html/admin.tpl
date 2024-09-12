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
                        <a href="/configuracoes">
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
                            <th><input type="checkbox" name="" id=""></th>
                            <th>id</th>
                            <th>Nome</th>
                            <th>Senha</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for user in users:
                        <tr>
                            <th><input type="checkbox" name="" id=""></th>
                            <th><input class="inputs" type="text" value="{{user[0]}}"></th>
                            <th><input class="inputs" type="text" value="{{user[1]}}"></th>
                            <th><input class="inputs" type="text" value="{{user[2]}}"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

            </div>

            <div class="divs_tables" id="sessoes_table">
                
                <table>
                    <thead>
                        <tr>
                            <th><input type="checkbox" name="" id=""></th>
                            <th>Sessão</th>
                            <th>Usuário</th>
                        </tr>
                    </thead>
                    <tbody>
                        % for sessao in sessoes:
                        <tr>
                            <th><input type="checkbox" name="" id=""></th>
                            <th><input class="inputs" type="text" value="{{sessao[0]}}"></th>
                            <th><input class="inputs" type="text" value="{{sessao[1]}}"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

            </div>

            <div class="divs_tables" id="perfis_table">
                
                <table>
                    <thead>
                        <tr>
                            <th><input type="checkbox" name="" id=""></th>
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
                            <th><input type="checkbox" name="" id=""></th>
                            <th><input class="inputs" type="text" value="{{perfil[0]}}"></th>
                            <th><input class="inputs" type="text" value="{{perfil[1]}}"></th>
                            <th><input class="inputs" type="text" value="{{perfil[3]}}"></th>
                            <th><input class="inputs" type="text" value="{{perfil[4]}}"></th>
                            <th><input class="inputs" type="text" value="{{perfil[5]}}"></th>
                            <th><input class="inputs" type="text" value="{{perfil[6]}}"></th>
                        </tr>
                        % end
                    </tbody>
                </table>

            </div>
            
            <div class="divs_tables" id="notas_table">
                <table>
                    <thead>
                        <tr>
                            <th><input type="checkbox" name="" id=""></th>
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
                            <th><input type="checkbox" name="" id=""></th>
                            <th><input class="inputs" type="text" value="{{note[0]}}"></th>
                            <th><input class="inputs" type="text" value="{{note[1]}}"></th>
                            <th><input class="inputs" type="text" value="{{note[2]}}"></th>
                            <th><input class="inputs , conteudo" type="text" value="{{note[3]}}"></th>
                            <th><input class="inputs" type="text" value="{{note[4]}}"></th>
                        </tr>
                        % end
                    </tbody>
                </table>
            </div>

            <div class="divs_tables" id="lixeira_table">
                <table>
                    <thead>
                        <tr>
                            <th><input type="checkbox" name="" id=""></th>
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
                            <th><input type="checkbox" name="" id="tr"></th>
                            <th><input class="inputs" type="text" value="{{lixo[0]}}"></th>
                            <th><input class="inputs" type="text" value="{{lixo[1]}}"></th>
                            <th><input class="inputs" type="text" value="{{lixo[2]}}"></th>
                            <th><input class="inputs , conteudo" type="text" value="{{lixo[3]}}"></th>
                            <th><input class="inputs" type="text" value="{{lixo[4]}}"></th>
                        </tr>
                        % end
                    </tbody>
                </table>
            </div>


        </div>




    </main>






</body>
<script src="../../static/js/admin.js"></script>
</html>
    