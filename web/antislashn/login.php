<!DOCTYPE html>
<html>
<head>
    <?php include_once('includes/head.php'); ?>
	<title>\Ville\intelligente</title>
</head>
<body>

<!-- <header> -->
<?php include_once('includes/header.php'); ?>
<!-- </header> -->
    <h1>Connexion</h1>

    <form class="form1" action="requetes/login.php" method="post">
        <label for='pseudo' hidden>Pseudo</label>
        <input class='ch1' type='text' id="pseudo" name='pseudo' placeholder='Entrez votre pseudonyme' autofocus> <br>
        <label for='mdp' hidden>Mot de passe</label>
        <input class='ch1' type='password' id="mdp" name='mdp' placeholder='Votre mot de passe' > <br>
        <input type='submit' name='connexion' value='Connexion'> <br><br>
        <a class='link' href='register.php'>Créer un compte</a> <br>
        <!-- <a class='mdp_oublie' href='../../404/Page404.html'>Mot de passe oublié</a> -->
    </form>
    <br>
    <button type="button" onclick="window.location.href='../'">Retour</button>

</body>
</html>







