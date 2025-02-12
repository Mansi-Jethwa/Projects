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

// Check if booking ID is provided
if (isset($_POST['id'])) {
    $booking_id = $_POST['id'];

    // Update the booking status to "Cancelled"
    $sql = "UPDATE bookings SET status = 'Cancelled' WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $booking_id);
    if ($stmt->execute()) {
        // Redirect to the booking history page with a success message
        header('Location: booking_history.php?status=cancel_requested');
        exit;
    } else {
        echo "Error updating record: " . $conn->error;
    }

    $stmt->close();
}

// Close the database connection
$conn->close();
?>
