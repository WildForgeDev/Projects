<?php session_start(); ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width-device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital@1&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="index2.css">
</head>

<body>
    <header>
        <nav>
            <div>
                <h3>Chris Lakey</h3>
                <ul class="menu-main">
                    <li><a href="index.php">Home</a></li>
                    <li><a href="#">Products</a></li>
                    <li><a href="#">Current Sales</a></li>
                    <li><a href="#">Member+</a></li>
                </ul>
            </div>
            <ul class="menu-member">
                <?php
                    if(isset($_SESSION['userid'])){
                ?>
                        <li><a href="#"><?php echo $_SESSION['useruid'];?></a></li>
                        <li><a href="includes/logout.inc.php" class="header-login-a">LOGOUT</a></li> 
                <?php
                    } else {
                ?>
                        <li><a href="#">SIGN UP</a></li>
                        <li><a href="#" class="header-login-a">LOGIN</a></li>
                <?php
                    }
                ?>
            </ul>
        </nav>
    </header>

    <section class="index-intro">
        <div class="index-intro-bg">
            <div class="wrapper">
                <div class="index-intro-c1">
                    <div class="video"></div>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae suscipit magna.</p>
                </div>
                <div class="index-intro-c2">
                    <h2>We make<br>professional<br>gear</h2>
                    <a href="#">FIND OUR GEAR HERE</a>
                </div>
            </div>
        </div>
    </section>

    <section class="index-login">
        <div class="wrapper">
            <div class="index-login-signup">
                <h4>SIGN UP</h4>
                <p>Don't have an account yet? Sign up here!</p>
                <form action="includes/signup.inc.php" method="post">
                    <input type="text" name="uid" placeholder="Username">
                    <input type="password" name="pwd" placeholder="Password">
                    <input type="password" name="pwdRepeat" placeholder="Repeat Password">
                    <input type="text" name="email" placeholder="E-mail">
                    <br>
                    <button type="submit" name="submit">Sign Up</button>
                </form>
            </div>
            <div class="index-login-signup">
                <h4>LOGIN</h4>
                <p>Don't have an account yet? Sign up here!</p>
                <form action="includes/login.inc.php" method="post">
                    <input type="text" name="uid" placeholder="Username">
                    <input type="password" name="pwd" placeholder="Password">
                    <br>
                    <button type="submit" name="submit">Login</button>
                </form>
            </div>
        </div>
    </section>
</body>

</html>