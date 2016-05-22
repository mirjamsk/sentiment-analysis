INSERT IGNORE INTO im_post_sentiment
(idpost)
SELECT id FROM im_post;