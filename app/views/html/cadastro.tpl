<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cadatro</title>
    <link rel="stylesheet" href="../../static/css/cadastro.css" />
  </head>
  <body>
    <nav>
      <a href="/"
        ><img
          id="MyStuffs_logo"
          src="../../static/img/MyStuffs icon.png"
          alt="Logo"
      /></a>
    </nav>

    <section>
      <div id="box">
        <h1 class="campText">Cadastro</h1>
        <img src="../../static/img/Business leader.png" alt="lindo" />
        <h1 id="mainText">Bem vindo a MyStuffs!</h1>

        <form method="post" action="/cadastro">
          <label for="username">Insira seu nome:</label>
          <input class="input" id="username" name="username" type="text" />

          <label for="password">Confirme sua senha:</label>
          <input class="input" id="password" name="password" type="password" />

          <label for="confirm_password">Insira sua senha:</label>
          <input
            class="input"
            id="confirm_password"
            name="confirm_password"
            type="password"
          />

          <br />
          <input id="btn" value="Realizar cadastro" type="submit" />

          % if error:
          <h3 style="color: red; font-size: 0.75em">{{ error }}</h3>
          % end
        </form>
      </div>
    </section>

    <img id="blurImage" src="../../static/img/blurImage.png" alt="fundoBlur" />
  </body>
</html>
