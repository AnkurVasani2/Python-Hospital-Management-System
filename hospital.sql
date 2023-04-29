-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2023 at 10:03 PM
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
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `name` text NOT NULL,
  `id` int(3) NOT NULL,
  `start_of-shift` datetime DEFAULT NULL,
  `end_of_shift` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`name`, `id`, `start_of-shift`, `end_of_shift`) VALUES
('Dr. Vidhi Gupta', 1, '2020-09-14 07:00:00', '15:00:00'),
('Dr. Nitesh Pathak', 2, '2018-01-15 10:00:00', '18:00:00'),
('Dr. Daniel Fernandes', 3, '2023-03-30 09:00:00', '17:00:00'),
('Dr. Nicole Wilson', 4, '2023-01-02 08:00:00', '16:00:00'),
('Dr. Hrithik Parmar', 5, '2013-02-28 16:00:00', '22:00:00'),
('Dr. Kabir Sen', 6, '2015-12-07 11:30:00', '17:30:00'),
('Dr. Ashish Nayak', 7, '2022-03-04 12:00:00', '19:00:00'),
('Dr. Rajveer Kaur', 8, '2016-05-28 22:00:00', '04:00:00'),
('Dr. Anita Menon', 9, '2018-04-16 00:00:00', '06:00:00'),
('Dr. Parag Ajmera', 10, '2021-07-01 06:00:00', '12:00:00');

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
  `Allergies` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`Name`, `Patient_id`, `Email`, `Contact_number`, `Address`, `City`, `Dob`, `Gender`, `Weight(kg)`, `Height(inches)`, `Blood_group`, `Insurance_id`, `Allergies`) VALUES
('Darsha Mittal', 1, 'darsha1212@gmail.com', 7738472230, '142, Tulsi niwas, S Vivekanand Rd, Malad, Mumbai-400064', 'Mumbai', '2005-09-14', 'Femaile', 56, 59, 'B+', 'AB11840', 'Dust'),
('Adarsh Raval', 2, 'adarshraval@gmail.co', 9594531426, 'c-139, Akash Apartment, Agarkar Lane, Dahisar', 'Pune', '1997-09-01', 'Male', 60, 65, 'O+', 'AA1600', 'Milk'),
('Pooja Roy', 3, 'poojaroy04@gmail.com', 8892340884, '204, 12th Floor, Maker Tower, Near St Mary College, Bandra', 'Mumbai', '1977-04-11', 'Female', 55, 52, 'O-', 'YK3166', 'Swelling'),
('Vijay Goel', 4, 'goelvijay@gmail.com', 9657823555, 'Radheshyam Chs 4 Basement VishvaNagar, Goregaon', 'Mumbai', '1965-01-29', 'Male', 77, 69, 'A-', 'GZ1126', ' Walnuts'),
('Bharat Chopra', 5, 'bharat.c@gmail.com', 9783245091, 'A-102, Mody Estate, L B Shastri Road,Prabhadevi', 'Mumbai', '2001-11-11', 'Male', 80, 75, 'A+', 'XX2345', 'Peanuts'),
('Raj Malhotra', 6, 'raj.malhotra@gmail.c', 9876543210, '24 / Ram Mandir Indl Estate Ram Mandir Rd Nr Sharma Estate Goregaon, Mumbai,Mumb', 'Mumbai', '0000-00-00', 'Male', 80, 72, 'AB-', 'XY2473', 'Itching '),
('Sarika Sharma', 7, 'sarikasharma@gmail.c', 9876543210, '13 Varma Sadan ,Tejpal Scheme Rd , Shankar Rd, Vile Parle ,Mumbai,400057', 'Mumbai', '1983-02-18', 'Female', 49, 51, 'B-', 'GH8364', 'Olives'),
('Harry D\'souza', 8, 'harrydzsa@gmail.com', 9876543210, '23, st johns church lane, - Grant Road, Mumbai', 'Mumbai', '2000-07-18', 'Male', 68, 58, 'O+', 'AX3627', 'None'),
('Farhan Shaikh', 9, 'farhan8shaikh@gmail.', 9876543210, '14th Floor , Hotel Oasis Building, Shahid Bhagat Singh Road, Kurla Mumbai 400001', 'Mumbai', '1999-08-08', 'Male', 72, 70, 'A+', 'AZ3412', 'None'),
('Karan Ahuja', 10, 'ahujakaran@gmail.com', 8749320434, 'B-42, Dattani Apartment, Near BlueBird cafe, Churchgate(W) ', 'Mumbai', '1988-03-10', 'Male', 90, 72, 'O+', 'SD4719', 'Penicillin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`Patient_id`);

--
-- AUTO_INCREMENT for dumped tables
--

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
