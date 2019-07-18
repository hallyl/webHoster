<?php

$user = "Derrick"
$pass = "hallyl"

if(isset($_POST["submit"])){
	if($_POST["username"] == $user && $_POST["password"] == $pass){
	
	}
	else{
		echo "Incorrect Login";
		}
}

?>
