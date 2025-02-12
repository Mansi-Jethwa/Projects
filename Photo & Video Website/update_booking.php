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

// Get the booking ID from the form submission
if (isset($_POST['id'])) {
    $booking_id = $_POST['id'];

    // Prepare and execute the SQL statement to fetch booking details
    $sql = "SELECT * FROM bookings WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $booking_id);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        // Booking found; Redirect to the update page (e.g., update_booking_form.php)
        header("Location: update_booking_form.php?id=$booking_id");
    } else {
        // No booking found
        echo "No booking found.";
    }
} else {
    // Invalid request
    echo "Invalid request.";
}

// Close the database connection
$conn->close();
?>
