<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header('Location: login.php');
    exit;
}

// Database connection details
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "admin_panel";

// Create a new connection to the MySQL server
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the booking ID from the POST request
    $booking_id = $_POST['id'];
    $user_name = $_SESSION['username'];

    // Update the booking status to 'Cancellation Requested'
    $sql = "UPDATE bookings SET status = 'Cancellation Requested' WHERE id = ? AND name = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("is", $booking_id, $user_name);

    if ($stmt->execute()) {
        // Redirect back to booking_history.php with success status
        header('Location: booking_history.php?status=notification_sent');
    } else {
        // Redirect back to booking_history.php with error status
        header('Location: booking_history.php?status=notification_failed');
    }
    exit();
} else {
    // If the form is not submitted via POST, redirect to booking_history.php
    header('Location: booking_history.php');
    exit();
}

// Close the database connection
$conn->close();
?>
