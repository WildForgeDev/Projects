<?php

class Car{

    var $wheels = 4;
    var $hood = 1;
    var $engine = 1;
    var $doors = 4;


    function __construct(){
        echo $this->wheels = 5;
        echo "<br>";
    }


    function honk_horn(){
        echo "Beep Beep";
        echo "<br>";
    }
    function move_wheels(){
        
        echo "Car moves it's $this->wheels wheels.";
        echo "<br>";
    }
}

class Plane extends Car{
    var $wheels = 0;
    var $hood = 0;
    var $engine = 2;
    var $doors = 1;

    function honk_horn(){
        echo "Planes don't have horns!";
        echo "<br>";
    }
}

$car = new Car();


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
