<?php session_start(); 

?>
<!DOCTYPE html>
<html lang='fr'>
<head>
    <?php include_once('../includes/head.php'); ?>
</head>
<body>
    <?php include_once('../includes/header.php'); ?>
    <h1>Bienvenue dans la création de la ville du futur</h1>
    <form class="form1" action="../requetes/creationVille.php" method="post">
        <label for='ville' hidden>Ville</label>
        <input class='ch1' required type='text' id='ville' name='ville' minlength="1" placeholder='Nom Ville'>
        <input class="creer" type='submit' name='ok' id='ok' value="Créer"> <br><br>
    </form>
    <?php include_once('../includes/footer.php'); ?>
</body>
</html>