<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    $loginButton = '<a href="login.php"><img src="enter.png" alt="Login"></a>';
} else {
    $loginButton = '<a href="logout.php"><img src="logout.png" alt="Logout"></a>';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>

    <!-- Swiper css link -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>

    <!-- font awesome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

    <!-- css Link -->
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="glass-container">
    <!-- header section starts -->
    <section class="header">
    <a href="index.php" class="logo">Mansi Photo & Video</a>
    <nav class="navbar">
        <a href="index.php">Home</a>
        <a href="about.php">About Us</a>
        <a href="film.php">Services</a>
        <a href="contact.php">Book</a>
        <a href="contactus.php">Contact Us</a>
<!-- Check if the user is logged in and show the booking history link -->
<?php if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true): ?>
                    <a href="booking_history.php">Booking History</a>
                    
                <?php endif; ?>
                <?php echo $loginButton; ?>
    </nav>
    <div id="menu-btn" class="fas fa-bars"></div>
</section>
    <!-- header section ends -->

<div class="heading" style="background:url(h1.jpg) no-repeat">
    <h1>About Us</h1>
</div>

<!-- about section starts -->
    <section class="about">
        <div class="image">
            <img src="ab.JPG">
</div>
        <div class="content">
            <h3 class="hii">Why Choose Us?</h3>
            <p class="byy">At Mansi Photo and Video, we believe that every click of the shutter freezes a unique story in time. Our journey began with a passion for visual storytelling, and over the <b>18 years</b>, it has evolved into a full-fledged love affair with the art of photography. We don't just take pictures; we create visual narratives. Our approach is a blend of professionalism and personal connection. We take the time to understand your vision, whether it's a wedding, a family portrait, or a corporate event. Our goal is to capture the essence of the moment—the laughter, the tears, and everything in between.</p>

            <h3 class="hii">Who we are?</h3>
            <p class="byy">Founded by <b>Amit Jethwa</b>, a seasoned photographer and videographer with over 18 years of experience, our studio is built on a foundation of creativity, professionalism, and an unwavering commitment to excellence. Mansi's journey began with a simple love for the art of photography, which has since evolved into a full-fledged career capturing the essence of life's most precious moments.</p>

            
            </div>
    </section>
<!-- about section ends -->






     <!-- footer section starts -->
     <footer class="footer">
    <div class="footer-content">
    <div class="footer-section social">
            <a href="https://www.facebook.com/manshiprajapati.manshiprajapati.5/" class="social-link"><i class="fab fa-facebook-f"></i></a>
            <a href="https://www.instagram.com/mansi_beauty_bridal_studio/" class="social-link"><i class="fab fa-instagram"></i></a>
            <a href="https://www.youtube.com/@canonindiapvtltd" class="social-link"><i class="fab fa-youtube"></i></a>
        </div>
    </div>
    <div class="footer-bottom">
        &copy; 2024 Created by Mansi Jethwa | All rights reserved!
    </div>
</footer>
<!-- footer section ends --><!-- footer section ends -->



    <!-- swiper js link -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <!-- js file link -->
    <script src="script.js"></script>
</body>
</html>