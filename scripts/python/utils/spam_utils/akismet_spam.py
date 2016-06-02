from base_api import BaseAPI
from akismet import Akismet


class AkismetSpamAPI(BaseAPI):
    def __init__(self):
        self.ApiKey = 'ade34decf355'
        self.api = Akismet(self.ApiKey, 'sentiment-analysis.ml')
        BaseAPI.__init__(
            self,
            # url='https://'+self.ApiKey+'akismet.com/1.1/comment-check',
        )

    def spam_check(self, content, post_url):
        data = {}
        data['user_ip'] = "127.0.0.1"
        data['user_agent'] = "Sentiment-analysis"
        data['blog'] = post_url
        data['comment_type'] = 'comment'
        return self.api.comment_check(content, data=data, build_data=False, DEBUG=False)
