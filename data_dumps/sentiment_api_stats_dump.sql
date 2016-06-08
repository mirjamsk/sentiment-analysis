-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Jun 08, 2016 at 01:00 PM
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

REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(1, 'sentiment_api1', 0.5131, 0.5147, '{"positive": 0.5, "neutral": 0.5318, "negative": 0.3596}', '{"positive": 0.4922, "neutral": 0.5368, "negative": 0.3497}', '{"positive": 0.2119, "neutral": 0.8037, "negative": 0.256}', '{"positive": 0.2116, "neutral": 0.7995, "negative": 0.256}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(2, 'sentiment_api1_en', 0.566, 0.5659, '{"positive": 0.5746, "neutral": 0.5996, "negative": 0.4135}', '{"positive": 0.5683, "neutral": 0.6042, "negative": 0.4052}', '{"positive": 0.3453, "neutral": 0.7382, "negative": 0.564}', '{"positive": 0.3449, "neutral": 0.7341, "negative": 0.564}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(3, 'sentiment_api2', 0.5608, 0.5606, '{"positive": 0.6894, "neutral": 0.5694, "negative": 0.2872}', '{"positive": 0.6656, "neutral": 0.5732, "negative": 0.2828}', '{"positive": 0.2265, "neutral": 0.8944, "negative": 0.224}', '{"positive": 0.2273, "neutral": 0.8852, "negative": 0.224}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(4, 'sentiment_api2_en', 0.6136, 0.6119, '{"positive": 0.7231, "neutral": 0.6395, "negative": 0.3249}', '{"positive": 0.7048, "neutral": 0.6429, "negative": 0.3219}', '{"positive": 0.3924, "neutral": 0.8298, "negative": 0.412}', '{"positive": 0.3931, "neutral": 0.8206, "negative": 0.412}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(5, 'sentiment_api3', 0.4519, 0.4498, '{"positive": 0.5282, "neutral": 0.5355, "negative": 0.242}', '{"positive": 0.5217, "neutral": 0.5406, "negative": 0.2386}', '{"positive": 0.5661, "neutral": 0.329, "negative": 0.608}', '{"positive": 0.5655, "neutral": 0.3282, "negative": 0.608}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(6, 'sentiment_api4', 0.538, 0.5356, '{"positive": 0.5029, "neutral": 0.6093, "negative": 0.5528}', '{"positive": 0.4979, "neutral": 0.6155, "negative": 0.5433}', '{"positive": 0.7791, "neutral": 0.3307, "negative": 0.628}', '{"positive": 0.7794, "neutral": 0.3308, "negative": 0.628}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(7, 'sentiment_api3_without_neutral', 0.3405, 0.3386, '{"positive": 0.469, "negative": 0.171}', '{"positive": 0.4673, "negative": 0.1692}', '{"positive": 0.686, "negative": 0.7336}', '{"positive": 0.6871, "negative": 0.7336}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(8, 'sentiment_api4_without_neutral', 0.4378, 0.4349, '{"positive": 0.4527, "negative": 0.3785}', '{"positive": 0.4502, "negative": 0.3741}', '{"positive": 0.93, "negative": 0.757}', '{"positive": 0.9302, "negative": 0.757}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(9, 'sentiment_api1_emoji', 0.5975, 0.5978, '{"positive": 0.6503, "neutral": 0.6035, "negative": 0.3716}', '{"positive": 0.644, "neutral": 0.6083, "negative": 0.3617}', '{"positive": 0.4462, "neutral": 0.7862, "negative": 0.272}', '{"positive": 0.4457, "neutral": 0.7825, "negative": 0.272}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(10, 'sentiment_api1_en_emoji', 0.6434, 0.6427, '{"positive": 0.6676, "neutral": 0.686, "negative": 0.4316}', '{"positive": 0.6623, "neutral": 0.6902, "negative": 0.4239}', '{"positive": 0.5605, "neutral": 0.7243, "negative": 0.568}', '{"positive": 0.5599, "neutral": 0.7213, "negative": 0.568}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(11, 'sentiment_api2_emoji', 0.6757, 0.6731, '{"positive": 0.757, "neutral": 0.6767, "negative": 0.3626}', '{"positive": 0.7432, "neutral": 0.6799, "negative": 0.3568}', '{"positive": 0.5796, "neutral": 0.8403, "negative": 0.264}', '{"positive": 0.5801, "neutral": 0.8308, "negative": 0.264}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(12, 'sentiment_api2_en_emoji', 0.7181, 0.7141, '{"positive": 0.7596, "neutral": 0.7707, "negative": 0.3781}', '{"positive": 0.7465, "neutral": 0.773, "negative": 0.3741}', '{"positive": 0.7085, "neutral": 0.7888, "negative": 0.428}', '{"positive": 0.7088, "neutral": 0.7789, "negative": 0.428}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(13, 'sentiment_api3_emoji', 0.5433, 0.539, '{"positive": 0.5955, "neutral": 0.7093, "negative": 0.2821}', '{"positive": 0.5883, "neutral": 0.712, "negative": 0.2782}', '{"positive": 0.8251, "neutral": 0.3045, "negative": 0.632}', '{"positive": 0.8242, "neutral": 0.3027, "negative": 0.632}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(14, 'sentiment_api4_emoji', 0.5726, 0.5683, '{"positive": 0.5259, "neutral": 0.7273, "negative": 0.5509}', '{"positive": 0.52, "neutral": 0.7311, "negative": 0.5414}', '{"positive": 0.889, "neutral": 0.3141, "negative": 0.628}', '{"positive": 0.8891, "neutral": 0.3121, "negative": 0.628}');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
