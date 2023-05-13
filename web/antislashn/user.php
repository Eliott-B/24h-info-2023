<?php
session_start();
if (!isset($_SESSION['pseudo']))
    {
		$redirect = "index.php";
		header("Location:$redirect");
	}
?>

<!DOCTYPE html>
<html lang='fr'>
<head>
    <?php include_once('includes/head.php'); ?>
</head>
<body>
<header>
<?php
    echo "<h1 class='bv'>Bonjour ";
    echo $_SESSION['pseudo'];

    echo "</h1>"
    ?>
    <button onclick="window.location.href='requetes/Deconnexion.php'">Déconnexion</button>
</header>
    <button type="submit" onclick="window.location = 'Ville/creationVille.php'">AJOUTER UNE VILLE</button>
    <div> <h3>Mes villes</h3>
        <?php
        session_start();
        require_once 'includes/variablesGlobales.php'; 
        $token = (bool)($connexion = mysqli_connect("localhost"
        ,"root","eliottavec2t" ));
        // je verifie ma connexion
        if($token){
    
            $token2 = ($bd=mysqli_select_db($connexion,"info"));
            if($token2){
    
                $table = "user";
                $pseudo = $_SESSION['pseudo'];

    
                $sql="SELECT id_u FROM user WHERE pseudo ='$pseudo'";
                $res = mysqli_query($connexion,$sql);
    
                $ligne = mysqli_fetch_row($res);
    
                $sqls = "SELECT nom_ville FROM ville WHERE user =$ligne[0]";
                $req = mysqli_query($connexion,$sqls);        
                echo "<form class=\"form1\" action=\"Ville/manageVille.php\" method=\"post\">";
                while ($ligne = mysqli_fetch_row($req)){
                    foreach($ligne as $v){
                        echo "<input class=\"creer\" type='submit' name='ok' id=".$v." value=".$v."> <br><br>";
                    }
                }
            }
        }
        
        ?>
    </div>
    
    
    
</body>
</html>