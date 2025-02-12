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

// Get the booking details from the form submission
if (isset($_POST['id'])) {
    $booking_id = $_POST['id'];
    $name = $_POST['name'];
    $email = $_POST['email'];
    $mobile = $_POST['mobile'];
    $session_dates = $_POST['session_dates'];
    $address = $_POST['address'];
    $event_type = $_POST['event_type'];
    $package = $_POST['package'];
    $amount = $_POST['amount'];

    // Prepare and execute the SQL statement to update the booking
    $sql = "UPDATE bookings SET name = ?, email = ?, mobile = ?, session_dates = ?, address = ?, event_type = ?, package = ?, amount = ? WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssssssssi", $name, $email, $mobile, $session_dates, $address, $event_type, $package, $amount, $booking_id);
    
    if ($stmt->execute()) {
        // Successfully updated; Redirect to the booking history page
        header("Location: booking_history.php");
    } else {
        // Failed to update
        echo "Failed to update booking.";
    }
} else {
    // Invalid request
    echo "Invalid request.";
}

// Close the database connection
$conn->close();
?>
