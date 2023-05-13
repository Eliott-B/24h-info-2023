<?php
session_start();
require_once '../includes/variablesGlobales.php';
if (isset($_POST['ok'], $_POST['ville'])){
    $ville = $_POST['ville'];
    $token = (bool)($connexion = mysqli_connect("localhost"
    ,"root","eliottavec2t" ));
    // je verifie ma connexion
    if($token){

        $token2 = ($bd=mysqli_select_db($connexion,"info"));
        if($token2){
            // echo "coucou je suis et encore la";

            $table = "user";
            // $pseudo = (string) $pseudo;
            // $res ="SELECT id_u FROM user WHERE pseudo ='admin'";
            $pseudo = $_SESSION['pseudo'];

            $sql="SELECT id_u FROM user WHERE pseudo ='$pseudo'";
            // echo $sql;
            //pointeur
            $res = mysqli_query($connexion,$sql);

            $ligne = mysqli_fetch_row($res);

            $req = "INSERT INTO ville (nom_ville, user) VALUES ('$ville', $ligne[0])";
            
            // foreach($ligne as $valeur){
            //     echo $valeur;
            // }
            
            // $id_u = mysqli_query($connexion,$res);

            // $res ="INSERT INTO ville (nom_ville, user) VALUES ($ville, $ligne[0]);";
            
            $req = mysqli_query($connexion,$req);

            session_start();
                $_SESSION['pseudo'] = $pseudo;
                header("Location:../user.php");

            // // requetes sql
            // $sql = "INSERT INTO ville (nom_ville, user)
            //             VALUES (?, ?);";
            //     $sqlp = mysqli_prepare($connexion,$sql);
            //     mysqli_stmt_bind_param($sqlp,'si',$ville,$id_u);
            //     mysqli_stmt_execute($sqlp);

            //pointeur
    }
}
}
?>