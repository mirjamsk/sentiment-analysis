# Sentiment analysis tesina


Live site lives on [sentiment-analysis.ml](http://sentiment-analysis.ml/)

--
#### Resources software:
+ [Django 1.9](https://www.djangoproject.com/)
+ [Django REST framework](http://www.django-rest-framework.org/)

--
#### Resources APIs:
The table maps used API's links to the column name in our database where the results of the API calls are stored

| API                  | Database column | 
|:--------------------:|:---------------:| 
| [vivekn][1]          | sentiment_api1  | 
| [text-processing][2] | sentiment_api2  |  


[1]: http://sentiment.vivekn.com/api/text/
[2]: http://text-processing.com/docs/sentiment.html

--
#### The developed API
Other than being able to access the API via a browser, it can also be done from the command-line, using tools like `curl`.
For e.g.
+ To get a list of posts:

 ``` bash
 curl -H 'Accept: application/json; indent=4' -u admin:sentiment1234 http://sentiment-analysis.ml/posts/
 ```
+ To get single post detail:

 ``` bash
 curl -H 'Accept: application/json; indent=4' -u admin:sentiment1234 http://sentiment-analysis.ml/posts/<id>/
 ```
+ To get a list of comments:

 ``` bash
 curl -H 'Accept: application/json; indent=4' -u admin:sentiment1234 http://sentiment-analysis.ml/comments/
 ```
+ To get single comment detail:

 ``` bash
 curl -H 'Accept: application/json; indent=4' -u admin:sentiment1234 http://sentiment-analysis.ml/comments/<id>/
 ```
 
--

####TO-DO:
+ Build front-end
+ Check reliability of the APIs
+ Clustering
  + [Weka](https://en.wikipedia.org/wiki/Weka_(machine_learning))
  + [Knime](https://www.knime.org/knime-cluster)
  + [Rapid miner](https://rapidminer.com/)
