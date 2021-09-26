<?php


$name = "Chris";
$age = 31;
$career = "Software Developer";
$marital_status = "Married";
$years_married = 2;
$number1 = 45;
$number2 = 10;
$number3 = 17;

if($number1 > $number2){
    echo "This is true";
    echo "<br></br>";
}

if(4 <= 4){
    echo "four is greater than or equal to four";
    echo "<br></br>";
}

if(4 !== "4"){
    echo "the string 4 is not the same as the number 4.";
    echo "<br></br>";
}

if(4 < 5 || 5 > 2){
    echo "Or statement is running";
    echo "<br></br>";
}

if(5 == 5 && 6 == 6){
    echo "The and statement is running";
    echo "<br></br>";
}

if($marital_status == "Married" && $years_married > 1 && $years_married < 3){
    echo "You have been married for two years.";
    echo "<br></br>";
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
