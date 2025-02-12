<?php
session_start();
if (!isset($_SESSION['admin_logged_in'])) {
    header("Location: index.php");
    exit();
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

// Check if the booking ID is set in the URL
if (isset($_GET['id'])) {
    $id = $_GET['id'];

    // Delete the booking
    $sql = "DELETE FROM bookings WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $id);

    if ($stmt->execute()) {
        header("Location: cancellations.php?status=deleted");
    } else {
        echo "Error deleting booking: " . $conn->error;
    }

    $stmt->close();
} else {
    header("Location: cancellations.php");
}

$conn->close();
?>
