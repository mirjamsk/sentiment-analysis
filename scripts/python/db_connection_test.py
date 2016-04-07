import MySQLdb
from requests import post


#sentiment_api_url = "http://sentiment.vivekn.com/api/text/"
sentiment_api_url = "http://text-processing.com/api/sentiment/"
#SENTIMENT_LABELS = {
#  'Positive': 'positive', 
#  'Negative': 'negative',
#  'Neutral' : 'neutral'
#}
SENTIMENT_LABELS = {
  'pos': 'positive', 
  'neg': 'negative',
  'neutral' : 'neutral'
}


# Open database connection
db = MySQLdb.connect(host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db")
# prepare a cursor object using cursor() method
cursor = db.cursor()
db_sentiment = MySQLdb.connect(host="localhost", port=3306, user="sentiment_admin", passwd="sentiment1234", db="sentiment_db")
cursor_sentiment = db_sentiment.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM im_commento"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      ID = row[0]
      idpost = row[1]
      content = row[2]
      #data={"txt": content}
      data={"text": content}

      # Now print fetched result
      print "id=%s,idpost=%s,content=%s" % (ID, idpost, content )
      response = post(sentiment_api_url, data=data)
      print response.status_code
      if response.status_code == 200:
        #sentiment = response.json()['result']['sentiment']
        sentiment = response.json()['label']
        
        print SENTIMENT_LABELS[sentiment]
        cursor_sentiment.execute(
          "UPDATE im_commento_sentiment SET sentiment_api2 = '%s' WHERE idcommento = %d"
           %(SENTIMENT_LABELS[sentiment], ID)) 

except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
db_sentiment.commit()
db_sentiment.close()