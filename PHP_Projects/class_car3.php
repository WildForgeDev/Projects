<?php

class Car{

    var $wheels = 4;
    var $hood = 1;
    var $engine = 1;
    var $doors = 4;

    function honk_horn(){
        echo "Beep Beep";
        echo "<br>";
    }
    function move_wheels(){
        
        echo "Car moves it's $this->wheels wheels.";
        echo "<br>";
    }
}

$car = new Car();
$car2 = new Car();
echo $car->wheels;
echo "<br>";
$car->honk_horn();
$car2->move_wheels();
$truck = new Car();
$truck->wheels = 18;
$truck->move_wheels();




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
