<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="../../static/css/login.css">
</head>
<body>
    <img id="MyStuffs_logo" src="../../static/img/MyStuffs icon.png" alt="Logo">

    % if sucess:
    <h3 style="color:rgb(10, 198, 104); font-size: 0.75em;">{{sucess}}</h3>
    % end
    
    <h1>Login</h1>
        <div id="caixa">
            <img src="../../static/img/Business leader.png" alt="lindo">
            <br>
            <h1 style="text-align: center;">Olá</h1>
            <form style="width: 20em; display: flex; flex-direction: column;" method="post" action="/login">
                <label for="username">Por favor insira seu nome:</label>
                <input class="input" id="username" name="username" type="text">
                <br>
                <label for="password">Insira sua senha:</label>
                <input class="input" id="password" name="password" type="password">
                <br>
                <input value="Enviar" type="submit" />
                
                % if error:
                    <h3 style="color:red; font-size: 0.75em;">{{error}}</h3>
                % end
        
                <br>
                <a style="text-align:center; color:cornflowerblue; font-size: 0.75em;" href="/cadastro">Ainda nn possui cadastro?</a>
        
            </form>
        </div>

    <img id="blurImage" src="../../static/img/blurImage.png" alt="fundoBlur">
</body>
</html>
