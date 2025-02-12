<?php
$servername = "localhost"; // Change this if your server is different
$username = "root"; // Database username
$password = ""; // Database password
$dbname = "admin_panel"; // Database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
