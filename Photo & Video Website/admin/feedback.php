<?php
session_start();
if (!isset($_SESSION['admin_logged_in'])) {
    header("Location: index.php");
    exit();
}

// Database configuration
$servername = "localhost"; // or your database server
$username = "root"; // or your database username
$password = ""; // or your database password
$dbname = "admin_panel";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch feedback data from the database
$sql = "SELECT id, name AS username, message AS feedback, submitted_at AS date FROM feedback ORDER BY submitted_at DESC";
$result = $conn->query($sql);

$feedback = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $feedback[] = $row;
    }
}

$conn->close();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Feedback</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <?php include 'includes/header.php'; ?>
    <div class="container-fluid">
        <div class="row">
            <?php include 'includes/sidebar.php'; ?>
            <main class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
                <h1 class="h2">Manage Feedback</h1>
                <div class="table-responsive">
                    <table class="table table-striped table-sm">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Username</th>
                                <th>Feedback</th>
                                <th>Date</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($feedback as $fb): ?>
                            <tr>
                                <td><?= htmlspecialchars($fb['id']) ?></td>
                                <td><?= htmlspecialchars($fb['username']) ?></td>
                                <td><?= htmlspecialchars($fb['feedback']) ?></td>
                                <td><?= htmlspecialchars($fb['date']) ?></td>
                                <td>
                                    <a href="delete_feedback.php?id=<?= htmlspecialchars($fb['id']) ?>" class="btn btn-sm btn-danger">Delete</a>
                                </td>
                            </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </main>
        </div>
    </div>
    <?php include 'includes/footer.php'; ?>
</body>
</html>
