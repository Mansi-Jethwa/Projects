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

// Fetch all bookings with a cancellation request
$sql = "SELECT id, name, email, session_dates, cancellation_status FROM bookings WHERE cancellation_status = 'Pending'";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel - Manage Cancellation Requests</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css"> <!-- Optional: Add your custom styles here -->
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 1.5rem;
            color: #343a40;
        }
        table {
            width: 100%;
            margin-bottom: 1rem;
            background-color: #fff;
            border-radius: .25rem;
            box-shadow: 0 0.125rem 0.25rem rgba(0,0,0,.075);
        }
        th, td {
            padding: 0.75rem;
            vertical-align: top;
            border-top: 1px solid #dee2e6;
        }
        thead th {
            background-color: #007bff;
            color: #fff;
            text-align: center;
        }
        tbody tr:nth-of-type(odd) {
            background-color: #f2f2f2;
        }
        button {
            margin: 0 5px;
        }
        .form-inline {
            display: inline;
        }
        .btn-approve {
            background-color: #28a745;
            color: #fff;
            border: none;
        }
        .btn-reject {
            background-color: #dc3545;
            color: #fff;
            border: none;
        }
        .btn {
            padding: 0.375rem 0.75rem;
            border-radius: 0.25rem;
            font-size: 1rem;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <?php include 'includes/header.php'; ?> <!-- Header inclusion -->
    <div class="container-fluid">
        <div class="row">
            <?php include 'includes/sidebar.php'; ?> <!-- Sidebar inclusion -->
            <main class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
                <h1>Manage Cancellation Requests</h1>
                <table class="table table-striped table-bordered">
                    <thead>
                        <tr>
                            <th>Booking ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Session Date</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php while ($row = $result->fetch_assoc()): ?>
                            <tr>
                                <td><?php echo htmlspecialchars($row['id']); ?></td>
                                <td><?php echo htmlspecialchars($row['name']); ?></td>
                                <td><?php echo htmlspecialchars($row['email']); ?></td>
                                <td><?php echo htmlspecialchars($row['session_dates']); ?></td>
                                <td>
                                    <form class="form-inline" action="manage_cancellation.php" method="POST">
                                        <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                                        <input type="hidden" name="action" value="approve">
                                        <button type="submit" class="btn btn-approve">Approve</button>
                                    </form>
                                    <form class="form-inline" action="manage_cancellation.php" method="POST">
                                        <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                                        <input type="hidden" name="action" value="reject">
                                        <button type="submit" class="btn btn-reject">Reject</button>
                                    </form>
                                </td>
                            </tr>
                        <?php endwhile; ?>
                    </tbody>
                </table>
            </main>
        </div>
    </div>
    <?php include 'includes/footer.php'; ?> <!-- Footer inclusion -->
</body>
</html>

<?php
// Close the database connection
$conn->close();
?>
