<?php

class Car{


    function honk_horn(){
        echo "Beep Beep";
        echo "<br>";
    }
    function move_wheels(){
        echo "Car moves it's wheels.";
        echo "<br>";
    }
}

$car = new Car();
$car2 = new Car();

$car->honk_horn();
$car2->move_wheels();



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
