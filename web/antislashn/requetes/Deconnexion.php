<?php
session_start();
session_destroy();
$redirect = "../index.php";
header("Location:$redirect");
exit();
?>