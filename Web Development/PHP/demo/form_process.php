<?php


if(isset($_POST['submit'])){
    $minimum = 5;
    $maximum = 15;
    $names = array("Edwin", "Christopher", "James", "Steven", "Wesley", "Lauren" ,"Joe");

    $username = $_POST['username'];
    $password = $_POST['password'];
    
    if(strlen($username) < $minimum) {
        echo "Username must be longer than 5 characters.";
    } else if (strlen($username)> $maximum){
        echo "Username must be less than 15 characters.";
    }

    if(!in_array($username, $names)){
        echo "Sorry you cannot login.";
    } else{
        echo "Welcome!";
        echo "<br>";
        echo "Hello " . $username . "!";
        echo "<br>";
        echo "Your password is " . $password. ".";
    }


    // echo "Hello " . $username . "!";
    // echo "<br>";
    // echo "Your password is " . $password. ".";
}


?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
