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
                passwd=self.passwd,
                charset='utf8mb4',
                use_unicode=True
            )
            self.cursor = self.connection.cursor()
            print ("Database connection open")
        except MySQLdb.Error as e:
            print ("Error in connecting to db: %s" % e)

    def fetch_all(self, select="*", from_clause="", where="", order_by=""):
        sql = "SELECT %s FROM %s" % (select, from_clause)

        if where != "":
            sql += " WHERE %s" % where
        if order_by != "":
            sql += " ORDER BY %s" % order_by

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, table="", set={}, where=""):
        set_query = ''
        for column, value in set.items():
            set_query += "%s='%s'," % (column, value)

        set_query = set_query[:-1]  # remove the trailing comma (,)
        sql = "UPDATE %s SET %s WHERE %s" % (table, set_query, where)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Updating table %s, columns %s ..." % (table, ', '.join(set.keys())))
            print("%d row%s affected" % (self.cursor.rowcount, 's' if self.cursor.rowcount != 1 else ''))
        except MySQLdb.Error as e:
            print ("Error in updating db: %s" % e)

    def close(self):
        self.cursor.close()
        self.connection.close()
        print ("Database connection closed")
