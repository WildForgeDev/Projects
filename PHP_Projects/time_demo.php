<?php

$starttime = new DateTime('2021-10-27 08:00:00');
$endtime = new DateTime('2021-10-27 08:30:00');
$diff =  $endtime->format('U') -$starttime->format('U');

$new_diff = $diff/60/60;


echo $new_diff;



?>