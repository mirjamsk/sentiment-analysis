from akismet import Akismet
from base_spam import BaseSpam


class AkismetSpam(BaseSpam):
    def __init__(self):
        self.data = {
            'blog': 'sentiment-analysis6',
            'user_ip': '127.0.0.1',
            'comment_type': 'comment',
            'comment_author': 0,
            'user_agent': 'sentiment-analysis6/0.6.0'
        }
        self.db_column_en = 'spam_api1_en'
        self.db_column = 'spam_api1_with_comment_author_and_blog'
        # self.api_key = 'ade34decf355'
        self.api_key = 'c7f3ea2b654d'

        self.api = Akismet(self.api_key, 'sentiment-analysis6.ml')
        print ('Using AkismetSpamAPI')

    def is_spam(self, content, comment_author, post_id):
        self.data['comment_author'] = comment_author
        self.data['blog'] = post_id
        try:
            is_spam = self.api.comment_check(content, data=self.data)
        except UnicodeEncodeError:
            is_spam = self.api.comment_check(content.encode('utf-8'), data=self.data)
        return is_spam

    def get_db_column(self, use_en):
        return self.db_column_en if use_en else self.db_column
