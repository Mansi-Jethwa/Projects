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

// Fetch notifications
$notification_sql = "SELECT id, name, notification FROM bookings WHERE notification IS NOT NULL AND notification != ''";
$notification_result = $conn->query($notification_sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <style>
        .card {
            cursor: pointer;
            text-decoration: none;
            color: inherit;
        }
        .card-body {
            display: flex;
            align-items: center;
        }
        .card-icon {
            font-size: 2rem;
            margin-right: 1rem;
        }
        .notification-card {
            margin-bottom: 1rem;
            border: 1px solid #ccc;
            padding: 15px;
            border-radius: 5px;
            background-color: #f8f9fa;
        }
        .notification-card h5 {
            margin: 0;
            font-size: 1.2rem;
            color: #333;
        }
        .notification-card p {
            margin: 0;
            font-size: 1rem;
            color: #666;
        }
    </style>
</head>
<body>
    <?php include 'includes/header.php'; ?>
    <div class="container-fluid">
        <div class="row">
            <?php include 'includes/sidebar.php'; ?>
            <main class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
                <h1 class="h2">Dashboard</h1>
                <div class="row">
                    <div class="col-md-4">
                        <a href="users.php" class="card">
                            <div class="card text-white bg-primary mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Manage Users</h5>
                                    <p class="card-text">View and manage registered users.</p>
                                </div>
                            </div>
                        </a>
                    </div>
                    <div class="col-md-4">
                        <a href="feedback.php" class="card">
                            <div class="card text-white bg-secondary mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Manage Feedback</h5>
                                    <p class="card-text">View and manage user feedback.</p>
                                </div>
                            </div>
                        </a>
                    </div>
                    <div class="col-md-4">
                        <a href="bookings.php" class="card">
                            <div class="card text-white bg-success mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Manage Bookings</h5>
                                    <p class="card-text">View and manage session bookings.</p>
                                </div>
                            </div>
                        </a>
                    </div>
                    <!-- Manage Notifications Section -->
                    <div class="col-md-4">
                        <a href="admin_panel.php" class="card">
                            <div class="card text-white bg-info mb-3">
                                <div class="card-body">
                                    <h5 class="card-title">Manage Notifications</h5>
                                    <p class="card-text">View and manage user notifications.</p>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>

                
            </main>
        </div>
    </div>
    <?php include 'includes/footer.php'; ?>

    <?php $conn->close(); ?>
</body>
</html>
