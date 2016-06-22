-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Jun 22, 2016 at 09:59 AM
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

REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(1, 'sentiment_api1', 0.489, 0.4943, '{"positive": 0.5921, "neutral": 0.4746, "negative": 0.4005}', '{"positive": 0.5609, "neutral": 0.4961, "negative": 0.3511}', '{"positive": 0.2289, "neutral": 0.8136, "negative": 0.2941}', '{"positive": 0.2289, "neutral": 0.7896, "negative": 0.2941}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(2, 'sentiment_api1_en', 0.5581, 0.552, '{"positive": 0.663, "neutral": 0.5407, "negative": 0.4358}', '{"positive": 0.6313, "neutral": 0.5576, "negative": 0.3878}', '{"positive": 0.3781, "neutral": 0.7571, "negative": 0.5205}', '{"positive": 0.3781, "neutral": 0.722, "negative": 0.5205}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(3, 'sentiment_api2', 0.5414, 0.542, '{"positive": 0.7605, "neutral": 0.5182, "negative": 0.3472}', '{"positive": 0.6984, "neutral": 0.5366, "negative": 0.3181}', '{"positive": 0.276, "neutral": 0.8847, "negative": 0.2977}', '{"positive": 0.276, "neutral": 0.8486, "negative": 0.2977}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(4, 'sentiment_api2_en', 0.6099, 0.5994, '{"positive": 0.7886, "neutral": 0.5918, "negative": 0.3709}', '{"positive": 0.734, "neutral": 0.6056, "negative": 0.3407}', '{"positive": 0.4413, "neutral": 0.8244, "negative": 0.4688}', '{"positive": 0.4413, "neutral": 0.7781, "negative": 0.4688}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(5, 'sentiment_api3', 0.4985, 0.4871, '{"positive": 0.614, "neutral": 0.5028, "negative": 0.2861}', '{"positive": 0.5885, "neutral": 0.526, "negative": 0.2664}', '{"positive": 0.6165, "neutral": 0.338, "negative": 0.6364}', '{"positive": 0.6165, "neutral": 0.3307, "negative": 0.6364}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(6, 'sentiment_api4', 0.5796, 0.563, '{"positive": 0.5794, "neutral": 0.5705, "negative": 0.6007}', '{"positive": 0.5549, "neutral": 0.5908, "negative": 0.5445}', '{"positive": 0.7881, "neutral": 0.3465, "negative": 0.6328}', '{"positive": 0.7881, "neutral": 0.3357, "negative": 0.6328}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(7, 'sentiment_api3_without_neutral', 0.3405, 0.3386, '{"positive": 0.469, "negative": 0.171}', '{"positive": 0.4673, "negative": 0.1692}', '{"positive": 0.686, "negative": 0.7336}', '{"positive": 0.6871, "negative": 0.7336}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(8, 'sentiment_api4_without_neutral', 0.4378, 0.4349, '{"positive": 0.4527, "negative": 0.3785}', '{"positive": 0.4502, "negative": 0.3741}', '{"positive": 0.93, "negative": 0.757}', '{"positive": 0.9302, "negative": 0.757}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(9, 'sentiment_api1_emoji', 0.5866, 0.5851, '{"positive": 0.7204, "neutral": 0.5471, "negative": 0.4221}', '{"positive": 0.6909, "neutral": 0.5673, "negative": 0.37}', '{"positive": 0.4547, "neutral": 0.8009, "negative": 0.2995}', '{"positive": 0.4547, "neutral": 0.7741, "negative": 0.2995}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(10, 'sentiment_api1_en_emoji', 0.6453, 0.6342, '{"positive": 0.7361, "neutral": 0.628, "negative": 0.4612}', '{"positive": 0.7076, "neutral": 0.6436, "negative": 0.4099}', '{"positive": 0.5811, "neutral": 0.7462, "negative": 0.5187}', '{"positive": 0.5811, "neutral": 0.7111, "negative": 0.5187}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(11, 'sentiment_api2_emoji', 0.6789, 0.6681, '{"positive": 0.8107, "neutral": 0.64, "negative": 0.4161}', '{"positive": 0.7662, "neutral": 0.655, "negative": 0.3803}', '{"positive": 0.6138, "neutral": 0.8413, "negative": 0.3226}', '{"positive": 0.6138, "neutral": 0.8003, "negative": 0.3226}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(12, 'sentiment_api2_en_emoji', 0.735, 0.7151, '{"positive": 0.8184, "neutral": 0.7474, "negative": 0.4236}', '{"positive": 0.7743, "neutral": 0.757, "negative": 0.3893}', '{"positive": 0.7469, "neutral": 0.79, "negative": 0.4795}', '{"positive": 0.7469, "neutral": 0.7408, "negative": 0.4795}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(13, 'sentiment_api3_emoji', 0.5989, 0.5802, '{"positive": 0.6676, "neutral": 0.7065, "negative": 0.3276}', '{"positive": 0.6403, "neutral": 0.7233, "negative": 0.3057}', '{"positive": 0.8557, "neutral": 0.3173, "negative": 0.6435}', '{"positive": 0.8557, "neutral": 0.3072, "negative": 0.6435}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(14, 'sentiment_api4_emoji', 0.6266, 0.6059, '{"positive": 0.6035, "neutral": 0.7179, "negative": 0.6059}', '{"positive": 0.5771, "neutral": 0.7329, "negative": 0.557}', '{"positive": 0.9068, "neutral": 0.3319, "negative": 0.6275}', '{"positive": 0.9068, "neutral": 0.3189, "negative": 0.6275}');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
