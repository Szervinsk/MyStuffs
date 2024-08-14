<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="../../static/css/landPage.css">
</head>
<body>
    
    % if login_message:
        <div class="message">{{login_message}}</div>
    % end

    <nav>
        <img id="MyStuffs_logo" src="../../static/img/MyStuffs icon.png" alt="Logo">
    
        % if current_user:
        <div id="perfil_lp">
            <h1>{{username}}</h1>
            <form action="/logout" method="post">
                <button type="submit">Logout</button>
            </form>
        </div>
        % else:
        <a id="login" href="/login">Login</a>
        % end
    </nav>
    
    <main>
        <div id="content_text">
            <h1 class="Title">Bem vindo ao</h1>
            <h1 class="Title-myStuffs">My Stuffs</h1>
            <h2 id="Subtitle">Organize suas ideias e conquiste seus objetivos com o nosso site de planejamento. Use blocos de nota para estruturar suas metas e transformar seus planos em realidade!</h2>
            
            % if current_user:
            <form action="/oficina/{{username}}" method="get">
                <button id="iniciar_projeto" type="submit">Iniciar Projetos</button>
            </form>
            % else:
            <form action="/login" method="get">
                <button id="iniciar_projeto" type="submit">Iniciar Projetos</button>
            </form>
            % end        

        </div>

        <img id="blurImage" src="../../static/img/blurImage.png" alt="fundoBlur">
    </main>
</body>
</html>
