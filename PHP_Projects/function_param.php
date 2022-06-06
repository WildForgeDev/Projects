<?php


$name = "Billiem";

function say_something($name){
    echo "Hello ".$name.", Welcome to the party!";
    echo "<br>";
}

for($counter = 0; $counter < 11; $counter++){
    say_something($name);
}

function calculator($number1, $number2, $operator){
    switch($operator){
    case "-":
        echo $number1 - $number2;
        echo "<br>";
        break;
    case "+":
        echo $number1 + $number2;
        echo "<br>";
        break;
    case "/":
        echo $number1 / $number2;
        echo "<br>";
        break;
    case "*":
        echo $number1 * $number2;
        echo "<br>";
        break;  
    }
}
$number1 = 10;
$number2 = 10;
$operator = "*";
calculator($number1, $number2, $operator);

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