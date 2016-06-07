-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Jun 08, 2016 at 01:56 AM
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

REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(1, 'sentiment_api1', 0.519, 0.5221, '{"positive": 0.5, "neutral": 0.5416, "negative": 0.3333}', '{"positive": 0.5, "neutral": 0.5457, "negative": 0.3312}', '{"positive": 0.2162, "neutral": 0.8031, "negative": 0.2477}', '{"positive": 0.2178, "neutral": 0.8038, "negative": 0.2477}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(2, 'sentiment_api1_en', 0.5665, 0.5681, '{"positive": 0.5703, "neutral": 0.6071, "negative": 0.3828}', '{"positive": 0.5697, "neutral": 0.6108, "negative": 0.3791}', '{"positive": 0.3478, "neutral": 0.7378, "negative": 0.5421}', '{"positive": 0.349, "neutral": 0.7378, "negative": 0.5421}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(3, 'sentiment_api2', 0.5655, 0.5651, '{"positive": 0.6787, "neutral": 0.579, "negative": 0.2692}', '{"positive": 0.6678, "neutral": 0.5809, "negative": 0.2649}', '{"positive": 0.2271, "neutral": 0.8896, "negative": 0.229}', '{"positive": 0.2274, "neutral": 0.8842, "negative": 0.229}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(4, 'sentiment_api2_en', 0.6163, 0.6149, '{"positive": 0.713, "neutral": 0.6493, "negative": 0.3007}', '{"positive": 0.7045, "neutral": 0.6506, "negative": 0.2976}', '{"positive": 0.3961, "neutral": 0.8261, "negative": 0.4019}', '{"positive": 0.3959, "neutral": 0.8208, "negative": 0.4019}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(5, 'sentiment_api3', 0.4528, 0.4512, '{"positive": 0.5267, "neutral": 0.5523, "negative": 0.2263}', '{"positive": 0.5237, "neutral": 0.5542, "negative": 0.2235}', '{"positive": 0.5725, "neutral": 0.3303, "negative": 0.6121}', '{"positive": 0.5728, "neutral": 0.3285, "negative": 0.6121}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(6, 'sentiment_api4', 0.5373, 0.5353, '{"positive": 0.4981, "neutral": 0.6233, "negative": 0.5426}', '{"positive": 0.4954, "neutral": 0.6259, "negative": 0.5344}', '{"positive": 0.779, "neutral": 0.3303, "negative": 0.6542}', '{"positive": 0.7798, "neutral": 0.3285, "negative": 0.6542}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(7, 'sentiment_api3_without_neutral', 0.3405, 0.3386, '{"positive": 0.469, "negative": 0.171}', '{"positive": 0.4673, "negative": 0.1692}', '{"positive": 0.686, "negative": 0.7336}', '{"positive": 0.6871, "negative": 0.7336}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(8, 'sentiment_api4_without_neutral', 0.4378, 0.4349, '{"positive": 0.4527, "negative": 0.3785}', '{"positive": 0.4502, "negative": 0.3741}', '{"positive": 0.93, "negative": 0.757}', '{"positive": 0.9302, "negative": 0.757}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(9, 'sentiment_api1_emoji', 0.6016, 0.6038, '{"positive": 0.6475, "neutral": 0.6129, "negative": 0.3436}', '{"positive": 0.6464, "neutral": 0.6169, "negative": 0.3415}', '{"positive": 0.447, "neutral": 0.7866, "negative": 0.2617}', '{"positive": 0.4478, "neutral": 0.7875, "negative": 0.2617}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(10, 'sentiment_api1_en_emoji', 0.6429, 0.6442, '{"positive": 0.6638, "neutral": 0.6918, "negative": 0.4}', '{"positive": 0.6629, "neutral": 0.6952, "negative": 0.3973}', '{"positive": 0.5614, "neutral": 0.7249, "negative": 0.5421}', '{"positive": 0.5618, "neutral": 0.726, "negative": 0.5421}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(11, 'sentiment_api2_emoji', 0.6771, 0.6752, '{"positive": 0.7473, "neutral": 0.6861, "negative": 0.3393}', '{"positive": 0.7407, "neutral": 0.6872, "negative": 0.3333}', '{"positive": 0.5771, "neutral": 0.8344, "negative": 0.2664}', '{"positive": 0.5762, "neutral": 0.829, "negative": 0.2664}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(12, 'sentiment_api2_en_emoji', 0.717, 0.7142, '{"positive": 0.7494, "neutral": 0.7783, "negative": 0.3518}', '{"positive": 0.743, "neutral": 0.7785, "negative": 0.3477}', '{"positive": 0.706, "neutral": 0.7847, "negative": 0.4159}', '{"positive": 0.7047, "neutral": 0.7792, "negative": 0.4159}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(13, 'sentiment_api3_emoji', 0.5401, 0.5372, '{"positive": 0.591, "neutral": 0.7227, "negative": 0.2626}', '{"positive": 0.5877, "neutral": 0.7229, "negative": 0.2591}', '{"positive": 0.8253, "neutral": 0.3045, "negative": 0.6308}', '{"positive": 0.8247, "neutral": 0.3023, "negative": 0.6308}');
REPLACE INTO `im_sentiment_api_stats` (`id`, `api_id`, `accuracy`, `accuracy_with_spam`, `precision`, `precision_with_spam`, `recall`, `recall_with_spam`) VALUES(14, 'sentiment_api4_emoji', 0.5716, 0.5683, '{"positive": 0.5219, "neutral": 0.7445, "negative": 0.5367}', '{"positive": 0.5185, "neutral": 0.7457, "negative": 0.5285}', '{"positive": 0.8892, "neutral": 0.3137, "negative": 0.6495}', '{"positive": 0.8896, "neutral": 0.3104, "negative": 0.6495}');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
