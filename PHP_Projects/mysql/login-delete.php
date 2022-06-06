<?php

include "db.php";
include "functions.php";
include "includes/header.php";


delete_user();

?>

    
        <style>h1 {text-align:center ;}</style>
        <h1>Delete User</h1>
        <div class="container">
            <div class="col-sm-6">
                <form action="login-delete.php" method="POST">
                    <div class="form-group">
                        <select name="id" id="">
                            <?php 
                                get_all_users();
                            ?>
                        </select>
                    </div>
                    <div class="form-group">
                        <input class="btn-primary" type="submit" name="submit" value="DELETE">
                    </div>
                </form>
            </div>

    <?php include "includes/footer.php"; ?>