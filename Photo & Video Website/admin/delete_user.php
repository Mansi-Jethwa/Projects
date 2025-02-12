<?php
session_start();
if (!isset($_SESSION['admin_logged_in'])) {
    header("Location: index.php");
    exit();
}

// Include the database connection
include 'includes/db_connect.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get the user ID from the form
    $user_id = $_POST['id'];

    // Prepare and bind the SQL statement to prevent SQL injection
    $stmt = $conn->prepare("DELETE FROM users WHERE id = ?");
    $stmt->bind_param("i", $user_id);

    if ($stmt->execute()) {
        // User deleted successfully
        $_SESSION['success_message'] = "User deleted successfully.";
    } else {
        // Error occurred while deleting user
        $_SESSION['error_message'] = "Error deleting user.";
    }

    $stmt->close();
    $conn->close();

    // Redirect back to the manage users page
    header("Location: users.php");
    exit();
} else {
    // If the request method is not POST, redirect to the manage users page
    header("Location: users.php");
    exit();
}
?>
