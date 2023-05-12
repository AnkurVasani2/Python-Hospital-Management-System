-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2023 at 08:32 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `minii_project_2023`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `p_id` varchar(10) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `email` varchar(15) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `insurance` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `admission` date DEFAULT NULL,
  `discharge` date DEFAULT NULL,
  `total` float DEFAULT NULL,
  `bill_no` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`p_id`, `name`, `email`, `contact`, `insurance`, `dob`, `admission`, `discharge`, `total`, `bill_no`, `timestamp`) VALUES
('P000T', 'Ankur Vasani', 'ankurvasani2585', '7350760039', 'BT35LAT54A2M', '2005-08-25', '2023-04-30', '2023-05-02', 500, 1, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'BT35LAT54A2M', '1965-01-29', '2023-05-01', '2023-05-03', 0, 2, '2023-05-12 14:56:29'),
('P00003', 'Pooja Roy', 'poojaroy04@gmai', '8892340884', 'ASDF2342FGM', '1977-04-11', '2023-05-02', '2023-05-04', 0, 3, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'BT35LAT54A2M', '1965-01-29', '2023-05-02', '2023-05-03', 0, 4, '2023-05-12 14:56:29'),
('P00001', 'Darsha Mittal', 'darsha1212@gmai', '7738472230', '', '2005-09-14', '2023-05-12', '2023-05-17', 0, 5, '2023-05-12 14:56:29'),
('P00007', 'Sarika Sharma', 'sarikasharma@gm', '9876543210', 'GH8364', '1983-02-18', '2023-05-12', '2023-05-15', 0, 6, '2023-05-12 14:56:29'),
('P00003', 'Pooja Roy', 'poojaroy04@gmai', '8892340884', 'YK3166', '1977-04-11', '2023-05-12', '2023-05-16', 0, 7, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-19', 0, 8, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-17', 0, 9, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-16', 0, 10, '2023-05-12 14:56:29'),
('P00003', 'Pooja Roy', 'poojaroy04@gmai', '8892340884', 'YK3166', '1977-04-11', '2023-05-12', '2023-05-15', 0, 11, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-15', 0, 14, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-16', 0, 15, '2023-05-12 14:56:29'),
('P00001', 'Darsha Mittal', 'darsha1212@gmai', '7738472230', 'AB11840', '2005-09-14', '2023-05-12', '2023-05-16', 0, 16, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-11', 0, 17, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-16', 0, 18, '2023-05-12 14:56:29'),
('P00004', 'Vijay Goel', 'goelvijay@gmail', '9657823555', 'GZ1126', '1965-01-29', '2023-05-12', '2023-05-16', 0, 19, '2023-05-12 14:56:29'),
('P00001', 'Darsha Mittal', 'darsha1212@gmai', '7738472230', 'AB11840', '2005-09-14', '2023-05-12', '2023-05-16', 0, 20, '2023-05-12 14:57:07');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `name` text NOT NULL,
  `id` int(3) NOT NULL,
  `start_shift` varchar(10) NOT NULL,
  `end_shift` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`name`, `id`, `start_shift`, `end_shift`) VALUES
('Dr. Vidhi Gupta', 1, '7 am ', '3 pm'),
('Dr. Nitesh Pathak', 2, '8 am ', '5 pm'),
('Dr. Daniel Fernandes', 3, '9 am ', '5 pm'),
('Dr. Nicole Wilson', 4, '4 pm ', '10 pm'),
('Dr. Hrithik Parmar', 5, '11 am ', '7 pm'),
('Dr. Kabir Sen', 6, '8 am ', '4 pm'),
('Dr. Ashish Nayak', 7, '10 am ', '7 pm'),
('Dr. Rajveer Kaur', 8, '3 pm ', '11 pm'),
('Dr. Anita Menon', 9, '7 am ', '12 pm'),
('Dr. Parag Ajmera', 10, '10am ', '4 pm');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Name` varchar(20) NOT NULL,
  `ID` int(3) NOT NULL,
  `Username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Name`, `ID`, `Username`, `password`) VALUES
('Ankur Vasani', 36, 'admin_ankur', 'adm_ankur!'),
('Khushi Sanghvi', 3, 'admin_khushi', 'adm_khushi!'),
('Hetvi Patel', 40, 'admin_hetvi', 'adm_hetvi!');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `Name` text NOT NULL,
  `Patient_id` smallint(3) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Contact_number` bigint(11) NOT NULL,
  `Address` varchar(80) NOT NULL,
  `City` text NOT NULL DEFAULT 'Mumbai',
  `Dob` date NOT NULL,
  `Gender` text NOT NULL,
  `Weight(kg)` float NOT NULL,
  `Height(inches)` float NOT NULL,
  `Blood_group` varchar(4) NOT NULL,
  `Insurance_id` varchar(10) NOT NULL,
  `Allergies` text DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `patient_code` varchar(6) NOT NULL,
  `insurance` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`Name`, `Patient_id`, `Email`, `Contact_number`, `Address`, `City`, `Dob`, `Gender`, `Weight(kg)`, `Height(inches)`, `Blood_group`, `Insurance_id`, `Allergies`, `age`, `patient_code`, `insurance`) VALUES
('Darsha Mittal', 1, 'darsha1212@gmail.com', 7738472230, '142, Tulsi niwas, S Vivekanand Rd, Malad, Mumbai-400064', 'Mumbai', '2005-09-14', 'Femaile', 56, 59, 'B+', 'AB11840', 'Dust', 17, 'P00001', ''),
('Adarsh Raval', 2, 'adarshraval@gmail.co', 9594531426, 'c-139, Akash Apartment, Agarkar Lane, Dahisar', 'Pune', '1997-09-01', 'Male', 60, 65, 'O+', 'AA1600', 'Milk', 25, 'P00002', ''),
('Pooja Roy', 3, 'poojaroy04@gmail.com', 8892340884, '204, 12th Floor, Maker Tower, Near St Mary College, Bandra', 'Mumbai', '1977-04-11', 'Female', 55, 52, 'O-', 'YK3166', 'Swelling', 46, 'P00003', 'ASDF2342FGM'),
('Vijay Goel', 4, 'goelvijay@gmail.com', 9657823555, 'Radheshyam Chs 4 Basement VishvaNagar, Goregaon', 'Mumbai', '1965-01-29', 'Male', 77, 69, 'A-', 'GZ1126', ' Walnuts', 58, 'P00004', 'BT35LAT54A2M'),
('Bharat Chopra', 5, 'bharat.c@gmail.com', 9783245091, 'A-102, Mody Estate, L B Shastri Road,Prabhadevi', 'Mumbai', '2001-11-11', 'Male', 80, 75, 'A+', 'XX2345', 'Peanuts', 21, 'P00005', ''),
('Raj Malhotra', 6, 'raj.malhotra@gmail.c', 9876543210, '24 / Ram Mandir Indl Estate Ram Mandir Rd Nr Sharma Estate Goregaon, Mumbai,Mumb', 'Mumbai', '1997-10-10', 'Male', 80, 72, 'AB-', 'XY2473', 'Itching ', NULL, 'P00006', ''),
('Sarika Sharma', 7, 'sarikasharma@gmail.c', 9876543210, '13 Varma Sadan ,Tejpal Scheme Rd , Shankar Rd, Vile Parle ,Mumbai,400057', 'Mumbai', '1983-02-18', 'Female', 49, 51, 'B-', 'GH8364', 'Olives', 40, 'P00007', ''),
('Harry D\'souza', 8, 'harrydzsa@gmail.com', 9876543210, '23, st johns church lane, - Grant Road, Mumbai', 'Mumbai', '2000-07-18', 'Male', 68, 58, 'O+', 'AX3627', 'None', 22, 'P00008', ''),
('Farhan Shaikh', 9, 'farhan8shaikh@gmail.', 9876543210, '14th Floor , Hotel Oasis Building, Shahid Bhagat Singh Road, Kurla Mumbai 400001', 'Mumbai', '1999-08-08', 'Male', 72, 70, 'A+', 'AZ3412', 'None', 23, 'P00009', ''),
('Karan Ahuja', 10, 'ahujakaran@gmail.com', 8749320434, 'B-42, Dattani Apartment, Near BlueBird cafe, Churchgate(W) ', 'Mumbai', '1988-03-10', 'Male', 90, 72, 'O+', 'SD4719', 'Penicillin', 35, 'P00010', '');

--
-- Triggers `patient`
--
DELIMITER $$
CREATE TRIGGER `add_patient_code` BEFORE INSERT ON `patient` FOR EACH ROW BEGIN
  SET NEW.patient_code = CONCAT('P', LPAD(NEW.patient_id, 5, '0'));
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`bill_no`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`Patient_id`),
  ADD UNIQUE KEY `patient_code` (`patient_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `bill_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `Patient_id` smallint(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
