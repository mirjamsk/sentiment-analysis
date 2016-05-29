-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: May 29, 2016 at 11:50 AM
-- Server version: 5.5.42
-- PHP Version: 5.6.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `sentiment_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `im_post_sentiment`
--

CREATE TABLE IF NOT EXISTS `im_post_sentiment` (
  `id` int(11) NOT NULL,
  `idpost` int(11) NOT NULL,
  `sentiment_api1` longtext COLLATE utf8mb4_unicode_ci,
  `real_sentiment` longtext COLLATE utf8mb4_unicode_ci,
  `sentiment_api1_en` longtext COLLATE utf8mb4_unicode_ci,
  `sentiment_api2` longtext COLLATE utf8mb4_unicode_ci,
  `sentiment_api2_en` longtext COLLATE utf8mb4_unicode_ci,
  `sentiment_api3` longtext COLLATE utf8mb4_unicode_ci,
  `sentiment_api4` longtext COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `im_post_sentiment`
--
ALTER TABLE `im_post_sentiment`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `im_post_sentiment_idpost_47c83fa5_uniq` (`idpost`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `im_post_sentiment`
--
ALTER TABLE `im_post_sentiment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `im_post_sentiment`
--
ALTER TABLE `im_post_sentiment`
ADD FOREIGN KEY (`idpost`) REFERENCES `im_post` (`id`);

--
-- Insert records with forgein keys idpost from im_post
--

INSERT IGNORE INTO im_post_sentiment (idpost)
SELECT id FROM im_post;

--
-- Update sentiment columns with default value
--


UPDATE `im_post_sentiment`
SET
`real_sentiment` = '{"sentiment_stats": {"total": 0}, "sentiment_label": "", "total_comments": 0}',
`sentiment_api1` = '{"sentiment_stats": {"total": 0}, "sentiment_label": "", "total_comments": 0}',
`sentiment_api1_en` = '{"sentiment_stats": {"total": 0}, "sentiment_label": "", "total_comments": 0}',
`sentiment_api2` = '{"sentiment_stats": {"total": 0}, "sentiment_label": "", "total_comments": 0}',
`sentiment_api2_en` = '{"sentiment_stats": {"total": 0}, "sentiment_label": "", "total_comments": 0}',
`sentiment_api3` = '{"sentiment_stats": {"total": 0}, "sentiment_label": "", "total_comments": 0}',
`sentiment_api4` = '{"sentiment_stats": {"total": 0}, "sentiment_label": "", "total_comments": 0}';