<?php


$file = "example.txt";


if($handle = fopen($file, 'r')){
    echo $content = fread($handle, filesize($file)); //each byte equals 1 character
    fclose($handle);
} else {
    echo "The file could not be written."; 
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
