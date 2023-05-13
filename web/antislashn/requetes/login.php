<?php

$token = (bool)($connexion = mysqli_connect("localhost"
,"root","eliottavec2t" ));
// je verifie ma connexion
if($token){
    $token2 = ($bd=mysqli_select_db($connexion,"info"));
    if($token2){
        if (isset($_POST['connexion']))
        {
            $pseudo = $_POST['pseudo'];
            $pass = $_POST['mdp'];
            $table = "user";
            // requetes sql
            $sql="select * from $table where '$pseudo' = pseudo";
            //pointeur
            $res = mysqli_query($connexion,$sql);

            $ligne = mysqli_fetch_row($res);

            if (password_verify($pass, $ligne[2])){
                echo "Connexion en cours";
                session_start();
                $_SESSION['pseudo'] = $pseudo;
                header("Location:../user.php");
            }
            else{
                             
                echo "<script>alert('Votre mot de passe est invalide.');
                window.location.href = '../login.php';</script>";
            }

        }
    }
}


?>