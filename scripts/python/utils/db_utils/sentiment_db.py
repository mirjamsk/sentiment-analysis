from base_db import Database


class CommentDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        Database.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd= passwd)
        self.table = "im_commento"
        self.select = "id, content"

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
        self.select = "id, idcommento, english_translation, real_sentiment"

    def fetch_all(self, where=""):
        return super(CommentSentimentDbConnection, self).fetch_all(
            select=self.select,
            from_clause=self.table,
            where=where,
            order_by="idcommento")

    def fetch_by_comment_id(self, id=""):
        return super(CommentSentimentDbConnection, self).fetch_all(
            select=self.select,
            from_clause=self.table,
            where="idcommento='%d'" % id)

    def update(self, comment_id="", sentiment_api_column="", sentiment=""):
        return super(CommentSentimentDbConnection, self).update(
            table=self.table,
            set={sentiment_api_column: sentiment},
            where="idcommento = %d" % comment_id)
