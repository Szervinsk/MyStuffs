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
    <main>
        <div id="content_dad2">
            <nav id="nav_v">

                <div id="content_logo">
                    <img id="MyStuffs_logo" src="../../static/img/MyStuffs icon.png" alt="Logo">
                </div>


                <ul class="list" style="list-style: none; padding: 0;">
                    <li><a href="/{{current_user.username}}" class="nav-link"><i class="bi bi-house"></i><h2> Home</h2></a></li>
                    <li><a href="../blocos/{{current_user.username}}" class="nav-link"><i class="bi bi-pen"></i><h2> Blocos</h2></a></li>
                    <li><a href="../calendario/{{current_user.username}}" class="nav-link"><i class="bi bi-calendar"></i><h2> Calendário</h2></a></li>
                    <li><a href="../../configuracoes" class="nav-link"><i class="bi bi-gear"></i><h2> Configurações</h2></a></li>
                </ul>

                <div id="content_image">
                    <img id="photoUser" src="../../static/img/studying.jpg" alt="imgUser">
                </div>
                <div id="content_user">
                    <h2 id="User">{{current_user.username}}</h2>
                    <h2 id="Email">email@gmail.com</h2>
                </div>


            </nav>

            <div id="main_painel">
                
                Aqui vao ficar os trem lá tlg
            </div>
        </div>
    </main>

    <!-- Scripts do Bootstrap -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.6/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.min.js"></script>
</body>
</html>
