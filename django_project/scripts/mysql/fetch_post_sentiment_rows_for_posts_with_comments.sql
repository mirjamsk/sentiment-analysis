SELECT * FROM im_post_sentiment
WHERE idpost in (
    SELECT DISTINCT(p.id)
    FROM  im_post AS p JOIN im_commento AS c ON p.id=c.idpost
);