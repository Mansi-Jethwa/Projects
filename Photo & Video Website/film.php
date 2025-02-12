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
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">


    <!-- css Link --> 
    <link rel="stylesheet" href="style.css">
    <style>


    h2, h3 {
        color: #222;
        font-family: 'Open Sans', sans-serif;
    }

    h2 {
        font-size: 2.5em;
        margin-bottom: 10px;
        font-family: 'Open Sans', sans-serif;
        color: pink; /* Changed color to pink */
    }

    h3 {
        font-size: 1.2em;
        line-height: 1.8;
        font-family: 'Open Sans', sans-serif;
    }

    /* Heading Section */
    .heading {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        background: linear-gradient(to bottom, rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('h2.jpg') center/cover no-repeat;
        color: white;
        text-align: center;
    }

    .heading h2 {
        font-size: 3em;
        font-family: 'Open Sans', sans-serif;
        color: #FF6969; /* Apply pink color to the heading section as well */
    }

    /* Services Section */
    .services {
        width: 85%;
        margin: 50px auto;
        padding: 30px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .services h2 {
        color: #FF6969; /* Changed the color to pink for services section */
        font-size: 2.2em;
        margin-bottom: 15px;
        border-bottom: 2px solid #FF6969; /* Pink border */
        padding-bottom: 10px;
    }

    .services h3 {
        margin-bottom: 20px;
    }
</style>


</head>
<body><div class="glass-container">
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
                <?php echo $loginButton; ?>    </nav>
    <div id="menu-btn" class="fas fa-bars"></div>
</section>
    <!-- header section ends -->

<div class="heading" style="background:url(h2.jpg) no-repeat">
    <h1>Services</h1>
</div>
<section class="services">
<div>
    <h2>Wedding Photography & Videography</h1>
    <h3>Our wedding photography services include capturing candid moments, group shots, and details like rings and decor. We specialize in natural light photography, ensuring beautiful, authentic images. Our videography services cover the entire wedding day, capturing emotional vows, speeches, and candid moments. We create cinematic highlight reels and full-length wedding films. Our team uses high-quality equipment to ensure stunning video quality.</h3>
    
    <h2>Event Coverage</h2>
    <h3>We specialize in providing comprehensive event coverage that ensures every significant moment is captured and immortalized. Our experienced team of photographers, videographers, and reporters are dedicated to delivering high-quality content that reflects the essence and excitement of your event. Our post-production services include editing, retouching, and packaging your photos and videos into beautiful keepsakes. We provide digital and physical copies to suit your needs.</h3>
    
    <h2>Editing & Post Production</h2>
    <h3>We specialize in turning raw footage into polished masterpieces. Our comprehensive editing and post-production services ensure that your project not only meets but exceeds your expectations.</h3>
    <h3>Narrative Editing: Crafting a compelling story from your footage.</h3>
    <h3>Corporate & Event Editing: Professional and engaging edits for corporate videos, events, and promotional content.</h3>
    <h3>Music Videos: Syncing visuals with the beat to create captivating music videos.</h3>

    <h2>Change your DVD, VHS, DVC to Pendrive</h2>
    <h3>Are you looking to safeguard your precious memories stored on DVDs, VHS tapes, or DVC cassettes? Our professional transfer service is here to help. We specialize in converting your old media formats into modern, high-quality digital files, conveniently stored on a USB pendrive.</h3>
    <h3>High-Quality Conversion: We use state-of-the-art equipment to ensure your memories are transferred with the highest possible fidelity.</h3>
    <h3>All Formats Supported: Whether you have DVDs, VHS tapes, or DVC cassettes, we can handle it all.</h3>
    <h3>Convenient Digital Storage: Your converted files will be saved on a USB pendrive, making them easy to share, view, and back up.</h3>
    <h3>Fast and Reliable Service: We understand the value of your memories, and our team works efficiently to deliver your digital files quickly.</h3>
</div>
</section>






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