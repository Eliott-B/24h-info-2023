<?php
$token = (bool)($connexion = mysqli_connect("localhost"
,"root","eliottavec2t" ));
if($token){
    $token2 = ($bd=mysqli_select_db($connexion,"info"));
    if($token2){


        // if ($_SESSION['captcha_a'] + $_SESSION['captcha_b'] == $_POST['captcha']){

            $pseudo = $_POST['pseudo'];
            $sql="SELECT * FROM user WHERE pseudo='$pseudo'";
            
            $res = mysqli_query($connexion,$sql);

            $row = mysqli_fetch_assoc($res);
            if($row){

                echo "<script>alert('Pseudo déjà pris');
                window.location.href = '../register.php';</script>";
            }
            else{
                $pass = password_hash($_POST['mdp'], PASSWORD_DEFAULT);
                $table = "user";
                $sql="INSERT INTO $table (pseudo,mdp) VALUES ('$pseudo','$pass')";

                $res = mysqli_query($connexion,$sql);
                session_start();
                $_SESSION['pseudo'] = $pseudo;
                header("Location:../user.php");
            }
        // }
        // else{
        //     echo "<script>alert('Captcha incorrect');
        //     window.location.href = '../register.php';</script>";
        // }
    }
}

?>