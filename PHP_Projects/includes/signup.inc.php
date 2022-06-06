<?php

if(isset($_POST['submit'])){
    // get the submitted data
    $uid = $_POST['uid'];
    $pwd = $_POST['pwd'];
    $pwdRepeat = $_POST['pwdRepeat'];
    $email = $_POST['email'];

    //instantiate Signupcontr class
include "../classes/dbh2.class.php";
include "../classes/signup.class.php";
include "../classes/signup-contr.class.php";

$signup = new SignupContr($uid, $pwd, $pwdRepeat, $email);

// Running Error handlers and user signup

$signup->signupUser();

// Navigate back to index 2
header("location: ../index2.php?error=none");
}

?>