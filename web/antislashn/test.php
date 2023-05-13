<?php

$token = (bool)($connexion = mysqli_connect("localhost"
,"root","eliottavec2t" ));
// je verifie ma connexion
if($token){
    $token2 = ($bd=mysqli_select_db($connexion,"info"));
    if($token2){
        $table = "user";
        // requetes sql
        $sql="select * from $table";
        //pointeur
        $res = mysqli_query($connexion,$sql);
        //pour lire la premiere ligne
        echo "<table>";
        echo "<tr><th> id </th><th> nom </th><th> mdp </th><th> groupe </th></tr>";
        while($ligne = mysqli_fetch_row($res)){
            echo "<tr>";
            foreach($ligne as $v){

                echo "<td>".$v."</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    }
    include "formSQL.php";
}