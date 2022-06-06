<?php

if(isset($_POST['submit'])){
    // get the submitted data
    $uid = $_POST['uid'];
    $pwd = $_POST['pwd'];

    //instantiate Logincontr class
include "../classes/dbh2.class.php";
include "../classes/login.class.php";
include "../classes/login.contr.class.php";

$login = new LoginContr($uid, $pwd);

// Running Error handlers and user signup

$login->loginUser();

// Navigate back to index 2
header("location: ../index2.php?error=none");
}

?>
