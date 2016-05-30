from base_db import Database


class SentimentApiStatsDbConnection(Database):
    def __init__(self, host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db"):
        Database.__init__(
            self,
            db=db,
            host=host,
            port=port,
            user=user,
            passwd=passwd)
        self.table = "im_sentiment_api_stats"
        self.select = "api_id, accuracy"

    def fetch_all(self, select="", where=""):
        select = select if select != "" else self.select
        return super(SentimentApiStatsDbConnection, self).fetch_all(
            select=select,
            from_clause=self.table,
            where=where)

    def fetch_by_api_id(self, api_id=""):
        return super(SentimentApiStatsDbConnection, self).fetch_all(
            select=self.select,
            from_clause=self.table,
            where="api_id='%d'" % api_id)

    def update(self, api_id="", column="", value=""):
        return super(SentimentApiStatsDbConnection, self).update(
            table=self.table,
            set={column: value},
            where="api_id = '%s'" % api_id)
