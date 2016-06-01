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
        self.select = "id, content, idpost"

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

        
class CommentSpamDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="spam_db"):
        Database.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd=passwd)
        self.table = "im_commento_sentiment"
        self.select = "id, idcommento, english_translation, real_sentiment, spam"

    def fetch_all(self, where=""):
        return super(CommentSpamDbConnection, self).fetch_all(
            select=self.select,
            from_clause=self.table,
            where=where,
            order_by="idcommento")

    def fetch_by_comment_id(self, id=""):
        return super(CommentSpamDbConnection, self).fetch_all(
            select=self.select,
            from_clause=self.table,
            where="idcommento='%d'" % id)

    def update(self, comment_id="", spam_column="", spam=""):
        return super(CommentSpamDbConnection, self).update(
            table=self.table,
            set={spam_column: spam},
            where="idcommento = %d" % comment_id)


class PostDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        Database.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd= passwd)
        self.table = "im_post"
        self.select = "id, content, link"

    def fetch_all(self, where=""):
        return super(PostDbConnection, self).fetch_all(select=self.select, from_clause=self.table, where=where)

    def fetch_by_id(self, id=""):
        return super(PostDbConnection, self).fetch_all(select=self.select, from_clause=self.table, where="id='%d'" %id)
