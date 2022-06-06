<?php

class Car{

    public $wheels = 4;
    protected $hood = 1;
    private $engine = 1;
    static $color = "red";
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

    function print_hood(){
        echo $this->hood;
        echo "<br>";
    }

    function print_engine(){
        echo $this->engine;
        echo "<br>";
    }

    function print_doors(){
        echo $this->doors;
        echo "<br>";
    }

    function print_color(){
        echo $this->color;
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

class Semi extends Car{
    
    function show_stuff(){
        echo $this->hood;
        echo "<br>";
        echo $this->engine;
        echo "<br>";
        echo $this->color;
        echo "<br>";
    }
}

$car = new Car();
echo Car::$color;
echo $car->color;

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
