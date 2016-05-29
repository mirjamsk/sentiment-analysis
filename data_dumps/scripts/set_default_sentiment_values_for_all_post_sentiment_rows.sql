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
