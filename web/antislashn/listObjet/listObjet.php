<?php
echo "<h1>";
echo $_POST['filtrePar'];
echo "</h1>";
if (!$_POST['filtrePar'] === null){
    $para = (string) $_POST['filtrePar'];
}
else{
    $para = "nom_objet";
}
echo "<script src='listObjet.js'> </script>";
$token = (bool)($connexion = mysqli_connect("localhost"
,"root","eliottavec2t" ));
// je verifie ma connexion
if($token){
    $token2 = ($bd=mysqli_select_db($connexion,"info"));
    if($token2){
        $table = "objet";
        // requetes sql
        $sql="select nom_objet, description_objet, consomation from $table order by nom_objet";
        //pointeur
        $res = mysqli_query($connexion,$sql);
        //pour lire la premiere ligne
        echo "<table>";
        echo "<tr><th> Nom </th><th> Description </th><th> kW / mois </th><th>
        <form class='form1' id='form1' method='post' action='manageVille.php'>

            <select form='form1' #filtre id='filtre' name='filtre >
                <option value=''>--none--</option>
                <option id='0' value='nomobjet'>Nom</option>
            </select>
            <button type='button' onclick='filtreObjet()'>Trier</button>
        </form>
        </tr>";
        while($ligne = mysqli_fetch_row($res)){
            echo "<tr>";
            foreach($ligne as $v){

                echo "<td '>".$v."</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    }
    include "formSQL.php";
}
?>