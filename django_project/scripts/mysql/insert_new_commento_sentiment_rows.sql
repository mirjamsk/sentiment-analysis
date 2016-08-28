INSERT IGNORE INTO im_commento_sentiment
(idcommento)
SELECT id FROM im_commento;
