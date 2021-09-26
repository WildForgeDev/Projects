<?php


function addNumbers($number1, $number2){
    $sum = $number1 + $number2;
    return $sum;
}

$result = AddNumbers(34, 64);
echo $result;
echo "<br></br>";

$result = AddNumbers($result, 300);
echo $result;
echo "<br></br>";


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
