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
                        <a href="/oficina/calendario/{{current_user}}">
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

            <a href="/perfil/{{current_user}}">
                <div id="div_perfil">
                    
                    <div><img src="../../static/img/studying.jpg" alt=""></div>
                    <h1 class="tags" id="username"> {{current_user}} </h1>
                    
                    <form action="/logout" method="post">
                        <button id="logout" type="submit"><i class="bi bi-box-arrow-left"></i></button>
                    </form>
                </div>
            </a>
                
        </nav>
    </div>

        <section>
            aqui vao ficar os post
        </section>

        <article>
            sla
        </article>

    <!-- Scripts do Bootstrap -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.6/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.min.js"></script>
    <script src="../../static/js/oficina.js"></script>
</body>
</html>
