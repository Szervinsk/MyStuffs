<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oficina</title>
    <link rel="stylesheet" href="../../static/css/oficina.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css" integrity="sha384-rbsA6ez33eEJ6RCXnYj0QO3/TfM/6b1B2hbJwD4nXzochzU1EyHXkSfj/z4cPzxL" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.10.3/font/bootstrap-icons.min.css">

</head>
<body>
    
    % if message:
            <div id="msg" class="message">{{message}}</div>
        % end

    <div id="div_nav">
        <nav id="navbar">
            <div id="div_logo">
                
                <a href="/{{current_user}}">
                    <img id="logo" src="../../static/img/MyStuffs icon.png" alt="Logo">
                    <img id="loguin" src="../../static/img/Package.png" alt="Loguin">
                </a>
            </div>

            <div id="div_itens">
                <ul>
                    <li>
                        <a href="/{{current_user}}">
                            <i class="bi bi-house-fill"></i>
                            <h2 class="tags"> Home </h2>
                        </a>
                    </li>
                    <li>
                        <a href="/oficina/{{current_user}}">
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

            <a href="/perfil/{{current_user}}">
                <div id="div_perfil">
                    
                    <div><img src="../../static/img/userphoto.png" alt=""></div>
                    <h1 class="tags" id="username"> {{current_user}} </h1>
                    
                    <form action="/logout" method="post">
                        <button id="logout" type="submit"><i class="bi bi-box-arrow-left"></i></button>
                    </form>
                </div>
            </a>
                
        </nav>
    </div>

        <section>
            <div>
                <div id="searchbar_div">
                    <input name="searchbar" class="input" id="searchbar" type="text" placeholder="Pesquisar notas ">
                    <button class="input_btn"><i class="bi bi-search"></i></button>
                </div>
                
                <div class="deladin" id="add_notas">
                    <h2> Minhas notas</h2>
                    <button class="buttons" onclick="switchSection('add_notes')"> Add + </button>
                </div>
                
                <div>
                    <ul id="pastas">
                            <li class="pastas_li" id="geral"><i id="icon" class="bi bi-folder2"></i></i> Geral</li>
                            <div id="div_pasta" class="depe">
                                <div>
                                    <ul>
                                    % for note in notes:
                                        <li class="lis_pastas" onclick="switchSection('edit_notes', '{{note[0]}}', '{{note[1]}}', '{{note[2]}}', '{{note[3]}}')"><i style="font-size: 10px;" class="bi bi-arrow-return-right"></i>  {{note[0]}}</li> 
                                    % end
                                    </ul>
                                </div>
                            </div>

                            <li class="pastas_li" id="favoritos"><i id="icon" class="bi bi-star"></i></i> Favoritos</li>
                            <div id="div_favoritos" class="depe">
                                <div>
                                    <ul>
                                        % for note in notes:
                                            % if note[4] == 1:
                                            <li class="lis_pastas" onclick="switchSection('edit_notes', '{{note[0]}}', '{{note[1]}}', '{{note[2]}}', '{{note[3]}}')">
                                                <i style="font-size: 10px;" class="bi bi-arrow-return-right"></i>  
                                                {{note[0]}}
                                            </li> 
                                            % end
                                        % end
                                    </ul>
                                </div>
                            </div>

                            <li class="pastas_li" id="lixeira"><i class="bi bi-trash3"></i></i> Lixeira</li>
                            <div id="div_lixeira" class="depe">
                                <div>
                                    <ul>
                                    % for lixo in lixos:
                                        <li class="lis_pastas" onclick="switchSection('delete_notes', '{{lixo[0]}}', '{{lixo[1]}}', '{{lixo[2]}}', '{{lixo[3]}}')"><i style="font-size: 10px;" class="bi bi-arrow-return-right"></i>  {{lixo[0]}}</li> 
                                    % end
                                    </ul>
                                </div>
                            </div>
                    </ul>
                    
                </div>

                <hr>

                <div id="bloquin">
                    % for note in notes:
                    <div class="bloquin" onclick="switchSection('edit_notes', '{{note[0]}}', '{{note[1]}}', '{{note[2]}}', '{{note[3]}}')">

                            <h3 class="title">{{note[0]}}</h3>  <!-- title -->
                            <hr>
                            <p>{{!note[1]}}</p>   <!-- content -->
                            gayyyy
                            <div class="deladin">
                                % if note[4] == 1:
                                    <h6><i style="font-size: 1.5em; color:gold" onclick="favorite(this, '{{note[3]}}')" class="bi bi-star-fill"></i></h6>
                                % else:
                                    <h6><i style="font-size: 1.5em; color:grey;" onclick="favorite(this, '{{note[3]}}')" class="bi bi-star-fill"></i></h6>
                                % end
                                <h6>{{note[2]}}</h6>  <!-- created_at -->
                            </div>
                        </div>
                    % end
                </div>
                
            </div>
        </section>
        
        <article>
            <div id="add_notes">
                <form action="/add_notes" method="post">
                    <label for="title"></label>
                    <input class="inputs" id="title" name="title" type="text" placeholder="Título" autocomplete="off">
                    <hr>
                    <textarea class="inputs" name="content" id="content" placeholder="Insira aqui o que você quiser" autocomplete="off"></textarea>
                    <button class="buttons" id="submit_btn" type="submit"> Salvar </button>
                </form>
            </div>

            <div id="no_notes"> 
                <img src="../../static/img/Task list.png" alt="notes">
                <h2>Por favor clique em um dos blocos pfv </h2>
            </div>
            
            <div id="edit_notes" style="display:none;">
                <form id="delete_form" action="/send2Trash" method="post">
                    <input type="hidden" id="noteId_del" name="noteId" value=''>
                    <button id="deletar_btn" type="submit"> Deletar <i class="bi bi-trash"></i></button>
                </form>

                <form id="edit_form" action="/edit_notes" method="post">
                    <input type="hidden" id="noteId_ed" name="noteId" value=''>
                    <label for="title_ed"></label>
                    <input class="inputs" id="title_ed" name="title_ed" type="text" placeholder="Título" autocomplete="off">
                    <hr>
                    <textarea class="inputs" name="content_ed" id="content_ed" placeholder="Insira aqui o que você quiser" autocomplete="off"></textarea>
                    <button id="submit_btn" type="submit"> Alterar </button>
                </form>
            </div>
            
            <div id="delete_notes" style="display:none;">

                <div id="btns_del">
                    <form id="delete_form" action="/delete_note" method="post">
                        <input type="hidden" id="noteId_delp" name="noteId" value=''>
                        <input type="hidden" id="created_atdp" name="created_atdp" value=''>
                        <button id="delete_btn" type="submit"> Deletar  <i class="bi bi-trash"></i></button>
                    </form>

                    <form id="restaurar_form" action="/restaurar_note" method="post">
                        <input type="hidden" id="noteId_res" name="noteId" value=''>
                        <button id="restart_btn" type="submit"> Restaurar  <i class="bi bi-back"></i></button>
                    </form>
                </div>
            
                    <input type="hidden" id="noteId_ed" name="noteId" value=''>
                    <label for="title_del"></label>
                    <input class="inputs" id="title_del" name="title_del" type="text" readonly="true" placeholder="Título" autocomplete="off">
                    <hr>
                    <textarea class="inputs" name="content_del" id="content_del" readonly="true" placeholder="Insira aqui o que você quiser" autocomplete="off"></textarea>
            </div>
            
        </article>
        
        <!-- Scripts do Bootstrap -->
    <script src="../../static/js/oficina.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.6/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.min.js"></script>
</body>
</html>
