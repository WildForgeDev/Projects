<?php
include ("classes.php");

$canned_job_1 = new CannedJob(12345, 'test', 100.00);
$part1 = new Part(1234, 'part1', 50.00, 1.0, .09);
$part1->addFee(new Fee(1234, 'fee1', 5.00, .09));


$canned_job_1
    ->addLabor(new Labor(1234, 'labor1', 1.0, 25.00, .09))
    ->addLabor(new Labor(1234, 'labor2', 1.0, 25.00, .09))
    ->addPart($part1)
    ->addPart(new Part(1234, 'part2', 50.00, 1.0, .09))
    ->addPart(new Part(1234, 'part3', 50.00, 1.0, .09))
    ->adjustPrices();

echo $canned_job_1->getTotal();
echo"<br>";
echo json_encode($canned_job_1);

?>

