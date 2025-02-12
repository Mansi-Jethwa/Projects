-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 25, 2024 at 03:17 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `bills`
--

CREATE TABLE `bills` (
  `bill_id` int(11) NOT NULL,
  `invoice_number` varchar(20) NOT NULL,
  `customer_name` varchar(100) NOT NULL,
  `customer_contact` varchar(15) NOT NULL,
  `bill_date` datetime NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `discount_amount` decimal(10,2) NOT NULL,
  `net_payable` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bills`
--

INSERT INTO `bills` (`bill_id`, `invoice_number`, `customer_name`, `customer_contact`, `bill_date`, `subtotal`, `discount_amount`, `net_payable`) VALUES
(1, 'INV-8405', 'mansi', '9023609661', '2024-12-23 18:31:06', 40000.00, 2000.00, 38000.00),
(2, 'INV-4318', 'Mansi', '9023609661', '2024-12-23 18:37:32', 40000.00, 2000.00, 38000.00),
(4, 'INV-5026', 'Mansi', '9023609661', '2024-12-25 18:21:42', 60000.00, 3000.00, 57000.00),
(5, 'INV-1325', 'Mansi', '9023609661', '2024-12-25 18:21:50', 60000.00, 3000.00, 57000.00),
(6, 'INV-6169', 'Mansi', '9023609661', '2024-12-25 18:22:03', 60000.00, 3000.00, 57000.00),
(7, 'INV-8926', 'demo', '2323232323', '2024-12-25 18:31:22', 20000.00, 1000.00, 19000.00),
(8, 'INV-6952', 'Mansi', '9023609661', '2024-12-25 19:45:59', 40000.00, 2000.00, 38000.00),
(9, 'INV-5304', 'Mansi', '9023609662', '2024-12-25 19:46:20', 80000.00, 4000.00, 76000.00);

-- --------------------------------------------------------

--
-- Table structure for table `bill_items`
--

CREATE TABLE `bill_items` (
  `item_id` int(11) NOT NULL,
  `bill_id` int(11) NOT NULL,
  `item_name` varchar(100) NOT NULL,
  `item_price` decimal(10,2) NOT NULL,
  `item_qty` int(11) NOT NULL,
  `item_total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bill_items`
--

INSERT INTO `bill_items` (`item_id`, `bill_id`, `item_name`, `item_price`, `item_qty`, `item_total`) VALUES
(1, 8, 'Oppo Phone', 20000.00, 2, 40000.00),
(2, 9, 'Oppo Phone', 20000.00, 2, 40000.00),
(3, 9, 'LG Fridge', 20000.00, 2, 40000.00);

-- --------------------------------------------------------

--
-- Table structure for table `category_data`
--

CREATE TABLE `category_data` (
  `id` int(255) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category_data`
--

INSERT INTO `category_data` (`id`, `name`, `description`) VALUES
(101, 'TV', 'Tv'),
(102, 'Phones', 'Phones'),
(103, 'Refrigerator', 'Fridge');

-- --------------------------------------------------------

--
-- Table structure for table `employee_data`
--

CREATE TABLE `employee_data` (
  `empid` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(30) DEFAULT NULL,
  `contact` varchar(30) DEFAULT NULL,
  `employement_type` varchar(50) DEFAULT NULL,
  `education` varchar(50) DEFAULT NULL,
  `work_shift` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `doj` varchar(30) DEFAULT NULL,
  `salary` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee_data`
--

INSERT INTO `employee_data` (`empid`, `name`, `email`, `gender`, `dob`, `contact`, `employement_type`, `education`, `work_shift`, `address`, `doj`, `salary`, `usertype`, `password`) VALUES
(101, 'Mansi', 'mansijethwa27@gmail.com', 'Female', '25/12/2024', '9023609661', 'Part Time', 'LLM', 'Night', 'Behind Essar Petrol Pump		\n\n', '25/12/2024', '200000', 'Admin', 'Mansi@2715'),
(102, 'Neha', 'mansijethwa27@gmail.com', 'Female', '25/12/2024', '9023609661', 'Part Time', 'LLM', 'Evening', 'Behind Essar Petrol Pump		\n', '25/12/2024', '200000', 'Employee', 'Mansi@2715');

-- --------------------------------------------------------

--
-- Table structure for table `product_data`
--

CREATE TABLE `product_data` (
  `id` int(11) NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `supplier` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_data`
--

INSERT INTO `product_data` (`id`, `category`, `supplier`, `name`, `price`, `quantity`, `status`) VALUES
(1, 'Phones', 'Nayan Jethwa', 'Oppo Phone', 20000.00, 20, 'Active'),
(2, 'Refrigerator', 'Kajal Jethwa', 'LG Fridge', 20000.00, 21, 'Active'),
(3, 'TV', 'Amit Jethwa', 'LG TV', 20000.00, 23, 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `supplier_data`
--

CREATE TABLE `supplier_data` (
  `invoice` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `contact` varchar(30) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier_data`
--

INSERT INTO `supplier_data` (`invoice`, `name`, `contact`, `description`) VALUES
(101, 'Nayan Jethwa', '9023609661', 'supplier of phones'),
(102, 'Kajal Jethwa', '9023609661', 'Supplier of Refrigerator'),
(103, 'Amit Jethwa', '9023609662', 'Supplier of TV');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bills`
--
ALTER TABLE `bills`
  ADD PRIMARY KEY (`bill_id`),
  ADD UNIQUE KEY `invoice_number` (`invoice_number`);

--
-- Indexes for table `bill_items`
--
ALTER TABLE `bill_items`
  ADD PRIMARY KEY (`item_id`),
  ADD KEY `bill_id` (`bill_id`);

--
-- Indexes for table `category_data`
--
ALTER TABLE `category_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee_data`
--
ALTER TABLE `employee_data`
  ADD PRIMARY KEY (`empid`);

--
-- Indexes for table `product_data`
--
ALTER TABLE `product_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `supplier_data`
--
ALTER TABLE `supplier_data`
  ADD PRIMARY KEY (`invoice`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bills`
--
ALTER TABLE `bills`
  MODIFY `bill_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `bill_items`
--
ALTER TABLE `bill_items`
  MODIFY `item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `product_data`
--
ALTER TABLE `product_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill_items`
--
ALTER TABLE `bill_items`
  ADD CONSTRAINT `bill_items_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `bills` (`bill_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
