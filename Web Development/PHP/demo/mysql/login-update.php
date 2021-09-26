<?php

include "db.php";
include "functions.php";
include "includes/header.php";
include "includes/footer.php";

update_user();


?>

        <style>h1 {text-align:center ;}</style>
        <h1>Update User</h1>
        <div class="container">
            <div class="col-sm-6">
                <form action="login-update.php" method="POST">
                    <div class="form-group">
                        <label for="username">Username</label>
                        <input type="text" name="username" class="form-control">
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" name="password" class="form-control">
                    </div>
                    <div class="form-group">
                        <select name="id" id="">
                            <?php 
                                get_all_users();
                            ?>
                        </select>
                    </div>
                    <div class="form-group">
                        <input class="btn-primary" type="submit" name="submit" value="UPDATE">
                    </div>
                </form>
            </div>
       
        <?php include "includes/footer.php"; ?>