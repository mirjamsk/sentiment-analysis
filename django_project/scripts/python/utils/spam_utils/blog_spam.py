from ..api_utils.base_api import BaseAPI
import json


class BlogSpam(object):
    def __init__(self):
        data = {
            'site': 'http://sentiment-analysis.ml',
            'options': 'min-words=1',
            'comment': '',
            'name': 0,
            'ip': '127.0.1.1'
        }

        self.api = BaseAPI(
            data=data,
            url='http://test.blogspam.net:9999')

        self.db_column_en = 'spam_api2_en'
        self.db_column = 'spam_api2'

        print ('Using BlogSpam')

    def is_spam(self, comment_author, content, post_id):
        self.api.data['name'] = comment_author
        self.api.data['comment'] = content.encode('utf-8')

        self.api.post(dump_data_as_json=True)
        response = json.loads(self.api.response.text)

        print('Api response: %s' % response['result'])
        if response['result'] != 'OK':
            print('Api reason: %s' % response['reason'])

        return True if response['result']== 'SPAM' else False

    def get_db_column(self, use_en):
        return self.db_column_en if use_en else self.db_column
