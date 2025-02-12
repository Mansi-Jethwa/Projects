<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    $loginButton = '<a href="login.php"><img src="enter.png" alt="Login"></a>';
} else {
    $loginButton = '<a href="logout.php"><img src="logout.png" alt="Logout"></a>';
}
?><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>

    <!-- Swiper css link -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>

    <!-- font awesome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

     <!-- Google Font link -->
     <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

    <!-- css Link -->
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }


        .contact {
            padding: 60px 20px;
            background-color: #f9f9f9;
        }

        .content {
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }

        .content h1 {
            font-size: 36px;
            color: #333;
            margin-bottom: 20px;
            text-align: center;
            font-weight: 500;
        }

        .content h2, .content h3 {
            color: #555;
            margin-bottom: 10px;
            font-weight: 400;
        }

        .content h3 {
            font-size: 18px;
            color: #777;
        }

        .content table {
            width: 100%;
            margin-bottom: 20px;
            font-size: 16px;
        }

        .content iframe {
            width: 100%;
            height: 300px;
            border: none;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        @media (max-width: 1024px) {
            .header {
                flex-direction: column;
                align-items: flex-start;
                padding: 10px;
            }

            .navbar {
                flex-direction: column;
                gap: 10px;
            }

            .content iframe {
                height: 250px;
            }

            .content table {
                font-size: 20px; /* Adjust font size for medium screens */
            }
        }

        @media (max-width: 768px) {
            .header {
                flex-direction: column;
                align-items: flex-start;
                padding: 10px;
            }

            .navbar {
                flex-direction: column;
                gap: 10px;
            }

            .content iframe {
                height: 200px;
            }

            .content table {
                font-size: 18px; /* Adjust font size for smaller screens */
            }
        }

        @media (max-width: 480px) {
            .header {
                padding: 10px;
            }

            .navbar {
                gap: 8px;
            }

            .content {
                padding: 15px;
            }

            .content iframe {
                height: 150px;
            }

            .content table {
                font-size: 16px; /* Adjust font size for very small screens */
            }
            
        }
        #sup {
    text-transform: lowercase;
}

    </style>


</head>
<body>
    <div class="glass-container">
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
   <section class="contact"> 
    <div class="content">
    <h1>CONTACT US</h1>
        <table border=0 align="center">
        
            <tr align="center">
                <td><h2>Contact Number:</h2></td>
            </tr>
            <tr align="center">
                <td><h3 class="h">+91 99793 61589</h3></td>
            </tr>
            <tr align="center">
            <td><h2>Email:</h2></td>
            </tr>
            <tr align="center" id="sup">
            <td><h3 class="h" id="sup">apjethwa79@gmail.com</h3></td>
            </tr>
            <tr align="center">
            <td><h2>Address:</h2></td>
            </tr>
            <tr align="center">
            <td><h3 class="h">Near Panchayat Chowki, Chhaya Road, Porbandar-360575</h3></td>
            </tr>
            <tr align="center">
            <td rowspan=6><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3708.812033714133!2d69.625881474108!3d21.632246980172404!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x395635032b80bae5%3A0xd1dc5cdb5b94b442!2sMansi%20Photo%20%26%20Video!5e0!3m2!1sen!2sin!4v1718457593834!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></td>
            </tr>
           
</table>
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
    </div>
</body>
</html>