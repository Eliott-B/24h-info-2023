<!DOCTYPE html>
<html>
<head>
    <?php include_once('includes/head.php'); ?>
	<title>\Ville\intelligente</title>
</head>
<body>

<?php include_once('includes/header.php'); ?>
        <h1>Créer un compte</h1>

            <form class="form1" action="requetes/register.php" method="post">
                <label for='pseudo' hidden>Pseudo</label>
                <input class='ch1' required type='text' id='pseudo' name='pseudo' minlength="1" placeholder='Pseudo'
                       pattern="^(?!.*[<>]).{1,}$"
                       title="Les caractères '<' & '>' ne sont pas autorisés"> <br>
                <label for='mdp' hidden>Mdp</label>
                <input class='ch1' required type='password' id='mdp' name='mdp' placeholder='Mot de passe'
                       
                       title="Critères : au moins 1 majuscule, 1 minuscule, 1 chiffre, 12 caractères minimum"> <br>
               <p>Résoudre :</p>
                <?php
                session_start();

                $captcha_a = rand(1, 20);
                $captcha_b = rand(1, 20);
                echo "<p>$captcha_a + $captcha_b =
                </p><input class='ch1' required type='number' id='captcha' name='captcha' placeholder='Réponse'> <br>";
                $_SESSION['captcha_a'] = $captcha_a;
                $_SESSION['captcha_b'] = $captcha_b;
                ?>
                <input class="se_connecter" type='submit' name='ok' value="S'inscrire"> <br><br>
            </form>
            <br>
       <button type="button" onclick="window.location.href='../login.php'">Retour</button>
    </div>
    <?php include_once('includes/footer.php'); ?>
</body>

</html>
<!-- pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*[<>]).{12,}$"  -->