<?php
session_start(); // Start the session to access the username

// Check if the user is logged in
if (!isset($_SESSION['username'])) {
    die("<div class='container'><div class='message error-message'>User is not logged in.</div></div>");
}

// Database connection
$conn = new mysqli('localhost', 'root', '', 'admin_panel');

// Check connection
if ($conn->connect_error) {
    die("<div class='container'><div class='message error-message'>Connection failed: " . $conn->connect_error . "</div></div>");
}

// Get username from session
$userName = $_SESSION['username'];

// Get form data
$paymentMethod = $_POST['paymentMethod'];
$cardNumber = $_POST['cardNumber'];
$cardExpiry = $_POST['cardExpiry'];
$cardCVC = $_POST['cardCVC'];
$amount = $_POST['amount'];

// SQL to insert payment data
$sql = "INSERT INTO payments (user_name, payment_method, card_number, card_expiry, card_cvc, payment_amount) 
        VALUES ('$userName', '$paymentMethod', '$cardNumber', '$cardExpiry', '$cardCVC', '$amount')";

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Status</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .container {
            width: 60%;
            margin: 50px auto;
            padding: 30px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #4CAF50;
            margin-bottom: 20px;
            font-size: 24px;
            font-weight: bold;
        }
        .message {
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            font-size: 18px;
        }
        .success-message {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .error-message {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .button {
            display: inline-block;
            padding: 12px 24px;
            color: #ffffff;
            background-color: #4CAF50;
            border: none;
            border-radius: 6px;
            text-decoration: none;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #45a049;
        }
        .button-container {
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Payment Status</h1>
    <?php
    if ($conn->query($sql) === TRUE) {
        echo "<div class='message success-message'>Payment successfully processed.</div>";
    } else {
        echo "<div class='message error-message'>Error: " . $conn->error . "</div>";
    }
    $conn->close();
    ?>
    <div class="button-container">
        <a href="index.php" class="button">Return to Home</a>
    </div>
</div>

</body>
</html>
