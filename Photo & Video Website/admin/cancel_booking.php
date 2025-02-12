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
if (isset($_POST['id'])) {
    $booking_id = $_POST['id'];

    // Update the booking status to "Cancelled" and set notification_status to 0
    $sql = "UPDATE bookings SET status = 'Cancelled', notification_status = 0 WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $booking_id);
    if ($stmt->execute()) {
        // Redirect to the dashboard with a success message
        header('Location: dashboard.php?status=cancelled');
        exit;
    } else {
        echo "Error updating record: " . $conn->error;
    }

    $stmt->close();
}

// Close the database connection
$conn->close();
?>
