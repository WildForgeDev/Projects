<?php

include "db.php";
include "functions.php";
include "includes/header.php";
include "includes/footer.php";

create_user();

?>

    <style>h1 {text-align:center ;}</style>
    <h1>Create User</h1>
    <div class="container">
        <div class="col-sm-6">
            <form action="login-create.php" method="POST">

            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" name="username" class="form-control">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" name="password" class="form-control">
            </div>

            <div class="form-group">
                <input class="btn-primary" type="submit" name="submit" value="Submit">
            </div>

            </form>
        </div>

    <?php include "includes/footer.php"; ?>