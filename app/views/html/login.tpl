<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="../../static/css/login.css">
</head>
<body>
    <nav>
        <a href="/"><img id="MyStuffs_logo" src="../../static/img/MyStuffs icon.png" alt="Logo"></a>
    </nav> 
    
    <section>
        <div id="box">
            <h1 class="campText">Login</h1>
            
            % if success:
            <h3 id="succes_message">{{success}}</h3>
            % end
            <img src="../../static/img/Business leader.png" alt="lindo">
            <h1 id="mainText">Olá usuário</h1>
            <form method="post" action="/login">

                <label for="username">Por favor insira seu nome:</label>
                <input class="input" id="username" name="username" type="text">
                <br>
                <label for="password">Por favor insira sua senha:</label>
                <input class="input" id="password" name="password" type="password">
                <br>
                <input id="btn" value="Enviar" type="submit" />
                
                % if error:
                <h3 style="color:red; font-size: 0.75em;">{{error}}</h3>
                % end
                
                <br>
                <a style="text-align:center; color:cornflowerblue; font-size: 0.75em;" href="/cadastro">Ainda nn possui cadastro?</a>
            </form>
        </div>
    </section>

    <img id="blurImage" src="../../static/img/blurImage.png" alt="fundoBlur">
</body>
</html>
