
<!DOCTYPE html>
<html lang='fr'>
<head>

<?php include_once('../includes/head.php'); ?>
</head>
<body>
<?php

    
    if(isset($_POST['ok'])){
        echo "<a href='../user.php'><button type='button' onclick='window.location.href='../user.php'>Retour</button></a>";
        echo "<h2>Ville séléctionné : ";
        echo $_POST['ok'];
        echo "</h2>";
        
        require_once '../listObjet/listObjet.php';

        echo "<em>  (A prévoir : Pouvoir ajouter des objets à notre ville depuis une carte et voir l'impact énergétique.)</em>";
    
    }
    
?>

</body>
</html>