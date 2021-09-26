<?php

class Car{


    function honk_horn(){
        echo "Beep Beep";
    }


    function move_wheels(){
        echo "Car moves it's wheels.";
    }
}

if(method_exists('Car', 'move_wheels')){
    echo "The move_wheels method exists.";
} else {
    echo "The method move_wheels does not exist.";
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
