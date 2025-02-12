<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    // If the user is not logged in, redirect to the login page
    header("Location: login.php");
    exit();
}

// Your code for displaying the main content of the index.php page
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>

    <!-- Swiper css link -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>

    <!-- font awesome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link
      href="https://cdn.jsdelivr.net/npm/remixicon@3.2.0/fonts/remixicon.css"
      rel="stylesheet"
    />
    <!-- css Link -->
    <link rel="stylesheet" href="style.css">
    <style>
 
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 20px;
    justify-content: center;
    cursor:pointer;
}

.gallery-item {
    flex: 1 1 30%;
    max-width: 300px;
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    cursor:pointer;
}

.gallery-image {
    width: 100%;
    display: block;
    transition: transform 0.3s ease;
    cursor:pointer;
}

.gallery-item:hover .gallery-image {
    transform: scale(1.1);
    cursor:pointer;
}

/* Lightbox styles */
.lightbox {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.9);
    cursor:pointer;
}

.lightbox-content {
    display: block;
    margin: auto;
    max-width: 80%;
    max-height: 80%;
    margin-top: 50px;
    cursor:pointer;
}

.close {
    position: absolute;
    top: 15px;
    right: 35px;
    color: white;
    font-size: 40px;
    font-weight: bold;
    transition: 0.3s;
    cursor: pointer;
}

.close:hover,
.close:focus {
    color: #bbb;
    text-decoration: none;
    cursor: pointer;
}

        </style>

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
                
        <!-- Check if the user is logged in to display the appropriate button -->
        <?php if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true): ?>
            <!-- Logout button -->
            <a href="logout.php"><img src="logout.png" alt="Logout"></a>
        <?php else: ?>
            <!-- Login button -->
            <a href="login.php"><img src="enter.png" alt="Login"></a>
        <?php endif; ?>
    </nav>
    <div id="menu-btn" class="fas fa-bars"></div>
</section>
    <!-- header section ends -->

    <!-- home section starts -->
    <section class="home">
        <div class="swiper home-slider">
            <div class="swiper-wrapper">
                <div class="swiper-slide slide" style="background:url(home.JPG) no-repeat">
                    <div class="content">
                        <span>Our Lences, Your Legacy.</span>
                        <h3>Your Life, Our Camera, Their Envy.</h3>
                        <a href="film.php" class="btn">Discover More</a>
                    </div>
                </div>

                <div class="swiper-slide slide" style="background:url(home2.JPG) no-repeat">
                    <div class="content">
                    <span>Our Lences, Your Legacy</span>
                    <h3>Photography With A Personal Touch.</h3>
                    <a href="film.php" class="btn">Discover More</a>
                    </div>
                </div>

                <div class="swiper-slide slide" style="background:url(home3.JPG) no-repeat">
                    <div class="content">
                    <span>Our Lences, Your Legacy</span>
                    <h3>Frame Your Life, Love Your Memories.</h3>
                    <a href="film.php" class="btn">Discover More</a>
                    </div>
                </div>
            </div>
            <div class="swiper-button-next"></div>
            <div class="swiper-button-prev"></div>

        </div>
    </section>
    <!-- home section ends -->

<!-- wedding section starts -->
<!--<section class="film">
    <h1 class="heading-title"> Services </h1>
    <div class="box-container">
        <div class="box">
            <img src="wed.png" alt="">
                <h3>Wedding Photography and Videography</h3>
        </div>
        <div class="box">
            <img src="event.png" alt="">
                <h3>Event Coverage</h3>
        </div>
        <div class="box">
            <img src="port.png" alt="">
                <h3>Portrait Sessions</h3>
        </div>
        <div class="box">
            <img src="product.png" alt="">
                <h3>Commercial Photography and Videography</h3>
        </div>
        <div class="box">
            <img src="vi.png" alt="">
                <h3>Editing and Post Production</h3>
        </div>
        <div class="box">
            <img src="online.png" alt="">
                <h3>Online Booking and Availability</h3>
        </div>
    </div>
</section> -->
<!-- wedding section ends -->
<!-- home packages section starts -->
<br>
<br>
<h1 class="pack">OUR PACKAGES</h1>
<section class="pricing">
    
    <div class="card-wrapper">
        <!-- card header -->
        <div class="card-header">
            <img src="MANSI.png">
            <h2>Silver</h2>
        </div>
        <!-- card detail -->
        <div class="card-detail">
            <p><span class="fas fa-check check "></span><b>3</b> hour video Sesion</p>
            <p><span class="fas fa-check check "></span><b>30</b> pages album</p>
            <p><span class="fas fa-check check "></span> Photobook & Calender</p>
            <p><span class="fas fa-check check "></span><b>1</b> day photography</p>
            <p><span class="fas fa-check check "></span>For Engagement and Birthday</p>
        </div>
        <!-- card price -->
        <div class="card-price">
            <p><sup>17500 &#8377</sup></p>
        </div>
        <!-- button -->
        <a href="contact.php?package=silver" class="card-button">I WANT IT</a>
    </div>
    <div class="card-wrapper">
        <!-- card header -->
        <div class="card-header">
            <img src="MANSI.png">
            <h2>Golden</h2>
        </div>
        <!-- card detail -->
        <div class="card-detail">
            <p><span class="fas fa-check check "></span><b>4</b> hour video Sesion</p>
            <p><span class="fas fa-check check "></span><b>40</b> pages album</p>
            <p><span class="fas fa-check check "></span> Photobook & Calender</p>
            <p><span class="fas fa-check check "></span><b>2</b> days photography</p>
            <p><span class="fas fa-check check "></span>For BabyShower and Marriage</p>
        </div>
        <!-- card price -->
        <div class="card-price">
            <p><sup>40000 &#8377</sup></p>
        </div>
        <!-- button -->
        <a href="contact.php?package=golden" class="card-button">I WANT IT</a>
    </div>
    <div class="card-wrapper">
        <!-- card header -->
        <div class="card-header">
            <img src="MANSI.png">
            <h2>Platinum</h2>
        </div>
        <!-- card detail -->
        <div class="card-detail">
            <p><span class="fas fa-check check "></span><b>5</b> hour video Sesion</p>
            <p><span class="fas fa-check check "></span><b>50</b> pages album</p>
            <p><span class="fas fa-check check "></span> Photobook & Calender</p>
            <p><span class="fas fa-check check "></span><b>3</b> days photography</p>
            <p><span class="fas fa-check check "></span>For Marriage</p>
        </div>
        <!-- card price -->
        <div class="card-price">
            <p><sup>72000 &#8377</sup></p>
        </div>
        <!-- button -->
        <a href="contact.php?package=platinum" class="card-button">I WANT IT</a>
    </div>
    
</section>

<!-- home about section start -->
<section class="home-about">
    <div class="content">
        <h3>ABOUT US</h3>
        <p>Welcome to Mansi Photo & Video! 📸✨ Capturing moments, emotions, and memories—that's what we live for. At Mansi Photo & Video, we believe that every click of the shutter freezes a unique story in time. Our journey began with a passion for visual storytelling, and over the years, it has evolved into a full-fledged love affair with the art of photography.</p>
        <a href="about.php" class="btn">Read More</a>
    </div>
</section>
 <!-- home about section ends --> 
<!-- wedding section starts -->
<div class="gallery-container">
        <div class="gallery-item">
            <img src="t8.jpg" alt="Photo 1" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="a3.jpg" alt="Photo 2" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="a4.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="a6.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="a8.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="t1.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="t2.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="t3.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="a9.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="t6.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="t7.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <div class="gallery-item">
            <img src="t9.jpg" alt="Photo 3" class="gallery-image">
        </div>
        <!-- Add more images as needed -->
    </div>

    <!-- Lightbox Modal -->
    <div id="lightbox" class="lightbox">
        <span class="close">&times;</span>
        <img class="lightbox-content" id="lightbox-img">
    </div>


<!-- wedding section ends -->

<section class="test">
<div class="section__container">
      <div>
        <h1 class="h">TESTIMONIALS<h1>
        <p class="pr">What our clients say about us.</p>
        <br>
      </div>
      <div class="testimonials__grid">
        <div class="card">
          <span><i class="ri-double-quotes-l"></i></span>
          <p>
          Amazing work displayed by them in my wedding. The quality of photos and videos are outstanding. You can hire them without a doubt.
          </p>
          <hr />
          <img src="t1.jpg" alt="user" />
          <p class="name">Prem & Vaishali</p>
        </div>
        <div class="card">
          <span><i class="ri-double-quotes-l"></i></span>
          <p>
          I was quite surprised how professionally they worked. They were so organised and the photos came out too good. Personally, I loved their work and would like to count on them anytime in future.


          </p>
          <hr />
          <img src="t2.jpg" alt="user" />
          <p class="name">Vishal & Mital</p>
        </div>
        <div class="card">
          <span><i class="ri-double-quotes-l"></i></span>
          <p>
            Love my wedding and prewedding work amazing experiance. Thanka a lot we choose you.
          </p>
          <hr />
          <img src="t3.jpg" alt="user" />
          <p class="name">Ravi & Hetvi</p>
        </div>
      </div>
      
    </div>
</section>
<section class="contact-container">
    <form action="submit_feedback.php" method="POST" class="contact-left">
        <div class="contact-left-title">
            <h2>Give a feedback</h2>
            <hr>
        </div>
        <input type="hidden" name="access_key" value="0ccf62e4-d34c-4a01-be46-346687a58998">

        <input type="text" name="name" placeholder="Your Name" class="contact-inputs" required>
        <input type="email" name="email" placeholder="Your Email" class="contact-inputs" id="cp" required title="Please enter a valid email">
        <textarea name="message" placeholder="Your Feedback" class="contact-inputs" required></textarea>
        <button type="submit">Submit<img src="arrow_icon.png" alt=""></button>
        </form>
    <div class="contact-right">
        <img src="right_img.png" alt="">
        <br>
        <br>
        <br>
</div>
</section> 

<!-- home packages section ends -->
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
    <script>
        const glassContainer = document.getElementById('glass-container');
        
        glassContainer.addEventListener('mouseover', () => {
            glassContainer.style.backdropFilter = 'blur(20px)';
            glassContainer.style.webkitBackdropFilter = 'blur(20px)';
        });

        glassContainer.addEventListener('mouseout', () => {
            glassContainer.style.backdropFilter = 'blur(10px)';
            glassContainer.style.webkitBackdropFilter = 'blur(10px)';
        });
    </script>
        <script>
    document.addEventListener("DOMContentLoaded", function () {
    const galleryImages = document.querySelectorAll(".gallery-image");
    const lightbox = document.getElementById("lightbox");
    const lightboxImg = document.getElementById("lightbox-img");
    const closeBtn = document.querySelector(".close");

    galleryImages.forEach(image => {
        image.addEventListener("click", function () {
            lightbox.style.display = "block";
            lightboxImg.src = this.src;
        });
    });

    closeBtn.addEventListener("click", function () {
        lightbox.style.display = "none";
    });

    lightbox.addEventListener("click", function (event) {
        if (event.target === lightbox) {
            lightbox.style.display = "none";
        }
    });
});
</script>
    </div>
</body>
</html>

