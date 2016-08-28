SET NAMES utf8mb4;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER DATABASE sentiment_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE sentiment_db.im_post CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE sentiment_db.im_commento CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE sentiment_db.im_post_sentiment CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE sentiment_db.im_commento_sentiment CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

/*

Also edit the /etc/my.cnf file
(to find it's location use the following command: mysql --help | grep cnf  )



Make sure it has the following lines:

[client]
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4

[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

*/