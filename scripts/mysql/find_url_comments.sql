SELECT id, english_translation FROM im_commento_sentiment
WHERE 
english_translation REGEXP "(https?:[[:space:]]*\/\/|www\.)[\.A-Za-z0-9\-]+\.[a-zA-Z]{2,4}" OR 
english_translation REGEXP "[\.]{1}[A-Za-z0-9\-]+[\.]{1}[a-zA-Z]{2,4}[\.]?([[:space:]]|[[.slash.]]|$)"
OR (
english_translation NOT REGEXP "[[.commercial-at.]]{1}" AND
english_translation REGEXP "[[:alnum:]]+[\.]{1}(com|net|org|gov)([[:space:]]|[[.slash.]]|$)"
);