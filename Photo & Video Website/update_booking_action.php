<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !== true) {
    header('Location: login.php');
    exit;
}

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "admin_panel";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if booking_id and other details are set
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['booking_id'])) {
    $booking_id = intval($_POST['booking_id']);
    $name = $_POST['name'];
    $email = $_POST['email'];
    $mobile = $_POST['mobile'];
    $session_date = $_POST['session_date'];
    $session_time_start = $_POST['session_time_start'];
    $session_time_end = $_POST['session_time_end'];
    $address = $_POST['address'];
    $event_type = $_POST['event_type'];
    $package = $_POST['package'];
    $amount = floatval($_POST['amount']);
    
    // Update the booking details
    $sql = "UPDATE bookings SET name = ?, email = ?, mobile = ?, session_date = ?, session_time_start = ?, session_time_end = ?, address = ?, event_type = ?, package = ?, amount = ? WHERE booking_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssssssssssi", $name, $email, $mobile, $session_date, $session_time_start, $session_time_end, $address, $event_type, $package, $amount, $booking_id);
    
    if ($stmt->execute()) {
        header('Location: booking_history.php');
        exit;
    } else {
        echo "Error updating booking: " . $conn->error;
    }
} else {
    echo "Invalid request.";
}

$conn->close();
?>
