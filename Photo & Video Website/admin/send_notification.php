<?php
session_start();

// Check if the admin is logged in
if (!isset($_SESSION['admin_logged_in']) || $_SESSION['admin_logged_in'] !== true) {
    header('Location: index.php');
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

// Check if booking ID is provided
if (isset($_GET['id'])) {
    $booking_id = $_GET['id'];

    // Fetch user details
    $sql = "SELECT name FROM bookings WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $booking_id);
    $stmt->execute();
    $stmt->bind_result($user_name);
    $stmt->fetch();
    $stmt->close();

    // Update the booking status to "Cancelled" and set notification_status to 1
    $sql = "UPDATE bookings SET status = 'Cancelled', notification_status = 1 WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $booking_id);
    if ($stmt->execute()) {
        // Redirect to the dashboard with a success message
        header('Location: dashboard.php?status=notified');
    } else {
        echo "Error updating record: " . $conn->error;
    }

    $stmt->close();
}

// Close the database connection
$conn->close();
?>
