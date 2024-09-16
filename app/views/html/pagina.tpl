<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="../../static/css/landPage.css">
    <script src="../../static/js/LandPage.js"></script>
</head>
<body>
    
    % if message:
        <div id="msg" class="message">{{message}}</div>
    % end

    <nav>
        <img id="MyStuffs_logo" src="../../static/img/MyStuffs icon.png" alt="Logo">
    
        % if current_user:
        <div id="div_perfil">
            <a style="text-decoration: none; color:black" href="/configuracoes/{{username}}"><h1 id="User">{{username}}</h1></a>
            <form action="/logout" method="post">
                <button id="logout_btn" type="submit">Logout</button>
            </form>
        </div>
        % else:
        <a id="login_btn" href="/login">Login</a>
        % end
    </nav>
    



    <main>
        <section id="content_text">

            <div id="div_title">
                <h2>Bem vindo ao</h2>
                <h1>My Stuffs</h1>

                <h3 id="Subtitle">Organize suas ideias e conquiste seus objetivos com o nosso site de planejamento. Use blocos de nota para estruturar suas metas e transformar seus planos em realidade!</h3>
            </div>
            
            
            % if current_user:
            <form action="/oficina/{{username}}" method="get">
                <button id="btn" type="submit">Iniciar Projetos</button>
            </form>
            % else:
            <form action="/login" method="get">
                <button id="btn" type="submit">Iniciar Projetos</button>
            </form>
            % end        
        </section>

        <img id="blurImage" src="../../static/img/blurImage.png" alt="fundoBlur">
    </main>
</body>
</html>
