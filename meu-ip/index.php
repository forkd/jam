<!doctype html>
<html lang="pt-br">
    <head>
        <meta name="description" content="Meu Endereço IP" />
        <meta name="keywords" content="ip, php, css, html5" />
        <meta name="author" content="Indiecode" />
        <meta charset="utf-8" /> 
        <title>Meu Endereço IP - Indiecode</title>

        <!-- Styles -->
        <link href="css/screen.css" rel="stylesheet" type="text/css" />
        <link href="http://fonts.googleapis.com/css?family=Days+One|Architects+Daughter" rel="stylesheet" type="text/css" />

        <link rel="shortcut icon" href="img/favicon.png" type="image/png" />
    </head>
    <body>
        <header>
            <p id="ask">Meu endereço IP é:</p>
        </header>
        
        <section id="content">
        
            <?php if ($_SERVER["HTTP_X_FORWARDED_FOR"] != "") {
				$IP = $_SERVER["HTTP_X_FORWARDED_FOR"];
				$proxy = $_SERVER["REMOTE_ADDR"];
				$host = @gethostbyaddr($_SERVER["HTTP_X_FORWARDED_FOR"]);
			} else {
				$IP = $_SERVER["REMOTE_ADDR"];
				$host = @gethostbyaddr($_SERVER["REMOTE_ADDR"]);
			} ?>
            
            <p id="ip"><?php echo $IP; ?></p>
            <p id="info_title">Detalhes:</p>
            <ul id="info_text">
			<?php 
				echo '<li>Remote Port: <span>'.$_SERVER["REMOTE_PORT"].'</span></li>';
				echo '<li>Request Method: <span>'.$_SERVER["REQUEST_METHOD"].'</span></li>';
				echo '<li>Server Protocol: <span>'.$_SERVER["SERVER_PROTOCOL"].'</span></li>';
				echo '<li>Server Host: <span>'.$host.'</span></li>';
				echo '<li>User Agent: <span>'.$_SERVER["HTTP_USER_AGENT"].'</span></li>'; 
				if ($proxy) echo '<li>Proxy: <span>'.($proxy) ? $proxy : ''.'</span></li>';
			?>
			</ul>            
        </section>

        <footer>
            <p id="credits">&copy; <a href="http://indiecode.com.br" title="Indiecode">Indiecode</a> baseado em <a href="http://perishablepress.com/" title="Perishable Press" target="_blank">Perishable Press</a>. Fontes por <a href="http://www.google.com/webfonts" title="Google Web Fonts" target="_blank">Google Web Fonts</a>.</p>
        </footer>

    <!--[if IE]>
    <a href="http://www.google.com/chrome?hl=pt-BR" target="_blank"><img id="noie" src="img/noie.png" alt="Baixar o Google Chrome" title="Baixar o Google Chrome" /></a>
    <![endif]-->
    </body>
</html>
