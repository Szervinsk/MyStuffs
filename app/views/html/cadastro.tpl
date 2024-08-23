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

      <script src="../../static/js/cadastro.js"></script>

      <div id="box">
        <h1 class="campText">Cadastro</h1>

        <form id="form_scroll" method="post" action="/cadastro">

          <div id="form-1">
            <img class="imgs" src="../../static/img/Online learning concept.png" alt="lindo" />
            <h1 id="mainText">Bem vindo a MyStuffs!</h1>
            <label for="username">Insira seu nome:</label>
            <input class="input" id="username" name="username" type="text" />
            <br />
            <btn class="btn , scroll_btn">Próximo</btn>
          </div>


          <div id="form-2">
            <img class="imgs" src="../../static/img/processing.png" alt="senha" />
            <h1 id="mainText">Segurança</h1>
            <label for="password">Insira sua senha:</label>
            <input class="input" id="password" name="password" type="password" />
            <br />
            <div class="btn , scroll_btn">Próximo</div>
          </div>
          

          <div id="form-3">
            <img class="imgs" src="../../static/img/processing.png" alt="senha" />
            <h1 id="mainText">Confirmar</h1>
            <label for="confirm_password">Confirme sua senha:</label>
            <input class="input" id="confirm_password" name="confirm_password" type="password"/>
            <br />
            <input class="btn " value="Realizar cadastro" type="submit" />
          </div>

        </form>
            % if error:
            <h3 style="color: red; font-size: 0.75em">{{ error }}</h3>
            % end

          <div id="div_balls">
            <ul id="balls">
              <li><input type="radio" name="ball" id="1" checked></li>
              <li><input type="radio" name="ball" id="2"></li>
              <li><input type="radio" name="ball" id="3"></li>
            </ul>
          </div>

      </div>
    </section>

    <img id="blurImage" src="../../static/img/blurImage.png" alt="fundoBlur" />
  </body>
</html>
