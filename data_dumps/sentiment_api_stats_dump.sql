-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: May 31, 2016 at 03:31 PM
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

REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision_without_neutral`, `precision_without_neutral_with_spam`, `recall`, `recall_with_spam`) VALUES(1, 'sentiment_api1', 0.519, 0.5221, '{"positive": 0.5, "neutral": 0.5416, "negative": 0.3333}', '{"positive": 0.5, "neutral": 0.5457, "negative": 0.3312}', '{"positive": 0.2162, "neutral": 0.8031, "negative": 0.2477}', '{"positive": 0.2178, "neutral": 0.8038, "negative": 0.2477}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision_without_neutral`, `precision_without_neutral_with_spam`, `recall`, `recall_with_spam`) VALUES(2, 'sentiment_api1_en', 0.5665, 0.5681, '{"positive": 0.5703, "neutral": 0.6071, "negative": 0.3828}', '{"positive": 0.5697, "neutral": 0.6108, "negative": 0.3791}', '{"positive": 0.3478, "neutral": 0.7378, "negative": 0.5421}', '{"positive": 0.349, "neutral": 0.7378, "negative": 0.5421}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision_without_neutral`, `precision_without_neutral_with_spam`, `recall`, `recall_with_spam`) VALUES(3, 'sentiment_api2', 0.5655, 0.5651, '{"positive": 0.6787, "neutral": 0.579, "negative": 0.2692}', '{"positive": 0.6678, "neutral": 0.5809, "negative": 0.2649}', '{"positive": 0.2271, "neutral": 0.8896, "negative": 0.229}', '{"positive": 0.2274, "neutral": 0.8842, "negative": 0.229}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision_without_neutral`, `precision_without_neutral_with_spam`, `recall`, `recall_with_spam`) VALUES(4, 'sentiment_api2_en', 0.6163, 0.6149, '{"positive": 0.713, "neutral": 0.6493, "negative": 0.3007}', '{"positive": 0.7045, "neutral": 0.6506, "negative": 0.2976}', '{"positive": 0.3961, "neutral": 0.8261, "negative": 0.4019}', '{"positive": 0.3959, "neutral": 0.8208, "negative": 0.4019}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision_without_neutral`, `precision_without_neutral_with_spam`, `recall`, `recall_with_spam`) VALUES(5, 'sentiment_api3', 0.3405, 0.3386, '{"positive": 0.469, "negative": 0.171}', '{"positive": 0.4673, "negative": 0.1692}', '{"positive": 0.686, "negative": 0.7336}', '{"positive": 0.6871, "negative": 0.7336}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision_without_neutral`, `precision_without_neutral_with_spam`, `recall`, `recall_with_spam`) VALUES(6, 'sentiment_api4', 0.4378, 0.4349, '{"positive": 0.4527, "negative": 0.3785}', '{"positive": 0.4502, "negative": 0.3741}', '{"positive": 0.93, "negative": 0.757}', '{"positive": 0.9302, "negative": 0.757}');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
