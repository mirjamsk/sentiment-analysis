-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: May 30, 2016 at 11:56 PM
-- Server version: 5.5.42
-- PHP Version: 5.6.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sentiment_db`
--

--
-- Dumping data for table `im_sentiment_api_stats`
--

REPLACE INTO `im_sentiment_api_stats` VALUES(1, 'sentiment_api1', 0.519, 0.5221);
REPLACE INTO `im_sentiment_api_stats` VALUES(2, 'sentiment_api1_en', 0.5665, 0.5681);
REPLACE INTO `im_sentiment_api_stats` VALUES(3, 'sentiment_api2', 0.5655, 0.5651);
REPLACE INTO `im_sentiment_api_stats` VALUES(4, 'sentiment_api2_en', 0.6163, 0.6149);
REPLACE INTO `im_sentiment_api_stats` VALUES(5, 'sentiment_api3', 0.3405, 0.3386);
REPLACE INTO `im_sentiment_api_stats` VALUES(6, 'sentiment_api4', 0.4378, 0.4349);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
