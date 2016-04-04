import MySQLdb


class Database(object):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        self.db = db
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.cursor = None
        self.connection = None

    def connect(self):
        # Create Database connection
        if self.connection is not None:
            print ("Connection already exists")
        try:
            self.connection = MySQLdb.connect(
                db=self.db,
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd)
            self.cursor = self.connection.cursor()

        except MySQLdb.Error as e:
            print ("Error in connecting to db: %s" % e)

    def fetch_all(self, select="*", table="", where=""):
        sql = "SELECT %s FROM %s" % (select, table)
        if where != "":
            sql += " WHERE %s" % where

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, table="", set="", where=""):
        sql = "UPDATE %s SET %s WHERE %s" %(table, set, where)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except MySQLdb.Error as e:
            print ("Error in updating db: %s" % e)

    def close(self):
        self.cursor.close()
        self.connection.close()
        print ("Database connection closed")


class CommentDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        Database.__init__(self, host=host, port=port,  user=user, passwd=passwd, db=db )
        self.table = "im_commento"
        self.select = "id, content"

    def fetch_all(self, where=""):
        return super(CommentDbConnection, self).fetch_all(select=self.select, table=self.table, where=where)


class CommentSentimentDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        Database.__init__(self, host=host, port=port,  user=user, passwd=passwd, db=db )
        self.table = "im_commento_sentiment"
        self.select = "id, idcommento, real_sentiment"

    def fetch_all(self, where=""):
        return super(CommentSentimentDbConnection, self).fetch_all(select=self.select, table=self.table, where=where)

    def update(self, comment_id="", sentiment_api_column="", sentiment=""):
        return super(CommentSentimentDbConnection, self).update(
            table=self.table,
            set="%s = '%s'" %(sentiment_api_column, sentiment),
            where="idcommento = %d" % comment_id)
