from base_db import Database


class CommentDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        Database.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd=passwd)
        self.table = "im_commento"
        self.select = "id, content, idpost, from_id"

    def fetch_all(self, where=""):
        return super(CommentDbConnection, self).fetch_all(select=self.select, from_clause=self.table, where=where)

    def fetch_by_id(self, id=""):
        return super(CommentDbConnection, self).fetch_all(select=self.select, from_clause=self.table, where="id='%d'" %id)


class CommentSentimentDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        Database.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd=passwd)
        self.table = "im_commento_sentiment"
        self.select = "id, idcommento, english_translation, real_sentiment, spam"

    def fetch_all(self, select="", where=""):
        select = select if select != "" else self.select
        return super(CommentSentimentDbConnection, self).fetch_all(
            select=select,
            from_clause=self.table,
            where=where,
            order_by="idcommento")

    def fetch_by_comment_id(self, id=""):
        return super(CommentSentimentDbConnection, self).fetch_all(
            select=self.select,
            from_clause=self.table,
            where="idcommento='%d'" % id)

    def update(self, comment_id="", column="", value=""):
        return super(CommentSentimentDbConnection, self).update(
            table=self.table,
            set={column: value},
            where="idcommento = %d" % comment_id)

        
class CommentSpamDbConnection(CommentSentimentDbConnection):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        CommentSentimentDbConnection.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd=passwd)
        self.table = "im_commento_spam"
        self.select = "id, idcommento, spam_api1"


class CommentEmojiSentimentDbConnection(CommentSentimentDbConnection):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        CommentSentimentDbConnection.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd=passwd)
        self.table = "im_commento_sentiment_emoji"
        self.select = "id, idcommento"

    def fetch_sentiment_by_comment_id(self, sentiment="", comment_id=""):
        return super(CommentSentimentDbConnection, self).fetch_all(
            select=sentiment,
            from_clause=self.table,
            where="idcommento='%d'" % comment_id)