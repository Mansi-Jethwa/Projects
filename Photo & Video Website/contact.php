<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    $loginButton = '<a href="login.php"><img src="enter.png" alt="Login"></a>';
} else {
    $loginButton = '<a href="logout.php"><img src="logout.png" alt="Logout"></a>';
}
?>
<?php
$servername = "localhost"; // Your server name
$username = "root"; // Your database username
$password = ""; // Your database password
$dbname = "admin_panel"; // Your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    $mobile = $conn->real_escape_string($_POST['mobile']);
    $session_dates = $conn->real_escape_string(implode(',', $_POST['session_dates']));
    
    $address = $conn->real_escape_string($_POST['address']);
    $event_type = $conn->real_escape_string($_POST['event_type']);
    $package = $conn->real_escape_string($_POST['package']);

    $sql = "INSERT INTO bill (name, email, mobile, session_dates,  address, event_type, package)
            VALUES ('$name', '$email', '$mobile', '$session_dates', '$address', '$event_type', '$package')";

    if ($conn->query($sql) === TRUE) {
        // Redirect to bill summary page with booking ID
        $booking_id = $conn->insert_id;
        header("Location: bill.php?id=" . $booking_id);
        exit();
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
    <!-- Swiper css link -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>

    <!-- font awesome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        .glass-container {
            background-image: url('bg1.jpg');
        }
        .book1 {
            margin: 20px auto;
            padding: 20px;
            border-radius: 8px;
        }
        .book1 table {
            width: 40%;
            border-collapse: collapse;
            background-color: rgba(255, 255, 255, 0.1);
            color: #000;
        }
        .lo {
            text-transform: lowercase;
        }
        .book1 tr {
            text-align: center;
        }
        .book1 td {
            padding: 10px;
            position: relative; /* Set relative positioning for td */
        }
        .book1 input, .book1 select, .book1 textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .book1 .btn {
            display: inline-block;
            padding: 10px 20px;
            color: #fff;
            background-color: #aaa;
            border: none;
            border-radius: 4px;
            text-decoration: none;
            font-size: 16px;
            cursor: pointer;
            width: 200px;
            transition: background-color 0.3s;
        }
        .book1 .btn:hover {
            background-color: #ff758c;
        }
        .error {
            color: red;
            font-size: 12px;
            position: absolute;
            bottom: -5px; /* Increased spacing from the input field */
            left: 12px; /* Spacing from the left of the input field */
            display: none;
        }
        .footer {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

.footer-content {
    margin-bottom: 10px;
}

.footer-section.social {
    display: flex;
    justify-content: center;
    gap: 15px;
}

.footer-section .social-link {
    color: #fff;
    font-size: 24px;
    text-decoration: none;
    transition: color 0.3s;
}

.footer-section .social-link:hover {
    color: #ff758c;
}

.footer-bottom {
    font-size: 24px;
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
            <?php echo $loginButton; ?>
        </nav>
        <div id="menu-btn" class="fas fa-bars"></div>
    </section>
    <!-- header section ends -->

    <div class="glass-container">
        <div class="book1">
            <center>
            <form id="bookingForm" action="bill.php" method="POST" onsubmit="return validateForm()">
                <table align="center" bgcolor="#efefef" height="300px" width="300px">
                    <tr align="center">
                        <td colspan="2" class="imr"><img src="MANSI.png" class="im"></td>
                    </tr>
                    <tr>
                        <td align="right" class="cp">Userame:</td>
                        <td>
                            <input type="text" name="name" id="name" value="<?php echo isset($_SESSION['username']) ? $_SESSION['username'] : ''; ?>" readonly>
                            <div id="nameError" class="error">Please enter your name.</div>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" class="cp">Email:</td>
                        <td>
                            <input type="text" name="email" id="email" class="lo">
                            <div id="emailError" class="error">Please enter a valid email address.</div>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" class="cp">Mobile Number:</td>
                        <td>
                            <input type="text" name="mobile" id="mobile" maxlength="10" pattern="[0-9]{10}" oninput="this.value = this.value.replace(/[^0-9]/g, '');">
                            <div id="mobileError" class="error">Please enter a valid 10-digit mobile number.</div>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" class="cp">Session Dates:</td>
                        <td>
                            <input type="text" name="session_dates[]" id="session_dates">
                            <div id="datesError" class="error">Please select at least one session date.</div>
                        </td>
                    </tr>
                    
                    <tr>
                        <td align="right" class="cp">Address:</td>
                        <td>
                            <textarea name="address" id="address"></textarea>
                            <div id="addressError" class="error">Please enter your address.</div>
                        </td>
                    </tr>
                    <tr>
                        <td align="right" class="cp">Event Type:</td>
                        <td>
                            <select name="event_type" id="event_type">
                                <option value="">Select Event</option>
                                <option value="Marriage">Marriage</option>
                                <option value="Birthday">Birthday</option>
                                <option value="Baby Shower">Baby Shower</option>
                                <option value="Engagement">Engagement</option>
                            </select>
                            <div id="eventTypeError" class="error">Please select an event type.</div>
                        </td>
                    </tr>
                    <tr>
                    <td align="right" class="cp">Select Package:</td>
                    <td>
                        <select name="package" id="package">
                            <option value="">Select Package</option>
                            <option value="Silver">Silver</option>
                            <option value="Golden">Golden</option>
                            <option value="Platinum">Platinum</option>
                            
                        </select>
                        <div id="packageError" class="error">Please select a package.</div>
                    </td>
                </tr>
                <tr>
                        <td colspan="2" align="center">
                            <button type="submit" class="btn">Submit</button>
                        </td>
                    </tr>
                </table>
            </form>
            </center>
        </div>
    </div>
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
</footer><!-- footer section ends -->
    <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            flatpickr("#session_dates", {
                mode: "multiple",
                dateFormat: "Y-m-d",
                minDate: "today",
                allowInput: true
            });
        });

        function validateForm() {
            let isValid = true;

            // Clear all error messages
            document.querySelectorAll('.error').forEach(function (error) {
                error.style.display = 'none';
            });

            // Name validation
            const name = document.getElementById('name').value;
            if (name.trim() === '') {
                document.getElementById('nameError').style.display = 'block';
                isValid = false;
            }

            // Email validation
            const email = document.getElementById('email').value;
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                document.getElementById('emailError').style.display = 'block';
                isValid = false;
            }

            // Mobile number validation
            const mobile = document.getElementById('mobile').value;
            const mobilePattern = /^[0-9]{10}$/;
            if (!mobilePattern.test(mobile)) {
                document.getElementById('mobileError').style.display = 'block';
                isValid = false;
            }

            // Session dates validation
            const sessionDates = document.getElementById('session_dates').value.split(' ').filter(date => date.trim() !== '');
            if (sessionDates.length === 0) {
                document.getElementById('datesError').style.display = 'block';
                isValid = false;
            }

            // Session time validation
            const sessionTimeStart = document.getElementById('session_time_start').value;
            const sessionTimeEnd = document.getElementById('session_time_end').value;
            if (sessionTimeStart.trim() === '' || sessionTimeEnd.trim() === '') {
                document.getElementById('timeError').style.display = 'block';
                isValid = false;
            }

            // Address validation
            const address = document.getElementById('address').value;
            if (address.trim() === '') {
                document.getElementById('addressError').style.display = 'block';
                isValid = false;
            }

            // Event type validation
            const eventType = document.getElementById('event_type').value;
            if (eventType.trim() === '') {
                document.getElementById('eventTypeError').style.display = 'block';
                isValid = false;
            }

            // Package validation
            const package = document.getElementById('package').value;
            if (package.trim() === '') {
                document.getElementById('packageError').style.display = 'block';
                isValid = false;
            }

            return isValid;
        }
    </script>
</body>
</html>
