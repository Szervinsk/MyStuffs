<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oficina</title>
    <link rel="stylesheet" href="../../static/css/perfil.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css" integrity="sha384-rbsA6ez33eEJ6RCXnYj0QO3/TfM/6b1B2hbJwD4nXzochzU1EyHXkSfj/z4cPzxL" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.10.3/font/bootstrap-icons.min.css">

</head>
<body>
    
    <div id="div_nav">
        <nav id="navbar">
            <div id="div_logo">
                
                <a href="/{{current_user.username}}">
                    <img id="logo" src="../../static/img/MyStuffs icon.png" alt="Logo">
                    <img id="loguin" src="../../static/img/Package.png" alt="Loguin">
                </a>
            </div>

            <div id="div_itens">
                <ul>
                    <li>
                        <a href="/{{current_user.username}}">
                            <i class="bi bi-house-fill"></i>
                            <h2 class="tags"> Home </h2>
                        </a>
                    </li>
                    <li>
                        <a href="/oficina/{{current_user.username}}">
                            <i class="bi bi-pen-fill"></i>
                            <h2 class="tags"> Oficina </h2>
                        </a>
                    </li>
                    <li>
                        <a href="/oficina/calendario/{{current_user.username}}">
                            <i class="bi bi-calendar-event-fill"></i>
                            <h2 class="tags"> Calendario </h2>
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
            <div id="navbar_perfil">

                <div id="text_content">
                    <h1> Olá </h1>
                    <h1 id="username"> {{current_user.username}} </h1>
                </div>

                <hr>

                <ul>
                    <li onclick="openEdit()"><i class="bi bi-person-fill"></i> Editar perfil</li>
                    <li onclick="openPass()"><i class="bi bi-shield-shaded"></i> Alterar Senha</li>
                    <li><i class="bi bi-tools"></i> Outras ferramentas</li>
                </ul>
            </div>

            <header>

                <div id="profile">
                    <div id="edit_perfil">
                        <div id="div_namepage">
                            <h1 class="namepage"> Editar perfil </h1>
                            <form action="/logout" method="post">
                                <button id="logout" type="submit"> Sair <i class="bi bi-box-arrow-left"></i></button>
                            </form>
                        </div>
        
                        <h2 class="tagPerfil">Avatar</h2>
                        <div id="div_perfil">
                            <article>
                                <div><img src="../../static/img/studying.jpg" alt="user_photo"></div>
        
                                <h2> Faça o upload de uma foto
                                    <br>
                                Aceitamos: jpg, png e jpeg
                                </h2>
                            </article>
            
                        </div>
            
                        <hr>
            
                        <section>
            
                            <div class="alterar_dados">
                                <form action="">
                                    <label for="username"> Deseja alterar seu nome? </label>
                                    <input type="text" name="username" id="username" class="input">
                
                                    <label for="bio"> Bio</label>
                                    <textarea name="bio" rows="7.5em" id="bio" class="input"></textarea>
        
                                    <button id="btn" type="submit"> Salvar alterações </button>
                                </form>
                            </div>
            
                        </section>
                    </div>
                </div>
            
                <div id="password">
                    <section>
                        <div id="edit_password">

                            <div id="div_namepage">
                                <h1 class="namepage"> Alterar senha </h1>
                                <form action="/logout" method="post">
                                <button id="logout" type="submit"> Sair <i class="bi bi-box-arrow-left"></i></button>
                                </form>
                            </div>
        
                            <div class="alterar_dados">
                                <form action="">
                                    <label for="username"> Insira sua senha antiga </label>
                                    <input type="text" name="username" id="username" class="input">
        
                                    <label for="username"> Insira sua senha nova</label>
                                    <input type="text" name="username" id="username" class="input">
        
                                    <label for="username"> Confirme sua senha </label>
                                    <input type="text" name="username" id="username" class="input">
                
        
                                    <button id="btn" type="submit"> Alterar senha </button>
                                </form>
                            </div>
                        </div>
                    </section>
                </div>
            </header>



        </main>

        <!-- Scripts do Bootstrap -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.6/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.min.js"></script>
        <script src="../../static/js/perfil.js"></script>
    </body>
    </html>
    