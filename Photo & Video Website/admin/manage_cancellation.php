<?php
session_start();



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

// Get request ID and action from the POST request
$booking_id = $_POST['id'];
$action = $_POST['action'];

if ($action === 'approve') {
    // Update the booking status to cancelled and set the notification
    $sql = "UPDATE bookings SET status = 'Cancelled', cancellation_status = 'Approved', notification = 'Your booking cancellation request has been approved.' WHERE id = ?";
} elseif ($action === 'reject') {
    // Mark the cancellation request as rejected and set the notification
    $sql = "UPDATE bookings SET cancellation_status = 'Rejected', notification = 'Your booking cancellation request has been rejected.' WHERE id = ?";
}

$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $booking_id);
$stmt->execute();

header('Location: admin_panel.php');

// Close the statement and connection
$stmt->close();
$conn->close();
?>
