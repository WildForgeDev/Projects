<?php

include "db.php";
include "functions.php";
include "includes/header.php";
include "includes/footer.php";

$result = read_users();


?>


    <style>h1 {text-align:center ;}</style>
    <h1>Read Users</h1>
        <div class="container">
            <div class="col-sm-6">
                <table>
                    <tr>
                        <td>Username</td>
                        <td>Password</td>
                    </tr>  
                <?php
                read_user_table($result)              
                ?>
                    </tr>
                </table>
            </div>

        <?php include "includes/footer.php"; ?>