<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadatro</title>
</head>
<body>

    <h1> Cadastro </h1>
    <form style="width: 20em; display: flex; flex-direction: column;" method="post" action="/cadastro">
        <label for="username">Insira seu nome:</label>
        <input id="username" name="username" type="text">

        <label for="password">Insira sua senha:</label>
        <input id="password" name="password" type="password">
        
        <label for="confirm_password">Insira sua senha:</label>
        <input id="confirm_password" name="confirm_password" type="password">

        <br>
        <input value="Realizar cadastro" type="submit" />
        
        % if error:
            <h3 style="color:red; font-size: 0.75em;">{{error}}</h3>
        % end

    </form>
</body>
</html>
