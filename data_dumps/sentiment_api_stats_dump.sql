-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Jun 27, 2016 at 03:27 PM
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

REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(1, 'sentiment_api1', 0.4764, 0.4867, '{"positive": 0.5965, "neutral": 0.4578, "negative": 0.3946}', '{"positive": 0.5583, "neutral": 0.4868, "negative": 0.3412}', '{"positive": 0.2172, "neutral": 0.8206, "negative": 0.2632}', '{"positive": 0.2172, "neutral": 0.7964, "negative": 0.2632}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(2, 'sentiment_api1_en', 0.5546, 0.5481, '{"positive": 0.6706, "neutral": 0.529, "negative": 0.4522}', '{"positive": 0.6323, "neutral": 0.5498, "negative": 0.3946}', '{"positive": 0.3683, "neutral": 0.7669, "negative": 0.5295}', '{"positive": 0.3683, "neutral": 0.7247, "negative": 0.5295}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(3, 'sentiment_api2', 0.5242, 0.5294, '{"positive": 0.7631, "neutral": 0.4977, "negative": 0.3327}', '{"positive": 0.6964, "neutral": 0.5223, "negative": 0.3019}', '{"positive": 0.2592, "neutral": 0.8872, "negative": 0.2663}', '{"positive": 0.2592, "neutral": 0.8512, "negative": 0.2663}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(4, 'sentiment_api2_en', 0.6028, 0.5917, '{"positive": 0.7978, "neutral": 0.5757, "negative": 0.3801}', '{"positive": 0.7324, "neutral": 0.5934, "negative": 0.3451}', '{"positive": 0.4292, "neutral": 0.8293, "negative": 0.475}', '{"positive": 0.4292, "neutral": 0.7752, "negative": 0.475}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(5, 'sentiment_api3', 0.4942, 0.4822, '{"positive": 0.616, "neutral": 0.4829, "negative": 0.2915}', '{"positive": 0.5841, "neutral": 0.5135, "negative": 0.2704}', '{"positive": 0.6007, "neutral": 0.336, "negative": 0.643}', '{"positive": 0.6007, "neutral": 0.3302, "negative": 0.643}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(6, 'sentiment_api4', 0.5786, 0.5596, '{"positive": 0.5839, "neutral": 0.5479, "negative": 0.6193}', '{"positive": 0.5541, "neutral": 0.5738, "negative": 0.5558}', '{"positive": 0.7752, "neutral": 0.3451, "negative": 0.6399}', '{"positive": 0.7752, "neutral": 0.3336, "negative": 0.6399}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(7, 'sentiment_api3_without_neutral', 0.3405, 0.3386, '{"positive": 0.469, "negative": 0.171}', '{"positive": 0.4673, "negative": 0.1692}', '{"positive": 0.686, "negative": 0.7336}', '{"positive": 0.6871, "negative": 0.7336}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(8, 'sentiment_api4_without_neutral', 0.4378, 0.4349, '{"positive": 0.4527, "negative": 0.3785}', '{"positive": 0.4502, "negative": 0.3741}', '{"positive": 0.93, "negative": 0.757}', '{"positive": 0.9302, "negative": 0.757}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(9, 'sentiment_api1_emoji', 0.5828, 0.5846, '{"positive": 0.7351, "neutral": 0.5342, "negative": 0.4126}', '{"positive": 0.7001, "neutral": 0.562, "negative": 0.3583}', '{"positive": 0.456, "neutral": 0.8093, "negative": 0.2678}', '{"positive": 0.456, "neutral": 0.7824, "negative": 0.2678}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(10, 'sentiment_api1_en_emoji', 0.649, 0.636, '{"positive": 0.7482, "neutral": 0.6215, "negative": 0.4793}', '{"positive": 0.7138, "neutral": 0.6406, "negative": 0.4178}', '{"positive": 0.5814, "neutral": 0.7573, "negative": 0.5265}', '{"positive": 0.5814, "neutral": 0.7145, "negative": 0.5265}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(11, 'sentiment_api2_emoji', 0.6734, 0.6656, '{"positive": 0.822, "neutral": 0.6259, "negative": 0.3876}', '{"positive": 0.776, "neutral": 0.6471, "negative": 0.3527}', '{"positive": 0.6124, "neutral": 0.8476, "negative": 0.2844}', '{"positive": 0.6124, "neutral": 0.8078, "negative": 0.2844}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(12, 'sentiment_api2_en_emoji', 0.7396, 0.717, '{"positive": 0.8307, "neutral": 0.7438, "negative": 0.4313}', '{"positive": 0.7801, "neutral": 0.7561, "negative": 0.3912}', '{"positive": 0.7507, "neutral": 0.7977, "negative": 0.4841}', '{"positive": 0.7507, "neutral": 0.7405, "negative": 0.4841}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(13, 'sentiment_api3_emoji', 0.6042, 0.583, '{"positive": 0.6756, "neutral": 0.7059, "negative": 0.3318}', '{"positive": 0.6426, "neutral": 0.7284, "negative": 0.308}', '{"positive": 0.8553, "neutral": 0.3168, "negative": 0.643}', '{"positive": 0.8553, "neutral": 0.3077, "negative": 0.643}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(14, 'sentiment_api4_emoji', 0.6292, 0.605, '{"positive": 0.61, "neutral": 0.7031, "negative": 0.6161}', '{"positive": 0.5785, "neutral": 0.7224, "negative": 0.5602}', '{"positive": 0.8995, "neutral": 0.3322, "negative": 0.6263}', '{"positive": 0.8995, "neutral": 0.3176, "negative": 0.6263}');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
